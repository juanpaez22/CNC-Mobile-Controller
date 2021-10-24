import blynklib
import ctypes
from ctypes import wintypes
import time
import time
import auth_vars
from pyautogui import press, typewrite, hotkey

# ******************** SETUP ********************
key_bindings = {
    "ARROW_LEFT": "left",
    "ARROW_RIGHT": "right",
    "ARROW_UP": "up",
    "ARROW_DOWN": "down",
    "Z_UP": "pageup",
    "Z_DOWN": "pagedown",
    "SPEED_1": "1",
    "SPEED_2": "2",
    "SPEED_3": "3",
    "SPEED_4": "4",
}

BLYNK_AUTH = auth_vars.BLYNK_AUTH
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
CONNECT_PRINT_MSG = '[CONNECT_EVENT]'

# ******************** SPEED HANDLERS ********************
@blynk.handle_event('write V1')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["SPEED_1"])

@blynk.handle_event('write V2')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["SPEED_2"])

@blynk.handle_event('write V3')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["SPEED_3"])

@blynk.handle_event('write V4')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["SPEED_4"])

# ******************** DIRECTION HANDLERS ********************
@blynk.handle_event('write V5')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["ARROW_UP"])

@blynk.handle_event('write V6')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["ARROW_DOWN"])

@blynk.handle_event('write V7')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["ARROW_LEFT"])

@blynk.handle_event('write V8')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["ARROW_RIGHT"])

# ******************** Z AXIS HANDLERS ********************
@blynk.handle_event('write V9')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["Z_DOWN"])

@blynk.handle_event('write V10')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings["Z_UP"])
    
# ******************** CONNECTION HANDLER ********************
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    print('Done.')

# ******************** MAIN LOOP ********************
def main():
    while True:
        blynk.run()

if __name__ == "__main__":
    main()