#author Arif.Bozdag

import keyboard
import time
from datetime import datetime
import traceback

def main():
    try:
        print("hi")
        keyboard.remap_hotkey('ctrl+tab', 'alt+tab')
        while True:
            time.sleep(0.5)
    except:
        traceback.print_exc()

def do_this():
    try:
        keyboard.press("a")
    except:
        pass

if __name__ == "__main__":
    main()
