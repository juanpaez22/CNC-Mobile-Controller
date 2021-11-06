import blynklib
import time
import auth_vars
from pyautogui import press
import threading

# ******************** SETUP ********************
key_bindings = {
    1: "1",         # Pin V1 -> Speed 1 (0.025 mm)
    2: "2",         # Pin V2 -> Speed 2 (0.25 mm)
    3: "3",         # Pin V3 -> Speed 3 (1 mm)
    4: None,        # Pin V4 -> Change mode (single vs. hold)
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

mode_hold = True        # Hold or single press
key_to_hold = None     # Which key to press in background thread

# ******************** CONTROL HELPERS ********************
def handle_pin_event(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    global key_to_hold
    global mode_hold
    if value[0] == '1':
        if pin == 4:
            # Set single press mode
            key_to_hold = None
            mode_hold = False
        elif mode_hold:
            # Set key to hold using key binding map
            key_to_hold = key_bindings[pin]
        else:
            # Press single key using key binding map
            press(key_bindings[pin])
    else:
        if pin == 4:
            # Set hold mode
            key_to_hold = None
            mode_hold = True
        elif mode_hold:
            # Stop holding key
            key_to_hold = None
        else:
            pass

def hold_thread():
    while True:
        if key_to_hold is not None:
            press(key_to_hold)

# ******************** VIRTUAL PIN HANDLERS ********************
@blynk.handle_event('write V1')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V2')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V3')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V4')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V5')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V6')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V7')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V8')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V9')
def handle_pin(pin, value):
    handle_pin_event(pin, value)

@blynk.handle_event('write V10')
def handle_pin(pin, value):
    handle_pin_event(pin, value)
    
# ******************** CONNECTION HANDLER ********************
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    print('Done.')

# ******************** MAIN LOOP ********************
def main():
    t = threading.Thread(target=hold_thread, daemon=True)
    t.start()
    while True:
        blynk.run()

if __name__ == "__main__":
    main()
