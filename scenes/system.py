import time

import pyautogui
from pymouse import PyMouse

from positions import POSITION
from scenes.common import CommonScene
from tools import locate


# 场景：操作系统
class SystemScene(CommonScene):

    @classmethod
    def into_loading_scene(cls):
        m = PyMouse()
        time.sleep(1)
        m.click(*POSITION['windows']['start_button'])
        time.sleep(0.5)
        m.click(*POSITION['windows']['genshin_icon'])
        time.sleep(0.5)
        location = locate('windows_genshin_start_button.jpg', once=False)
        time.sleep(1)
        pyautogui.click(*location)
        time.sleep(0.5)

    @staticmethod
    def game_close():
        m = PyMouse()
        time.sleep(1)
        m.click(*POSITION['windows']['genshin_close_button'])
        time.sleep(0.5)
