import usb_hid
import storage
import usb_midi
import usb_cdc
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
from pmk import PMK
import time

pmk = PMK(Hardware())
keys = pmk.keys

boot_time = time.monotonic()
safe_mode = False
key = 0

while time.monotonic() - boot_time <= 1:
    pmk.set_all(0, 0, 0)
    pmk.keys[key].set_led(255, 0, 255)
    if key > 0:
        pmk.keys[key-1].set_led(200, 0, 200)
    pmk.update()

    if keys[15].pressed and keys[0].pressed:
        safe_mode = True
        
    if key >= 15:
        key = 0
    else:
        key = key + 1
    
# disable
usb_midi.disable()

if safe_mode:
    storage.enable_usb_drive()
    usb_cdc.enable(console=True, data=False)
else:
    storage.disable_usb_drive()
    usb_cdc.disable()

# enable
usb_hid.enable((usb_hid.Device.KEYBOARD,), boot_device=1)

pmk.set_all(255, 0, 255)
pmk.update()
print("safe mode:", "on" if safe_mode else "off")