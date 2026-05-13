@echo off
cd /d "%~dp0"
start "" /max cmd /c "py game_animations.py & echo. & pause"


