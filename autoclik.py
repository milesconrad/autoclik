from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
from threading import Thread, Event
from time import sleep
from datetime import datetime

mouse = Controller()
active = Event()
last_key = None

def on_press(pressed_key):
    global last_key
    # if you try to call pressedKey.char when pressedKey is a key object, then
    # it throws an AttributeError and this thread closes
    if not isinstance(pressed_key, Key):
        if pressed_key.char == ']':
            if last_key.char == '[':
                if active.is_set():
                    active.clear()
                    print(f"[{datetime.now().strftime("%H:%M:%S")}] Clicker deactivated")
                else:
                    active.set()
                    print(f"[{datetime.now().strftime("%H:%M:%S")}] Clicker activated")
                        
        last_key = pressed_key
    
def clicker():
    while True:
        active.wait()
        mouse.click(Button.left)
        sleep(0.005)

clickerThread = Thread(target=clicker)
listenerThread = Listener(on_press=on_press)

listenerThread.start()
clickerThread.start()

listenerThread.join()
clickerThread.join()
