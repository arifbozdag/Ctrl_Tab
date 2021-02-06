#author Arif.Bozdag

import keyboard
import time
import traceback

class alt_tab_modifier():
    
    def __init__(self): 
        self.alt_tab = False
        keyboard.on_press_key('tab', self.tab_event, suppress=True)
        keyboard.on_release_key('ctrl', self.ctrl_release_event, suppress=True)

    def tab_event(self, e):
        if self.alt_tab:
            pass            
        elif keyboard.is_pressed('ctrl'):
            keyboard.release('ctrl')
            keyboard.press('alt')
            self.alt_tab = True
        keyboard.send('tab')

    def ctrl_release_event(self, e):
        if self.alt_tab:
            keyboard.release('alt')
            self.alt_tab = False
        else:
            keyboard.release('ctrl')


if __name__ == "__main__":
    
    modifier = alt_tab_modifier()
    while True:
        time.sleep(0.1)
