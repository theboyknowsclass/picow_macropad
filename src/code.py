import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
from pmk import PMK

pmk = PMK(Hardware())
pmk.set_all(255, 0, 255)
keys = pmk.keys

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

keymap =    [Keycode.ZERO,
             Keycode.ONE,
             Keycode.TWO,
             Keycode.THREE,
             Keycode.FOUR,
             Keycode.FIVE,
             Keycode.SIX,
             Keycode.SEVEN,
             Keycode.EIGHT,
             Keycode.NINE,
             Keycode.A,
             Keycode.B,
             Keycode.C,
             Keycode.D,
             Keycode.E,
             Keycode.SCROLL_LOCK]

for key in keys:
    @pmk.on_press(key)
    def press_handler(key):
        pmk.keys[key.number].set_led(255, 255, 255)
        keycode = keymap[key.number]
        keyboard.send(keycode)
        
    @pmk.on_release(key)
    def release_handler(key):
        pmk.keys[key.number].set_led(255, 0, 255)

while True:
    pmk.update()


#import time

# Set up a keyboard device.
#kbd = Keyboard(usb_hid.devices)


def tap_scroll_lock():
    kbd.press(Keycode.SCROLL_LOCK)
    time.sleep(.15)
    kbd.release(Keycode.SCROLL_LOCK)
    
def double_tap_scroll_lock():
    tap_scroll_lock()
    time.sleep(.25)
    tap_scroll_lock()
    time.sleep(.25)
    
def tap_two():
    kbd.press(Keycode.TWO)
    time.sleep(.15)
    kbd.release(Keycode.TWO)
    
#print(kbd.led_on(Keyboard.LED_SCROLL_LOCK))
#double_tap_scroll_lock()
#print(kbd.led_on(Keyboard.LED_SCROLL_LOCK))
#tap_two()
