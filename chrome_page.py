import pyautogui
import time

class ChromePage:
    def __init__(self):
        self.window_key = "win"
        self.chrome_app = "Google Chrome"
        self.enter_key = "Enter"
        self.wait_time = 1

    def open_chrome(self):
        pyautogui.press(self.window_key)
        pyautogui.write(self.chrome_app)
        pyautogui.press(self.enter_key)
        time.sleep(self.wait_time)