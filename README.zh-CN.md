<!-- [English Version](README.md) -->

# 原神自动化工具

> ⚠️ **项目状态**: 本项目已不再维护，因为作者已退坑原神。

这是一个基于图像识别和GUI自动化的原神游戏自动化工具，可自动完成各种日常任务。

## 功能特性

- **每日奖励收集**
  - 自动领取每日祝福
  - 自动领取探索派遣奖励
  - 自动领取尘歌壶奖励
  - 自动处理邮件
  - 自动领取纪行奖励

- **资源收集**
  - 自动砍树(木材收集)
  - 自动拾取物品
  - 自动采矿(待实现)
  - 自动收集角色突破材料(待实现)

- **角色管理**
  - 血量低时自动治疗
  - 自动使用元素战技(E)
  - 自动战斗连招

- **地图导航**
  - 自动传送到指定地点
  - 自动在不同游戏场景间切换

## 技术实现

- **图像识别**
  - 使用OpenCV进行模板匹配
  - 自定义图像比较算法(`is_match`函数)
  - 截图分析检测UI元素

- **自动化控制**
  - 使用PyAutoGUI控制鼠标键盘
  - 多线程处理并发任务
  - 状态机模式管理不同场景

## 文件结构

```
.
├── actions.py            # 动作定义
├── demo.py               # 主自动化脚本
├── positions.py          # 屏幕坐标定义
├── requirements.txt      # Python依赖
├── roles.py              # 角色控制函数
├── tools.py              # 核心图像处理工具
├── locations/            # UI元素参考图片
│   ├── game_*.jpg        # 游戏UI元素
│   ├── loading_*.jpg     # 加载界面元素
│   └── map/              # 地图相关元素
└── scenes/               # 场景处理器
    ├── battle.py         # 战斗场景
    ├── game.py           # 主游戏场景
    ├── loading.py        # 加载场景
    ├── log.py            # 纪行场景
    ├── map.py            # 地图场景
    ├── pot.py            # 尘歌壶场景
    ├── setting.py        # 设置场景
    └── system.py         # 系统/启动器场景
```

## 依赖要求

- Python 3.x
- OpenCV (`opencv-python`)
- PyAutoGUI
- Pillow (PIL)
- PyUserInput

安装依赖:
```bash
pip install -r requirements.txt
```

## 使用说明

1. 配置游戏分辨率以匹配`positions.py`中定义的坐标
2. 将游戏窗口放置在预期位置(坐标基于2560x1440分辨率)
3. 运行主脚本:
```bash
python demo.py
```

## 配置说明

- 编辑`positions.py`调整适合您屏幕分辨率的坐标
- 在`locations/`文件夹中添加/更新参考图片
- 修改`tools.py`中的阈值调整图像匹配敏感度

## 注意事项

- 工具设计为在游戏窗口模式下运行
- 已禁用故障保护(pyautogui.FAILSAFE = False)防止中断
- 谨慎使用，自动化可能违反游戏服务条款
