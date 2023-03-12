import time

import pyautogui
from pykeyboard import PyKeyboard
from pymouse import PyMouse

from positions import POSITION
from roles import Role
from scenes.common import CommonScene
from tools import loading, locate


# 场景3：游戏界面
class GameScene(CommonScene):
    @staticmethod
    def goto_association():
        """
        步行至冒险家协会
        :return:
        """
        k = PyKeyboard()
        time.sleep(1)
        k.press_key('w')
        time.sleep(10)
        k.press_key('a')
        time.sleep(0.5)
        k.release_key('a')
        while 1:
            if locate('game_catch_1_item.jpg'):
                k.release_key('w')
                break
        time.sleep(0.5)

    @staticmethod
    def receive_daily_prizes():
        pass

    @staticmethod
    def receive_discovery_prizes():
        k = PyKeyboard()
        m = PyMouse()

        time.sleep(1)
        k.press_key('f')
        time.sleep(1)
        m.click(*POSITION['game']['skip_dialog'])
        time.sleep(1.5)
        m.move(*POSITION['game']['discovery_prizes_button'])
        time.sleep(0.3)
        m.click(*POSITION['game']['discovery_prizes_button'])
        time.sleep(3)

        # 进入探索派遣界面
        def _tag(name):
            m.move(*POSITION['discovery'][name])
            time.sleep(0.3)
            m.click(*POSITION['discovery'][name])
            time.sleep(0.3)

        def _receive(place='place_monde_2', role='role_2'):
            m.move(*POSITION['discovery'][place])
            time.sleep(0.3)
            m.click(*POSITION['discovery'][place])
            time.sleep(0.3)
            # 判断是否完成探索 未完成则跳过流程
            if not locate('discovery_recall_button.png'):
                m.move(*POSITION['discovery']['confirm'])
                time.sleep(0.3)
                m.click(*POSITION['discovery']['confirm'])  # 领取奖励
                time.sleep(0.3)
                m.click(*POSITION['discovery']['confirm'])  # 确认奖励
                time.sleep(0.3)
                m.click(*POSITION['discovery']['confirm'])  # 选择角色
                time.sleep(0.3)
                m.move(*POSITION['discovery'][role])
                time.sleep(0.3)
                m.click(*POSITION['discovery'][role])  # 选择角色1
                time.sleep(0.3)

        _tag('tag_monde')
        _receive('place_monde_1', 'role_1')  # 蒙德1
        _receive('place_monde_2', 'role_2')  # 蒙德2

        _tag('tag_liyue')
        _receive('place_liyue_1', 'role_3')  # 璃月1 角色3-申鹤
        _receive('place_liyue_2', 'role_1')  # 璃月2

        _tag('tag_inazuma')
        _receive('place_inazuma_1', 'role_1')  # 稻妻1

        k.tap_key(k.escape_key)
        time.sleep(1)

    @classmethod
    def into_pot_scene(cls):
        """
        进入尘歌壶
        :return:
        """
        k = PyKeyboard()
        m = PyMouse()
        time.sleep(1)
        k.press_key(k.alt_l_key)
        time.sleep(1)
        m.move(*POSITION['game']['backpack_button'])
        time.sleep(0.3)
        m.click(*POSITION['game']['backpack_button'])
        time.sleep(0.5)
        k.release_key(k.alt_l_key)
        time.sleep(1)
        m.move(*POSITION['backpack']['category_6'])
        time.sleep(0.3)
        m.click(*POSITION['backpack']['category_6'])
        time.sleep(0.3)
        m.click(*POSITION['backpack']['item_1'])
        time.sleep(0.3)
        m.click(*POSITION['backpack']['confirm'])
        time.sleep(1)
        while 1:
            if locate('game_catch_1_item.jpg'):
                break
        k.tap_key('f')
        time.sleep(8)

    @classmethod
    def into_log_scene(cls):
        """
        进入纪行界面
        :return:
        """
        k = PyKeyboard()
        k.press_key(k.alt_l_key)
        time.sleep(0.5)
        # todo 会出现纪行期限结束 没有纪行图标存在的情况
        pyautogui.click(*locate('game_log_button.png', once=False, threshold=0.8))
        time.sleep(0.1)
        k.release_key(k.alt_l_key)
        time.sleep(0.5)

    @staticmethod
    def receive_blessing():
        is_received = False

        time.sleep(1)
        while 1:
            if loading(POSITION['game']['role_button'], 'game_role_button', once=True, threshold=0.8):
                is_received = True
                break
            if loading(POSITION['game']['receive_blessing_button'], 'game_receive_blessing_button', once=True, threshold=0.8):
                break

        if not is_received:  # 已领取空月祝福的场合直接跳过领取流程
            time.sleep(1)
            pyautogui.click(*POSITION['game']['receive_blessing_button'][0:2])
            time.sleep(0.3)
            loading(POSITION['game']['receive_blessing_confirm'], 'game_receive_blessing_confirm', threshold=0.8)
            time.sleep(1)
            pyautogui.click(*POSITION['game']['receive_blessing_confirm'][0:2])
            time.sleep(2.5)

        GameScene.switch_role(1)
        time.sleep(0.5)

    @staticmethod
    def switch_role(number=1):
        # todo 诺埃尔图标
        time.sleep(1)
        pyautogui.press(str(number))
        time.sleep(0.5)

    @classmethod
    def hit_tree_1(cls):
        """
        蒙德城砍树
        :return:
        """
        with pyautogui.hold('s'):
            time.sleep(3)
        with pyautogui.hold('d'):
            time.sleep(2)
        Role.hit_3()
        time.sleep(0.5)
        with pyautogui.hold('a'):
            time.sleep(0.5)
        time.sleep(0.5)
        with pyautogui.hold('w'):
            time.sleep(0.5)
        time.sleep(0.5)
        Role.hit_3()
        time.sleep(0.5)
        with pyautogui.hold('s'):
            time.sleep(0.15)
        time.sleep(0.5)
        Role.hit_3()
        time.sleep(2)

    @classmethod
    def hit_tree_2(cls):
        """
        蒙德城外砍树
        :return:
        """
        with pyautogui.hold('a'):
            with pyautogui.hold('w'):
                time.sleep(4)
        with pyautogui.hold('w'):
            time.sleep(1)
        Role.hit_3()
        time.sleep(0.5)
        with pyautogui.hold('d'):
            with pyautogui.hold('s'):
                time.sleep(1)
        Role.hit_3()
        time.sleep(2)

    @classmethod
    def hit_tree_3(cls):
        """
        蒙德城外砍树
        :return:
        """
        Role.go_back(3.5)
        Role.hit_3()
        time.sleep(0.5)
        pyautogui.press('e')
        Role.go_back(0.1, left=True)
        Role.hit_3()
        Role.go_right(1)
        time.sleep(0.5)
        Role.go_front(0.1, right=True)
        Role.hit_3()
        Role.go_front(1.5, right=True)
        Role.go_front(0.1)
        Role.hit_3()
        time.sleep(0.5)
        Role.go_front(1.5, left=True)
        Role.go_front(0.1)
        Role.hit_3()
        time.sleep(1)

    @classmethod
    def hit_tree_4(cls):
        """
        庆云顶砍树
        :return:
        """
        Role.go_back(2.5, right=True)
        Role.hit_1()
        time.sleep(4)
        Role.go_left(0.5)
        with pyautogui.hold('d'):
            Role.hit_4()
        Role.go_left(2)
        with pyautogui.hold('w'):
            Role.hit_4()


    @classmethod
    def load_complete(cls):
        loading(POSITION['game']['role_button'], 'game_role_button', threshold=0.7)
        time.sleep(0.3)
