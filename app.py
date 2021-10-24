import blynklib
import time
from . import secrets

BLYNK_AUTH = secrets.BLYNK_AUTH
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
CONNECT_PRINT_MSG = '[CONNECT_EVENT]'

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)

def main():
    print("hello world")
    while True:
        blynk.run()

if __name__ == "__main__":
    main()