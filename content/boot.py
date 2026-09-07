import board

from storage import disable_usb_drive, remount
from digitalio import DigitalInOut, Direction, Pull
from time import sleep

############################################################################################

# Initializes a switch. Returns the switch instance.
def _init_switch(pin):
	switch = DigitalInOut(pin) 
	switch.direction = Direction.INPUT
	switch.pull = Pull.UP
	sleep(0.05)
	return switch

# Is a switch pressed? 
def _is_switch_pressed(switch):
	return switch.value == False   # Inverse logic!

# Disables auto-reload (rebooting on every drive change). CircuitPython 7 has 
# supervisor.disable_autoreload(), which CircuitPython 8 replaced by supervisor.runtime.autoreload.
# No exception may escape here: any exception raised in boot.py aborts the whole file.
def _disable_autoreload():
	import supervisor

	try:
		supervisor.runtime.autoreload = False    # CircuitPython 8 and later
	except AttributeError:
		try:
			supervisor.disable_autoreload()      # CircuitPython 7 and earlier
		except AttributeError:
			pass

############################################################################################
 
# When this switch is pressed during boot, the USB drive will be mounted
_switch_mount_usb = _init_switch(board.GP1)       

############################################################################################

# No USB drive in normal operation, but we need to write on the drive via MIDI bridge. When the drive 
# stays mounted, code.py does not start the firmware at all (see the comments there).
if not _is_switch_pressed(_switch_mount_usb):	
    disable_usb_drive()
    remount("/", readonly = False)

# Disable autoreload (done last, so that a failure here cannot skip the USB drive handling above)
_disable_autoreload()
