import blynklib
import time
import auth_vars
from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import threading

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

key_to_press = None

# ******************** SPEED HANDLERS ********************
@blynk.handle_event('write V1')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["SPEED_1"]
    else:
        key_to_press = None

@blynk.handle_event('write V2')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["SPEED_2"]
    else:
        key_to_press = None

@blynk.handle_event('write V3')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["SPEED_3"]
    else:
        key_to_press = None

@blynk.handle_event('write V4')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["SPEED_4"]
    else:
        key_to_press = None

# ******************** DIRECTION HANDLERS ********************
@blynk.handle_event('write V5')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["ARROW_UP"]
    else:
        key_to_press = None

@blynk.handle_event('write V6')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["ARROW_DOWN"]
    else:
        key_to_press = None

@blynk.handle_event('write V7')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["ARROW_LEFT"]
    else:
        key_to_press = None

@blynk.handle_event('write V8')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["ARROW_RIGHT"]
    else:
        key_to_press = None

# ******************** Z AXIS HANDLERS ********************
@blynk.handle_event('write V9')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["Z_DOWN"]
    else:
        key_to_press = None

@blynk.handle_event('write V10')
def handle_joystick_y(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = key_bindings["Z_UP"]
    else:
        key_to_press = None
    
# ******************** CONNECTION HANDLER ********************
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    print('Done.')

# ******************** MAIN LOOP ********************
def main():
    x = threading.Thread(target=press_thread, daemon=True)
    x.start()
    while True:
        blynk.run()
        #if key_to_press is not None:
            #press(key_to_press)

def press_thread():
    while True:
        if key_to_press is not None:
            press(key_to_press)

if __name__ == "__main__":
    main()