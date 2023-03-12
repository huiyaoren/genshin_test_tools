from concurrent.futures.thread import ThreadPoolExecutor

import pyautogui

from roles import Role
from scenes import *
from scenes.log import LogScene


def main():
    pyautogui.FAILSAFE = False
    # 启动
    SystemScene.into_loading_scene()
    LoadingScene.into_game_scene()
    GameScene.receive_blessing()
    # 派遣奖励
    GameScene.into_map_scene()
    MapScene.transmit_to_monde()
    GameScene.goto_association()
    GameScene.receive_discovery_prizes()
    # 清心
    GameScene.into_map_scene()
    MapScene.transmit_to_liyue_qingyunding()
    # 砍树
    GameScene.into_map_scene()
    MapScene.transmit_to_monde()
    GameScene.hit_tree_1()

    GameScene.into_map_scene()
    MapScene.transmit_to_monde_2()
    GameScene.hit_tree_2()

    GameScene.into_map_scene()
    MapScene.transmit_to_monde_mingguangxia()
    GameScene.load_complete()
    GameScene.hit_tree_3()
    #
    GameScene.load_complete()
    GameScene.into_map_scene()
    MapScene.transmit_to_liyue_qingyunding1()
    GameScene.hit_tree_4()
    # todo 狗粮
    # todo 采矿
    # GameScene.into(MapScene)
    # MapScene.transmit_to_monde_benlanglin()
    # todo 副本
    # todo 质变仪
    # todo 树脂合成
    # todo 邮件2
    # 尘歌壶奖励
    GameScene.into_map_scene()
    MapScene.transmit_to_monde()
    GameScene.load_complete()
    GameScene.into_pot_scene()
    GameScene.load_complete()
    PotScene.receive_pot_prizes()
    # 邮件
    GameScene.load_complete()
    GameScene.into_setting_scene()
    SettingScene.receive_mail()
    SettingScene.into_game_scene()
    # 纪行
    GameScene.load_complete()
    GameScene.into_log_scene()
    LogScene.receive_quest_prizes()
    LogScene.receive_log_prizes()
    LogScene.into_game_scene()
    GameScene.load_complete()
    # 关闭
    # PotScene.into_setting_scene()
    # SettingScene.into_loading_scene()
    # LoadingScene.into_system_scene()
    # SystemScene.game_close()
    while 1:
        with ThreadPoolExecutor(max_workers=8) as executor:
            executor.submit(Role.auto_health)
            executor.submit(Role.auto_catch)
            executor.submit(Role.skill_e)


if __name__ == '__main__':
    main()
