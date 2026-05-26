from adafruit_midi import MIDI as _MIDI
from adafruit_midi.midi_message import MIDIUnknownEvent as _MIDIUnknownEvent
from busio import UART as _UART


# Wraps a UART and re-inserts the running-status byte that adafruit_midi's parser
# would otherwise skip, because adafruit_midi has no running-status support.
# Running status: a keyboard omits repeated status bytes for consecutive messages
# of the same type (e.g. multiple NoteOns in a chord).  Without this wrapper every
# note after the first in a chord is permanently discarded.
class _RunningStatusUART:

    # Expected total byte-count (status + data) for each channel-message class
    _MSG_LEN = {
        0x80: 3, 0x90: 3, 0xA0: 3, 0xB0: 3,  # NoteOff, NoteOn, PolyPress, CC
        0xC0: 2, 0xD0: 2,                        # ProgramChange, ChannelPressure
        0xE0: 3,                                  # PitchBend
    }

    def __init__(self, uart):
        self._uart    = uart
        self._status  = 0   # last channel-message status byte seen
        self._expected = 0  # total bytes in that message type (incl. status)
        self._count    = 0  # bytes consumed in current message (incl. status)
        self._sysex    = False

    def read(self, n):
        raw = self._uart.read(n)
        if not raw:
            return raw

        result = bytearray()
        for byte in raw:
            if byte & 0x80:                        # --- status byte ---
                if byte == 0xF0:                   # SysEx start
                    self._sysex   = True
                    self._status  = 0              # SysEx cancels running status
                    self._count   = 0
                    self._expected = 0
                elif byte == 0xF7:                 # SysEx end
                    self._sysex = False
                elif byte >= 0xF8:                 # System Realtime — pass through,
                    pass                           # does NOT cancel running status
                else:                              # Channel message status
                    self._sysex    = False
                    self._status   = byte
                    self._expected = self._MSG_LEN.get(byte & 0xF0, 0)
                    self._count    = 1
                result.append(byte)
            else:                                  # --- data byte ---
                if not self._sysex:
                    if self._count == 0 or self._count >= self._expected:
                        # Start of a new running-status message: re-insert status
                        if self._status:
                            result.append(self._status)
                            self._expected = self._MSG_LEN.get(self._status & 0xF0, 0)
                            self._count    = 1
                    self._count += 1
                result.append(byte)

        return bytes(result) if result else None


# DIN MIDI Device
class AdafruitDinMidiDevice:
    def __init__(self,
                 gpio_in,
                 gpio_out,
                 in_buf_size,
                 baudrate,
                 timeout,
                 in_channel = None,   # All
                 out_channel = 0,
        ):

        midi_uart = _UART(
            gpio_in,
            gpio_out,
            baudrate = baudrate,
            timeout = timeout
        )

        self.__midi = _MIDI(
            midi_out = midi_uart,
            out_channel = out_channel,
            midi_in = _RunningStatusUART(midi_uart),
            in_channel = in_channel,
            in_buf_size = in_buf_size
        )

    # def __repr__(self):
    #     return "DIN"

    def send(self, midi_message):
        if isinstance(midi_message, _MIDIUnknownEvent):
            return

        self.__midi.send(midi_message)

    def receive(self):
        return self.__midi.receive()
