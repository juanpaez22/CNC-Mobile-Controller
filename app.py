import blynklib
import time
import auth_vars
from pyautogui import press, typewrite, hotkey, keyDown, keyUp
import threading

# ******************** SETUP ********************
key_bindings = {
    1: "1",         # Pin V1 -> Speed 1
    2: "2",         # Pin V2 -> Speed 2
    3: "3",         # Pin V3 -> Speed 3
    4: "4",         # Pin V4 -> Speed 4
    5: "up",        # Pin V5 -> Arrow up
    6: "down",      # Pin V6 -> Arrow down
    7: "left",      # Pin V7 -> Arrow left
    8: "right",     # Pin V8 -> Arrow right
    9: "pagedown",  # Pin V9 -> Z down
    10: "pageup",   # Pin V10 -> Z up
}

BLYNK_AUTH = auth_vars.BLYNK_AUTH
blynk = blynklib.Blynk(BLYNK_AUTH)
WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
CONNECT_PRINT_MSG = '[CONNECT_EVENT]'

key_to_press = None

# ******************** CONTROL HELPERS ********************
def handle_press_event(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value[0] == '1':
        press(key_bindings[pin])

def handle_hold_event(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_press
    if value[0] == '1':
        key_to_press = None
        keyDown(key_bindings[pin])
    else:
        key_to_press = None
        keyUp(key_bindings[pin])

def press_thread():
    while True:
        if key_to_press is not None:
            press(key_to_press)

# ******************** VIRTUAL PIN HANDLERS ********************
@blynk.handle_event('write V1')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V2')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V3')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V4')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V5')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V6')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V7')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V8')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V9')
def handle_pin(pin, value):
    handle_press_event(pin, value)

@blynk.handle_event('write V10')
def handle_pin(pin, value):
    handle_press_event(pin, value)
    
# ******************** CONNECTION HANDLER ********************
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    print('Done.')

# ******************** MAIN LOOP ********************
def main():
    # x = threading.Thread(target=press_thread, daemon=True)
    # x.start()
    while True:
        blynk.run()

if __name__ == "__main__":
    main()