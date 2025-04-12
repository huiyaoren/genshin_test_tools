<!-- [Chinese Version](README.md) -->

# Genshin Impact Automation Tool

> ⚠️ **Project Status**: This project is no longer maintained as the author has quit Genshin Impact. 

This is an automation tool for Genshin Impact game that performs various daily tasks automatically using image recognition and GUI automation.

## Features

- **Daily Rewards Collection**
  - Auto receive daily blessing
  - Auto claim expedition rewards
  - Auto collect Serenitea Pot rewards
  - Auto process mail
  - Auto claim Battle Pass rewards

- **Resource Collection**
  - Auto chop trees (wood collection)
  - Auto pick up items
  - Auto mine ores (TODO)
  - Auto collect character ascension materials (TODO)

- **Character Management**
  - Auto heal when health is low
  - Auto use Elemental Skill (E)
  - Auto combat actions (attack combos)

- **Navigation**
  - Auto teleport to specific locations
  - Auto navigate between different game scenes

## Technical Implementation

- **Image Recognition**
  - Uses OpenCV for template matching
  - Custom image comparison algorithm (`is_match` function)
  - Screenshot analysis to detect UI elements

- **Automation**
  - PyAutoGUI for mouse/keyboard control
  - Multi-threading for concurrent tasks
  - State machine pattern for scene management

## File Structure

```
.
├── actions.py            # Action definitions
├── demo.py               # Main automation script
├── positions.py          # Screen coordinates definitions
├── requirements.txt      # Python dependencies
├── roles.py              # Character control functions
├── tools.py              # Core image processing utilities
├── locations/            # Reference images for UI elements
│   ├── game_*.jpg        # Game UI elements
│   ├── loading_*.jpg     # Loading screen elements
│   └── map/              # Map related elements
└── scenes/               # Scene handlers
    ├── battle.py         # Battle scene
    ├── game.py           # Main game scene
    ├── loading.py        # Loading scene
    ├── log.py            # Battle Pass scene
    ├── map.py            # Map scene
    ├── pot.py            # Serenitea Pot scene
    ├── setting.py        # Settings scene
    └── system.py         # System/launcher scene
```

## Dependencies

- Python 3.x
- OpenCV (`opencv-python`)
- PyAutoGUI
- Pillow (PIL)
- PyUserInput

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage

1. Configure game resolution to match the coordinates defined in `positions.py`
2. Place the game window in the expected position (coordinates are based on 2560x1440 resolution)
3. Run the main script:
```bash
python demo.py
```

## Configuration

- Edit `positions.py` to adjust coordinates for your screen resolution
- Add/update reference images in `locations/` folder as needed
- Modify thresholds in `tools.py` for image matching sensitivity

## Notes

- The tool is designed to run while the game is in windowed mode
- Failsafe is disabled (pyautogui.FAILSAFE = False) to prevent interruption
- Use with caution as automation may violate game's Terms of Service
