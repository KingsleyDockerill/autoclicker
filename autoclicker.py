from time import sleep
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key
from pynput.keyboard import Controller as Controllerk

pressed = False
delay = 0.1

def start():
    global pressed
    control = Controller()
    controlk = Controllerk()
    while pressed is False:
        global delay
        try:
            sleep(delay)
        except ValueError:
            print("Max speed reached!")
            delay += 0.01
        control.click(Button.left)
    pressed = False

def check(key):
    global delay
    if key == Key.shift_l:
        if threading.active_count() == 2:
            thread = threading.Thread(target=start)
            thread.start()
        else:
            delay -= 0.01
    elif key == Key.shift_r:
        global pressed
        pressed = True
        delay = 0.1


with Listener(on_press=check) as listen:
    listen.join()
