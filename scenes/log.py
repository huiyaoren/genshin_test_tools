import time

import pyautogui

from scenes import GameScene
from tools import locate

# 场景：纪行


class LogScene(GameScene):
    @classmethod
    def load_complete(cls):
        locate('log_icon.png', once=False, threshold=0.7)
        time.sleep(0.3)

    @classmethod
    def into_game_scene(cls):
        locate('log_icon.png', once=False, threshold=0.7)
        time.sleep(1)
        pyautogui.press('esc')

    @staticmethod
    def receive_quest_prizes():
        locate('log_icon.png', once=False, threshold=0.7)
        time.sleep(1)

        location = locate('log_quest_icon.png', once=True)
        if location:
            pyautogui.click(*location)
            time.sleep(0.3)
            button_location = locate('log_quest_receive_button.png', once=True)
            if button_location:
                pyautogui.click(*button_location)
                time.sleep(3)

    @staticmethod
    def receive_log_prizes():
        locate('log_icon.png', once=False, threshold=0.7)
        time.sleep(1)

        location = locate('log_main_icon.png', once=True)
        if location:
            pyautogui.click(*location)
            time.sleep(0.5)
        button_location = locate('log_quest_receive_button.png', once=True)
        if button_location:
            pyautogui.click(*button_location)
            time.sleep(0.3)
            pyautogui.click(*locate('log_receive_confirm.png', once=False))
            time.sleep(3)
