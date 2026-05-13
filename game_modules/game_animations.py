"""
project_RPS - game_animations
"""

# --- CODE START ---

import os
import time

from .game_art import (
    show_header_1, show_header_2, show_header_3, show_header_4, show_header_5, show_header_6,
    show_rock_draw_1, show_rock_draw_2, show_rock_draw_3, show_rock_draw_4, show_rock_draw_5,
    show_rock_draw_6, show_rock_draw_7, show_rock_draw_8, show_rock_draw_9, show_rock_draw_10,
    show_rock_draw_11, show_rock_draw_12, show_rock_draw_13, show_rock_draw_14,
    show_rock_win_1, show_rock_win_2, show_rock_win_3, show_rock_win_4, show_rock_win_5,
    show_rock_win_6, show_rock_win_7, show_rock_win_8, show_rock_win_9, show_rock_win_10,
    show_rock_win_11, show_rock_win_12, show_rock_win_13, show_rock_win_14, show_rock_win_15,
    show_rock_win_16, show_rock_win_17, show_rock_win_18, show_rock_win_19, show_rock_win_20,
    show_rock_win_21, show_rock_win_22, show_rock_win_23, show_rock_win_24, show_rock_win_25,
    show_rock_win_26, show_rock_win_27, show_rock_win_28, show_rock_win_final_1, show_rock_win_final_2,
    show_paper_draw_1, show_paper_draw_2, show_paper_draw_3, show_paper_draw_4, show_paper_draw_5,
    show_paper_draw_6, show_paper_draw_7, show_paper_draw_8, show_paper_draw_9,
    show_paper_win_1, show_paper_win_2, show_paper_win_3, show_paper_win_4, show_paper_win_5,
    show_paper_win_6, show_paper_win_7, show_paper_win_8, show_paper_win_9, show_paper_win_10,
    show_paper_win_11, show_paper_win_12, show_paper_win_13, show_paper_win_14, show_paper_win_15,
    show_paper_win_16, show_paper_win_17, show_paper_win_18, show_paper_win_19, show_paper_win_20,
    show_paper_win_21, show_paper_win_22, show_paper_win_23, show_paper_win_24, show_paper_win_25,
    show_paper_win_26, show_paper_win_27, show_paper_win_28, show_paper_win_29, show_paper_win_30,
    show_paper_win_31, show_paper_win_32, show_paper_win_33, show_paper_win_34, show_paper_win_35,
    show_paper_win_36, show_paper_win_final_1, show_paper_win_final_2,
    show_scissors_draw_1, show_scissors_draw_2, show_scissors_draw_3, show_scissors_draw_4, show_scissors_draw_5,
    show_scissors_draw_6, show_scissors_draw_7, show_scissors_draw_8, show_scissors_draw_9,
    show_scissors_win_1, show_scissors_win_2, show_scissors_win_3, show_scissors_win_4, show_scissors_win_5,
    show_scissors_win_6, show_scissors_win_7, show_scissors_win_8, show_scissors_win_9, show_scissors_win_10,
    show_scissors_win_11, show_scissors_win_12, show_scissors_win_13, show_scissors_win_14, show_scissors_win_15,
    show_scissors_win_16, show_scissors_win_17, show_scissors_win_18,
    show_scissors_win_19, show_scissors_win_19a, show_scissors_win_19b,
    show_scissors_win_20, show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i,
    show_scissors_win_20j, show_scissors_win_20k, show_scissors_win_20l,
    show_scissors_win_21, show_scissors_win_22, show_scissors_win_23, show_scissors_win_24,
    show_scissors_win_final_1, show_scissors_win_final_2,
)

# animations
# header
def show_header_animation():

    frames = [
        show_header_1, show_header_2, show_header_3, show_header_4, show_header_5,
        show_header_6,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# rock draw
def show_rock_draw_animation():

    frames = [
        show_rock_draw_1, show_rock_draw_2, show_rock_draw_3, show_rock_draw_4, show_rock_draw_5,
        show_rock_draw_6, show_rock_draw_7, show_rock_draw_8, show_rock_draw_9, show_rock_draw_10,
        show_rock_draw_11, show_rock_draw_12, show_rock_draw_11, show_rock_draw_12, show_rock_draw_11,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    frames = [
        show_rock_draw_13, show_rock_draw_14,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# rock win
def show_rock_win_animation():

    # movement fast
    frames = [
        show_rock_win_1, show_rock_win_2, show_rock_win_3, show_rock_win_4, show_rock_win_5,
        show_rock_win_6, show_rock_win_7, show_rock_win_8, show_rock_win_9, show_rock_win_10,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # impact slowdown
    frames = [
        show_rock_win_11, show_rock_win_12, show_rock_win_13, show_rock_win_14, show_rock_win_15,
        show_rock_win_16, show_rock_win_17, show_rock_win_18, show_rock_win_19, show_rock_win_20,
        show_rock_win_21, show_rock_win_22,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # crushed + backing up slowly
    frames = [
        show_rock_win_23, show_rock_win_24, show_rock_win_25,
        show_rock_win_26,
    ]

    fps = 5
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_rock_win_27, show_rock_win_28,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# rock win final
def show_rock_win_final_animation():

    # movement fast
    frames = [
        show_rock_win_1, show_rock_win_2, show_rock_win_3, show_rock_win_4, show_rock_win_5,
        show_rock_win_6, show_rock_win_7, show_rock_win_8, show_rock_win_9, show_rock_win_10,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # impact slowdown
    frames = [
        show_rock_win_11, show_rock_win_12, show_rock_win_13, show_rock_win_14, show_rock_win_15,
        show_rock_win_16, show_rock_win_17, show_rock_win_18, show_rock_win_19, show_rock_win_20,
        show_rock_win_21, show_rock_win_22,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # crushed + backing up slowly
    frames = [
        show_rock_win_23, show_rock_win_24, show_rock_win_25,
        show_rock_win_26,
    ]

    fps = 5
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_rock_win_27, show_rock_win_28,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_rock_win_final_1, show_rock_win_final_2, show_rock_win_final_1, show_rock_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# rock loss placeholder ; stillframe for now

# paper draw
def show_paper_draw_animation():

    frames = [
        show_paper_draw_1, show_paper_draw_2, show_paper_draw_3, show_paper_draw_4, show_paper_draw_5,
        show_paper_draw_6, show_paper_draw_7, show_paper_draw_6, show_paper_draw_7, show_paper_draw_6,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    frames = [
        show_paper_draw_8, show_paper_draw_9,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# paper win
def show_paper_win_animation():

    # movement + covering
    frames = [
        show_paper_win_1, show_paper_win_2, show_paper_win_3, show_paper_win_4, show_paper_win_5,
        show_paper_win_6, show_paper_win_7, show_paper_win_8, show_paper_win_9, show_paper_win_10,
        show_paper_win_11, show_paper_win_12, show_paper_win_13, show_paper_win_14, show_paper_win_15,
        show_paper_win_16, show_paper_win_17, show_paper_win_18, show_paper_win_19, show_paper_win_20,
        show_paper_win_21, show_paper_win_22, show_paper_win_23, show_paper_win_24, show_paper_win_25,
        show_paper_win_26, show_paper_win_27,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # make a fist
    frames = [
        show_paper_win_28, show_paper_win_29, show_paper_win_30, show_paper_win_31,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # backing up slowly
    frames = [
        show_paper_win_32, show_paper_win_33, show_paper_win_34,
    ]

    fps = 5
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_paper_win_35, show_paper_win_36,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# paper win final
def show_paper_win_final_animation():

    # movement + covering
    frames = [
        show_paper_win_1, show_paper_win_2, show_paper_win_3, show_paper_win_4, show_paper_win_5,
        show_paper_win_6, show_paper_win_7, show_paper_win_8, show_paper_win_9, show_paper_win_10,
        show_paper_win_11, show_paper_win_12, show_paper_win_13, show_paper_win_14, show_paper_win_15,
        show_paper_win_16, show_paper_win_17, show_paper_win_18, show_paper_win_19, show_paper_win_20,
        show_paper_win_21, show_paper_win_22, show_paper_win_23, show_paper_win_24, show_paper_win_25,
        show_paper_win_26, show_paper_win_27,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # make a fist
    frames = [
        show_paper_win_28, show_paper_win_29, show_paper_win_30, show_paper_win_31,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # backing up slowly
    frames = [
        show_paper_win_32, show_paper_win_33, show_paper_win_34,
    ]

    fps = 5
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_paper_win_35, show_paper_win_36,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_paper_win_final_1, show_paper_win_final_2, show_paper_win_final_1, show_paper_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# paper loss placeholder ; stillframe for now

# scissors draw
def show_scissors_draw_animation():

    frames = [
        show_scissors_draw_1, show_scissors_draw_2, show_scissors_draw_3, show_scissors_draw_4, show_scissors_draw_5,
        show_scissors_draw_6, show_scissors_draw_7, show_scissors_draw_6, show_scissors_draw_7, show_scissors_draw_6,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    frames = [
        show_scissors_draw_8, show_scissors_draw_9,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# scissors win
def show_scissors_win_animation():

    # 1 step slow
    frames = [
        show_scissors_win_1, show_scissors_win_2,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime dash fast
    frames = [
        show_scissors_win_3, show_scissors_win_4, show_scissors_win_5, show_scissors_win_6, show_scissors_win_7,
        show_scissors_win_8,
    ]

    fps = 60
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash pre attack fast
    frames = [
        show_scissors_win_9, show_scissors_win_10, show_scissors_win_9, show_scissors_win_10,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash attack fast
    frames = [
        show_scissors_win_11, show_scissors_win_12, show_scissors_win_11, show_scissors_win_13,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash post attack fast
    frames = [
        show_scissors_win_14, show_scissors_win_15, show_scissors_win_14, show_scissors_win_15,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # reappear + 3 steps slow
    frames = [
        show_scissors_win_16, show_scissors_win_17, show_scissors_win_18, show_scissors_win_19,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # cut fast
    frames = [
    show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20,
    show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i, show_scissors_win_20j,
    show_scissors_win_20k, show_scissors_win_20l,
    ]

    fps = 120
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # cut + cut through + score slow
    frames = [
        show_scissors_win_19, show_scissors_win_21, show_scissors_win_22, show_scissors_win_23, show_scissors_win_24,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# scissors win final
def show_scissors_win_final_animation():

    # 1 step slow
    frames = [
        show_scissors_win_1, show_scissors_win_2,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime dash fast
    frames = [
        show_scissors_win_3, show_scissors_win_4, show_scissors_win_5, show_scissors_win_6, show_scissors_win_7,
        show_scissors_win_8,
    ]

    fps = 60
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash pre attack fast
    frames = [
        show_scissors_win_9, show_scissors_win_10, show_scissors_win_9, show_scissors_win_10,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash attack fast
    frames = [
        show_scissors_win_11, show_scissors_win_12, show_scissors_win_11, show_scissors_win_13,
    ]

    fps = 10
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # anime clash post attack fast
    frames = [
        show_scissors_win_14, show_scissors_win_15, show_scissors_win_14, show_scissors_win_15,
    ]

    fps = 20
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # reappear + 3 steps slow
    frames = [
        show_scissors_win_16, show_scissors_win_17, show_scissors_win_18, show_scissors_win_19,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # cut fast
    frames = [
    show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20,
    show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i, show_scissors_win_20j,
    show_scissors_win_20k, show_scissors_win_20l,
    ]

    fps = 120
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # cut + cut through + score slow
    frames = [
        show_scissors_win_19, show_scissors_win_21, show_scissors_win_22, show_scissors_win_23, show_scissors_win_24,
    ]

    fps = 1
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_scissors_win_final_1, show_scissors_win_final_2, show_scissors_win_final_1, show_scissors_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")
        frame()
        time.sleep(delay)

# scissors loss placeholder ; still frame for now

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":

    # to test animations with game_animations_test.bat remove the "." at the top from "from .game_art" - > "from game_art"
    # add back the "." at the end of test for use in main programm game_start.bat
    show_scissors_win_final_animation()

# --- CODE END ---
