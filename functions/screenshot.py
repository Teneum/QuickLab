import pygetwindow
import pyautogui
from PIL import Image
import time

from functions.configfuncs import set_image_paths


class CaptureShell:
    def __init__(self, name):
        self.name = name
        self.path = f'./screenshots/{self.name}.png'

    def set_path(self):
        set_image_paths(self.path)

    def capture(self):
        try:
            titles = pygetwindow.getAllTitles()
            win_title = ''
            for title in titles:
                if 'IDLE Shell' in title:
                    win_title = title
                    break
            else:
                return 'fail'
            window = pygetwindow.getWindowsWithTitle(win_title)[0]
            window.activate()
            x1, y1 = tuple(window.topleft)
            x2, y2 = tuple(window.bottomright)
            time.sleep(1)
            pyautogui.screenshot(self.path)
            im = Image.open(self.path)
            im = im.crop((x1, y1, x2, y2))
            im.save(self.path)
            self.set_path()
            return 'success'
        except Exception as e:
            print(e)


