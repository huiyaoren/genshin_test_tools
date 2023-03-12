import time

from pykeyboard import PyKeyboard
from pymouse import PyMouse

from positions import POSITION
from scenes import GameScene, MapScene


# 场景6：尘歌壶

class PotScene(GameScene):
    @staticmethod
    def receive_pot_prizes():
        k = PyKeyboard()
        m = PyMouse()

        time.sleep(1)
        k.press_key('a')
        time.sleep(1.5)
        k.release_key('a')
        time.sleep(0.3)
        k.tap_key('f')
        time.sleep(2.5)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(1)
        m.click(*POSITION['pot']['dialog_option_1'])  # 信任等阶 dialog_option_1
        time.sleep(1.5)
        m.click(*POSITION['pot']['friend_icon'])  # 领取好感 friend_icon
        time.sleep(0.5)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(0.5)
        m.click(*POSITION['pot']['money_icon'])  # 领取宝钱 money_icon
        time.sleep(0.5)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(0.5)
        k.tap_key(k.escape_key)  # 退出领取界面
        time.sleep(1)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(1)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(1)
        m.click(*POSITION['pot']['dialog_option_6'])  # 再见 dialog_option_6
        time.sleep(1)
        m.click(*POSITION['pot']['skip_dialog'])  # 跳过对话 skip_dialog
        time.sleep(1.5)

    @classmethod
    def into_game_scene(cls):
        """
        进入游戏界面
        :return:
        """
        k = PyKeyboard()
        m = PyMouse()
        time.sleep(1)
        k.tap_key('m')
        time.sleep(1)
        m.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        m.click(*POSITION['map']['tag_monde'])
        time.sleep(0.3)
        MapScene.transmit_to_monde()
        time.sleep(0.3)
