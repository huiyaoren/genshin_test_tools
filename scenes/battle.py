import time

import pyautogui

from positions import POSITION
from scenes.common import CommonScene
from tools import loading


class BattleScene(CommonScene):
    @classmethod
    def hit_3(cls):
        """
        三连击
        :return:
        """
        # time.sleep(1)
        pyautogui.click(clicks=3, interval=0.6)
        time.sleep(0.1)
        pyautogui.click(button='right')

    @classmethod
    def shift(cls, reverse=False):
        """
        游走
        :return:
        """
        time.sleep(1)
        pyautogui.keyDown('a' if reverse else 'd')
        time.sleep(0.5)
        pyautogui.keyDown('d' if reverse else 'a')
        pyautogui.keyUp('a' if reverse else 'd')
        time.sleep(0.5)
        pyautogui.keyUp('d' if reverse else 'a')
        pyautogui.press('s')
        pyautogui.press('w')

    @classmethod
    def skill_e(cls, once=False):
        while 1:
            match = loading(POSITION['game']['skill_e'], 'game_skill_e', once=once)
            if match:
                pyautogui.press('e')
                return match
            if once:
                return match
