from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
from threading import Thread, Event
from time import sleep

mouse = Controller()
active = Event()
last_key = None

def on_press(pressed_key):
    global last_key
    # if you try to call pressedKey.char when pressedKey is a key object, then
    # it throws an AttributeError and this thread closes
    if not isinstance(pressed_key, Key):
        if pressed_key.char == ']':
            if not isinstance(last_key, Key):
                if last_key.char == '[':
                    if active.is_set():
                        active.clear()
                    else:
                        active.set()
                        
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
