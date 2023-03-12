import time

import pyautogui
from pykeyboard import PyKeyboard

from positions import POSITION
from tools import loading, locate


class CommonScene:
    @classmethod
    def into_setting_scene(cls):
        """
        进入设置界面
        :return:
        """
        k = PyKeyboard()
        time.sleep(1)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(0.3)
        k.tap_key(k.escape_key)
        time.sleep(1)

    @classmethod
    def into_map_scene(cls):
        """
        进入地图界面
        :return:
        """
        k = PyKeyboard()
        time.sleep(1)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(0.3)
        k.tap_key('m')
        locate('map/button/close.png', once=False)
        time.sleep(0.3)
        pyautogui.click(*locate('map/zoom/down.png', once=False), clicks=5, interval=0.1)
        pyautogui.click(*locate('map/zoom/up.png', once=False), clicks=2, interval=0.2)
        time.sleep(0.5)

    @classmethod
    def into_system_scene(cls):
        pass

    @classmethod
    def into_loading_scene(cls):
        pass

    @classmethod
    def into_game_scene(cls):
        pass

    @classmethod
    def into_pot_scene(cls):
        pass

    @staticmethod
    def load_complete():
        pass

    # @classmethod
    # def into(cls, scene_class):
    #     if scene_class == SystemScene:
    #         return cls.into_system_scene()
    #     elif scene_class == LoadingScene:
    #         return cls.into_loading_scene()
    #     elif scene_class == GameScene:
    #         return cls.into_game_scene()
    #     elif scene_class == MapScene:
    #         return cls.into_map_scene()
    #     elif scene_class == SettingScene:
    #         return cls.into_setting_scene()
    #     elif scene_class == PotScene:
    #         return cls.into_pot_scene()
