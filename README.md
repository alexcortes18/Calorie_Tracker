# Calorie Tracker

A PyQt6-based calorie tracking app for macOS.

## Features
- Log meals and calories
- Track daily totals

## Build Instructions
From project root:
1. Enable venv: source/calorie_tracker_env/bin/activate
2. Use the next code in bash to rebuild:
```bash:
(calorie_tracker_env) Alejandros-MacBook-Air:Calorie_Tracker alejandrocortes$ 
pyinstaller --onefile --windowed calorie_tracker_gui/calorie_tracker_pyqt6.py
```