import time

from pymouse import PyMouse

from positions import POSITION
from scenes.common import CommonScene
from tools import loading


# 场景：载入界面
class LoadingScene(CommonScene):

    @classmethod
    def into_game_scene(cls):
        m = PyMouse()
        time.sleep(1)
        loading(POSITION['loading']['into_button'], 'loading_into_button')
        time.sleep(0.3)
        m.click(*POSITION['loading']['into_button'][:2])
        time.sleep(60)

    @classmethod
    def into_system_scene(cls):
        m = PyMouse()
        time.sleep(1)
        m.click(*POSITION['loading']['exit_button'])
        time.sleep(0.3)
        m.click(*POSITION['loading']['confirm'])
        time.sleep(0.3)
        loading(POSITION['windows']['genshin_start_button'], 'windows_genshin_start_button')
        time.sleep(0.3)
