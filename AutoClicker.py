
import time
import win32api as wapi
import win32con as wcon

from getKeys import key_check

class AutoClicker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moveCursor(self.x, self.y)
        self.paused = False
        self.stop = False

    # Perform left mouse click at coordinates (x, y)
    def click(self):
        wapi.mouse_event(wcon.MOUSEEVENTF_LEFTDOWN, self.x, self.y, 0, 0)
        wapi.mouse_event(wcon.MOUSEEVENTF_LEFTUP, self.x, self.y, 0, 0)

    def moveCursor(self, x, y):
        self.x = x
        self.y = y
        wapi.SetCursorPos((self.x, self.y))

    # Start auto clicking
    def start(self):
        while True:
            if not self.paused:
                self.click()
                print("Click!")
            time.sleep(0.15) # delay

            self.checkPause()
            if self.stop:
                break

    # Check for pause conditions
    def checkPause(self):
        keys = key_check()
        if 'P' in keys:
            self.paused = not self.paused
        if 'Q' in keys:
            self.stop = True

