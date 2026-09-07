##############################################################################################################################################
#
# CircuitPython entry point.
#
# Holding switch 1 while powering up tells boot.py to leave the USB drive mounted. In that mode the
# firmware is not started at all: the display shows a notice and the board idles, so that copying files
# cannot be disturbed by the running application. Power cycle without switch 1 to run the firmware.
#
##############################################################################################################################################

# Created once by _usb_drive_enabled() and then left in place as an empty file, so that later boots do
# not write to the flash at all.
_PROBE_FILE = "/.usb_drive_check"


# Is the USB drive currently mounted on the host?
#
# The two modes differ in who may write to "/": in USB drive mode boot.py does not remount it, so it is
# writable for the host and read-only for CircuitPython, and in normal operation it is the other way
# round. Opening a file for writing tells them apart, without any side effect for the host.
#
# Do not use storage.remount() here. It only refuses to run once the host has really mounted the drive,
# so this early in the boot it usually succeeds instead of raising - and it then takes write access to
# the drive away from the host.
def _usb_drive_enabled():
    try:
        open(_PROBE_FILE, "ab").close()
    except OSError:
        return True

    return False


# Shows the USB drive mode notice and never returns.
def _run_usb_drive_mode():
    from displayio import Group, Bitmap, Palette, TileGrid
    from terminalio import FONT
    from adafruit_display_text.label import Label
    from time import sleep

    from pyswitch.hardware.adafruit import AdafruitST7789DisplayDriver

    display_driver = AdafruitST7789DisplayDriver()
    display_driver.init()

    background = Bitmap(display_driver.width, display_driver.height, 1)
    palette = Palette(1)
    palette[0] = 0x000030

    splash = Group()
    splash.append(
        TileGrid(
            background, 
            pixel_shader = palette
        )
    )

    # terminalio.FONT is built into CircuitPython and 6x12 pixels per character, so no font file has to
    # be read from the drive while the host is working on it.
    def add_text(text, scale, y):
        splash.append(
            Label(
                FONT,
                text = text,
                color = 0xffffff,
                scale = scale,
                x = int((display_driver.width - len(text) * 6 * scale) / 2),
                y = y
            )
        )

    add_text("USB DRIVE MODE", 2, 100)
    add_text("Firmware not running.", 1, 140)
    add_text("Power cycle without", 1, 158)
    add_text("switch 1 to start it.", 1, 172)

    display_driver.tft.show(splash)

    while True:
        sleep(0.5)


##############################################################################################################################################

if _usb_drive_enabled():
    _run_usb_drive_mode()
else:
    import pyswitch.process
