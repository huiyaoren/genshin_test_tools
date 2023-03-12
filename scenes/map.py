import time

import pyautogui
from pymouse import PyMouse

from positions import POSITION
from scenes.common import CommonScene
from tools import loading, locate


# 场景4：地图界面
class MapScene(CommonScene):

    @classmethod
    def switch_tag(cls, name):
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['tag_{}'.format(name)])
        time.sleep(0.3)

    @staticmethod
    def transmit_to_monde():
        """
        传送至蒙德
        :return:
        """
        time.sleep(1.5)
        # todo loading
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        if not locate('map/tag/mondstadt.png'):
            pyautogui.click(*locate('map/tag/liyue.png'))
            time.sleep(0.3)
            pyautogui.click(*POSITION['map']['switch_tag_button'])
            time.sleep(0.3)
        pyautogui.click(*locate('map/tag/mondstadt.png'))
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['place_monde'])
        time.sleep(1)
        pyautogui.click(*locate('map/item/waypoint.png'))
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(0.3)

    @staticmethod
    def transmit_to_monde_2():
        """
        传送至蒙德
        :return:
        """
        time.sleep(1.5)
        # todo loading
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['tag_liyue'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['tag_monde'])
        time.sleep(0.3)
        while 1:
            position = locate('map/waypoint/mondstadt_brightcrown_mountains_1.png', threshold=0.75)
            if position is not None:
                break
        time.sleep(0.3)
        # 选中传送点
        pyautogui.click(*position)
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['item_1_in_2'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(0.3)

    @classmethod
    def transmit_to_monde_mingguangxia(cls):
        """
        传送至蒙德明冠峡
        :return:
        """
        time.sleep(1.5)
        # todo loading
        cls.switch_tag('liyue')
        cls.switch_tag('monde')
        while 1:
            position = locate('map/waypoint/mondstadt_brightcrown_mountains_1.png', threshold=0.75)
            if position is not None:
                break
        time.sleep(0.3)
        # 选中传送点
        pyautogui.click(*position)
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['item_1_in_2'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)

    @staticmethod
    def transmit_to_monde_benlanglin():
        """
        传送至蒙德奔狼领
        :return:
        """
        time.sleep(1.5)
        # todo loading
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['tag_liyue'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['tag_monde'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['place_monde_benlanglin'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['item_1_in_7'])
        time.sleep(0.3)
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(0.3)

        # pyautogui.keyDown('s')
        # time.sleep(18)
        # pyautogui.keyUp('s')
        # time.sleep(0.3)
        # pyautogui.keyDown('a')
        # time.sleep(1.5)
        # pyautogui.keyUp('a')
        # time.sleep(0.3)
        # pyautogui.keyDown('w')
        # time.sleep(1.5)
        # pyautogui.keyUp('w')
        # time.sleep(0.3)
        #
        # pyautogui.click(*POSITION['game']['skip_dialog'])
        # time.sleep(0.2)
        # pyautogui.press('f', presses=3, interval=0.2)

    @staticmethod
    def transmit_to_liyue_qingyunding():
        """
        传送至璃月-庆云顶-七天神像
        :return:
        """
        m = PyMouse()
        time.sleep(1)
        # 定位蒙德
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['tag_monde'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['tag_liyue'])
        time.sleep(0.5)

        # 偏移地图
        def _shift():
            time.sleep(0.5)
            m.move(*POSITION['windows']['left_top'])
            time.sleep(0.5)
            pyautogui.dragTo(*POSITION['windows']['right_bottom'], button='left', duration=0.4)
            time.sleep(0.5)

        _shift()
        _shift()

        position = locate('map/statue/liyue_qingyun_peak_1.png', once=False, threshold=0.85)
        time.sleep(0.3)
        # 选中传送点
        pyautogui.click(*position)
        time.sleep(0.3)
        # 指定传送点
        position = locate('map/item/statue.png', once=False)
        pyautogui.click(*position)
        time.sleep(0.3)
        # 确定传送
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(1)
        # 清心 * 2
        pyautogui.keyDown('d')
        time.sleep(0.75)
        pyautogui.keyUp('d')
        time.sleep(0.3)
        pyautogui.keyDown('s')
        time.sleep(1.5)
        pyautogui.keyUp('s')
        time.sleep(1)
        pyautogui.press('f')
        time.sleep(1)
        pyautogui.press('f')
        time.sleep(0.5)
        # 清心 * 1
        pyautogui.keyDown('a')
        time.sleep(1)
        pyautogui.keyUp('a')
        time.sleep(0.3)
        pyautogui.press('f')
        time.sleep(0.5)

    @staticmethod
    def transmit_to_liyue_qingyunding1():
        """
        传送至璃月-庆云顶-七天神像
        :return:
        """
        m = PyMouse()
        time.sleep(1)
        # 定位蒙德
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['tag_monde'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['switch_tag_button'])
        time.sleep(0.5)
        pyautogui.click(*POSITION['map']['tag_liyue'])
        time.sleep(0.5)

        # 偏移地图
        def _shift():
            m.move(*POSITION['windows']['left_top'])
            time.sleep(0.5)
            pyautogui.dragTo(*POSITION['windows']['right_bottom'], button='left', duration=0.3)
            time.sleep(0.5)

        _shift()
        _shift()

        position = locate('map/statue/liyue_qingyun_peak_1.png', once=False, threshold=0.85)
        time.sleep(0.3)
        # 选中传送点
        pyautogui.click(*position)
        time.sleep(0.3)
        # 指定传送点
        position = locate('map/item/statue.png', once=False)
        pyautogui.click(*position)
        time.sleep(0.3)
        # 确定传送
        pyautogui.click(*POSITION['map']['transmit_button'])
        time.sleep(0.3)
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)  # 确认是否进入游戏界面
        time.sleep(1)
