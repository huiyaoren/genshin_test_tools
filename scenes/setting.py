import time

import pyautogui
from pykeyboard import PyKeyboard
from pymouse import PyMouse

from positions import POSITION
from scenes.common import CommonScene
from tools import loading, locate


# 场景5：设置界面
class SettingScene(CommonScene):

    @classmethod
    def into_loading_scene(cls):
        m = PyMouse()
        time.sleep(1)
        m.click(*POSITION['setting']['exit'])
        time.sleep(0.3)
        m.click(*POSITION['setting']['confirm'])
        time.sleep(0.3)
        loading(POSITION['loading']['into_button'], 'loading_into_button')
        time.sleep(0.3)

    @classmethod
    def into_game_scene(cls):
        k = PyKeyboard()
        time.sleep(1)
        k.tap_key(k.escape_key)
        time.sleep(1)

    @classmethod
    def receive_mail(cls):
        position = locate('setting_mail_button.png')
        pyautogui.click(*position)
        time.sleep(0.3)
        while 1:
            if locate('mail_delete.png'):
                break
            position = locate('mail_receive_button.png')
            if position is not None:
                pyautogui.click(*position)
                time.sleep(0.3)
                pyautogui.click(*locate('mail_receive_confirm.png', once=False))
                break

        time.sleep(0.3)
        pyautogui.click(*locate('mail_close.png', once=False))
        time.sleep(0.5)

