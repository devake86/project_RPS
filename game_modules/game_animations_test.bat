REM = remark

REM disables commands, for example "py game_main.py" will not show in window
@echo off

REM changes the path to were the batch-file is in; drive (d) + path (p) der batch-file (0)
cd /d "%~dp0"

REM starts python-script with python-launcher
py game_animations.py

REM leaves window open ; good for debugging
pause


