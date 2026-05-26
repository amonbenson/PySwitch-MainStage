##############################################################################################################################################
#
# Definition of communication wrappers. This is where the client specific (i.e. Kemper) implementations are linked to the framework.
#
##############################################################################################################################################

from pyswitch.controller.midi import MidiRouting
from pyswitch.hardware.devices.pa_midicaptain import PA_MIDICAPTAIN_DIN_MIDI, PA_MIDICAPTAIN_USB_MIDI

# MIDI Devices in use (optionally you can specify the in/out channels here, too)
_DIN_MIDI = PA_MIDICAPTAIN_DIN_MIDI(
    in_channel = None,  # All
    out_channel = 0
)
_USB_MIDI = PA_MIDICAPTAIN_USB_MIDI(
    in_channel = None,  # All
    out_channel = 0
)

# Communication configuration
Communication = {

    # MIDI setup. This defines all MIDI routings. You at least have to define routings from and to
    # the MidiController.PYSWITCH source/target or the application will not be able to communicate!
    "midi": {
        "routings": [
            # MIDI Through: DIN to USB
            MidiRouting(
                source = _DIN_MIDI,
                target = _USB_MIDI
            ),

            # MIDI Through: USB to DIN
            MidiRouting(
                source = _USB_MIDI,
                target = _DIN_MIDI
            ),

            ###################################################

            # Application: Send MIDI messages to USB (buttons, expression inputs)
            MidiRouting(
                source = MidiRouting.APPLICATION,
                target = _USB_MIDI
            ),
        ]
    }
}
