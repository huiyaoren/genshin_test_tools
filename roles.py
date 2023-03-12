import time

import pyautogui
from PIL import ImageGrab

from positions import POSITION
from tools import loading, locate


class Role:

    @classmethod
    def current_role_health(cls):
        img = ImageGrab.grab(bbox=POSITION['game']['health_current'])
        img_pixels = list(img.convert("L").getdata())
        img_avg = 50
        health = 1 - (len([i for i in img_pixels if i < img_avg]) / len(img_pixels))
        return health

    @staticmethod
    def auto_catch(once=None):
        """
        自动拾取
        :param once:
        :return:
        """

        while 1:
            # if loading(POSITION['game']['catch_1_itemf'], 'game_catch_1_item', once=True):
            if locate('game_catch_1_item.jpg', box=(1200, 300, 2200, 800)):
                time.sleep(0.01)
                t = time.time()
                if locate('game_talk.png', box=(1200, 300, 2200, 800)):  # 区分拾取物品和人物交互 todo 性能优化 只选取指定区域识别
                    continue
                else:
                    pyautogui.press('f', presses=8, interval=0.1)

            # t = time.time()
            # if loading(POSITION['game']['catch_2_item'], 'game_catch_2_item', once=True):
            #     time.sleep(0.01)
            #     if locate('game_talk.png'):  # 区分拾取物品和人物交互
            #         continue
            #     else:
            #         pyautogui.press('f', presses=4, interval=0.1)
            # print('2', time.time() - t)

            if once:
                return

    @classmethod
    def auto_health(cls, once=None):
        """
        自动回血
        :param once:
        :return:
        """
        while 1:
            health = cls.current_role_health()
            if health == 0 or health == 1:
                pass
            else:
                if health <= 0.4:
                    time.sleep(0.15)
                    if loading(POSITION['game']['role_button'], 'game_role_button', once=True, threshold=0.7):
                        print('health: {} %'.format(round(health * 100, 2)))
                        pyautogui.press('z')
                        time.sleep(0.2)
            if once:
                return health


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
    def hit_4(cls):
        pyautogui.click(clicks=4, interval=0.6)
        time.sleep(0.1)
        pyautogui.click(button='right')

    @classmethod
    def hit_1(cls):
        pyautogui.click()

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
    def skill_e(cls, once=False, force=False):
        if force:
            pyautogui.press('e')
            return
        while 1:
            match = loading(POSITION['game']['skill_e'], 'game_skill_e', once=once)
            if match:
                pyautogui.press('e')
                return match
            if once:
                return match

    @classmethod
    def go_front(cls, second, left=False, right=False):
        with pyautogui.hold('w'):
            if left:
                with pyautogui.hold('a'):
                    time.sleep(second)
            elif right:
                with pyautogui.hold('d'):
                    time.sleep(second)
            else:
                time.sleep(second)

    @classmethod
    def go_back(cls, second, left=False, right=False):
        with pyautogui.hold('s'):
            if left:
                with pyautogui.hold('a'):
                    time.sleep(second)
            elif right:
                with pyautogui.hold('d'):
                    time.sleep(second)
            else:
                time.sleep(second)

    @classmethod
    def go_right(cls, second):
        with pyautogui.hold('d'):
            time.sleep(second)

    @classmethod
    def go_left(cls, second):
        with pyautogui.hold('a'):
            time.sleep(second)
