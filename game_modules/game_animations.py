"""
project_RPS - game_animations
"""

# --- CODE START ---

import os
import time
import sys

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
    show_scissors_win_6, show_scissors_win_7, show_scissors_win_8,
    show_scissors_win_9, show_scissors_win_9a,
    show_scissors_win_10, show_scissors_win_10a,
    show_scissors_win_11, show_scissors_win_12,
    show_scissors_win_12a, show_scissors_win_12b, show_scissors_win_12c, show_scissors_win_12d, show_scissors_win_12e,
    show_scissors_win_12f, show_scissors_win_12g, show_scissors_win_12h, show_scissors_win_12i, show_scissors_win_12j,
    show_scissors_win_12k, show_scissors_win_12l, show_scissors_win_12m,
    show_scissors_win_13,
    show_scissors_win_14, show_scissors_win_14a,
    show_scissors_win_15, show_scissors_win_15a,
    show_scissors_win_16, show_scissors_win_17, show_scissors_win_18,
    show_scissors_win_19, show_scissors_win_19a, show_scissors_win_19b, show_scissors_win_19c, show_scissors_win_19d,
    show_scissors_win_19e,
    show_scissors_win_20, show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i,
    show_scissors_win_20j, show_scissors_win_20k, show_scissors_win_20l,
    show_scissors_win_21, show_scissors_win_21a, show_scissors_win_21b,
    show_scissors_win_22, show_scissors_win_23, show_scissors_win_24,
    show_scissors_win_final_1, show_scissors_win_final_2,
)

from .game_sounds import (
    sound_sword_clashhit, sound_sword_slice, sound_whoosh_motion,
    sound_blood_splatter_explode, sound_body_rips_apart, sound_breeze_of_blood,
    sound_snow_step_1, sound_crushed_can, sound_paper_ball, sound_deep_sea_impact
)

# clear screen
def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def reset_cursor():
    sys.stdout.write("\033[H")
    sys.stdout.flush()

# animations
# header
def show_header_animation():

    frames = [
        show_header_1, show_header_2, show_header_3, show_header_4, show_header_5,
        show_header_6,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

# rock draw
def show_rock_draw_animation():

    frames = [
        show_rock_draw_1, show_rock_draw_2, show_rock_draw_3, show_rock_draw_4, show_rock_draw_5,
        show_rock_draw_6, show_rock_draw_7, show_rock_draw_8, show_rock_draw_9, show_rock_draw_10,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    frames = [
        show_rock_draw_11, show_rock_draw_12, show_rock_draw_11, show_rock_draw_12, show_rock_draw_11,
    ]

    fps = 10
    delay = 1.0 / fps

    sound_deep_sea_impact()

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    frames = [
        show_rock_draw_13, show_rock_draw_14,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

# rock win
def show_rock_win_animation():

    # movement fast
    frames = [
        show_rock_win_1, show_rock_win_2, show_rock_win_3, show_rock_win_4,
    ]

    fps = 20
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # movement + impact slowdown with sound
    frames = [
        show_rock_win_5, show_rock_win_6, show_rock_win_7, show_rock_win_8, show_rock_win_9, show_rock_win_10,
        show_rock_win_11, show_rock_win_12, show_rock_win_13, show_rock_win_14, show_rock_win_15,
        show_rock_win_16, show_rock_win_17, show_rock_win_18, show_rock_win_19, show_rock_win_20,
        show_rock_win_21, show_rock_win_22,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    sound_crushed_can()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # crushed + backing up slowly
    frames = [
        show_rock_win_23, show_rock_win_24, show_rock_win_25,
        show_rock_win_26,
    ]

    fps = 5
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_rock_win_27, show_rock_win_28,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

# rock win final
def show_rock_win_final_animation():

    # movement fast
    frames = [
        show_rock_win_1, show_rock_win_2, show_rock_win_3, show_rock_win_4,
    ]

    fps = 20
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # movement + impact slowdown with sound
    frames = [
        show_rock_win_5, show_rock_win_6, show_rock_win_7, show_rock_win_8, show_rock_win_9, show_rock_win_10,
        show_rock_win_11, show_rock_win_12, show_rock_win_13, show_rock_win_14, show_rock_win_15,
        show_rock_win_16, show_rock_win_17, show_rock_win_18, show_rock_win_19, show_rock_win_20,
        show_rock_win_21, show_rock_win_22,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    sound_crushed_can()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # crushed + backing up slowly
    frames = [
        show_rock_win_23, show_rock_win_24, show_rock_win_25,
        show_rock_win_26,
    ]

    fps = 5
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_rock_win_27, show_rock_win_28,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_rock_win_final_1, show_rock_win_final_2, show_rock_win_final_1, show_rock_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)


# paper draw
def show_paper_draw_animation():

    frames = [
        show_paper_draw_1, show_paper_draw_2, show_paper_draw_3, show_paper_draw_4, show_paper_draw_5,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    frames = [
        show_paper_draw_6, show_paper_draw_7, show_paper_draw_6, show_paper_draw_7, show_paper_draw_6,
    ]

    fps = 10
    delay = 1.0 / fps

    sound_deep_sea_impact()

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    frames = [
        show_paper_draw_8, show_paper_draw_9,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
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
        show_paper_win_21, show_paper_win_22, show_paper_win_23,
    ]

    fps = 20
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # make a fist with sound
    frames = [
        show_paper_win_24, show_paper_win_25,
        show_paper_win_26, show_paper_win_27, show_paper_win_28, show_paper_win_29, show_paper_win_30, show_paper_win_31,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    sound_paper_ball()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # backing up slowly
    frames = [
        show_paper_win_32, show_paper_win_33, show_paper_win_34,
    ]

    fps = 5
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_paper_win_35, show_paper_win_36,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
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
        show_paper_win_21, show_paper_win_22, show_paper_win_23,
    ]

    fps = 20
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # make a fist with sound
    frames = [
        show_paper_win_24, show_paper_win_25,
        show_paper_win_26, show_paper_win_27, show_paper_win_28, show_paper_win_29, show_paper_win_30, show_paper_win_31,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    sound_paper_ball()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # backing up slowly
    frames = [
        show_paper_win_32, show_paper_win_33, show_paper_win_34,
    ]

    fps = 5
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score
    frames = [
        show_paper_win_35, show_paper_win_36,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_paper_win_final_1, show_paper_win_final_2, show_paper_win_final_1, show_paper_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)


# scissors draw
def show_scissors_draw_animation():

    frames = [
        show_scissors_draw_1, show_scissors_draw_2, show_scissors_draw_3, show_scissors_draw_4, show_scissors_draw_5,
    ]

    fps = 10
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    frames = [
        show_scissors_draw_6, show_scissors_draw_7, show_scissors_draw_6, show_scissors_draw_7, show_scissors_draw_6,
    ]

    fps = 10
    delay = 1.0 / fps

    sound_deep_sea_impact()

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)


    frames = [
        show_scissors_draw_8, show_scissors_draw_9,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

# scissors win
def show_scissors_win_animation():

    # stillframe
    frames = [
        show_scissors_win_1,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # 3 step slow
    frames = [
        show_scissors_win_2, show_scissors_win_3, show_scissors_win_4,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        sound_snow_step_1()
        frame()
        time.sleep(delay)

    # anime teleport fast
    frames = [
         show_scissors_win_9a, show_scissors_win_10a, show_scissors_win_9a, show_scissors_win_10a,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_whoosh_motion()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blank
    frames = [
         show_scissors_win_11,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # anime clash attack fast
    # with sound effect
    frames = [
        show_scissors_win_12a, show_scissors_win_12b, show_scissors_win_12c, show_scissors_win_12d, show_scissors_win_12e,
        show_scissors_win_12f, show_scissors_win_12g, show_scissors_win_12h, show_scissors_win_12i, show_scissors_win_12j,
        show_scissors_win_12k, show_scissors_win_12l, show_scissors_win_12m,
    ]

    fps = 120
    delay = 1.0 / fps

    clear_screen()

    sound_sword_clashhit()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blank
    frames = [
         show_scissors_win_11,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # anime clash post attack fast
    frames = [
        show_scissors_win_14a, show_scissors_win_15a, show_scissors_win_14a, show_scissors_win_15a,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_whoosh_motion()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # reappear
    frames = [
        show_scissors_win_16,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # 3 steps slow
    frames = [
        show_scissors_win_17, show_scissors_win_18, show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        sound_snow_step_1()
        frame()
        time.sleep(delay)

    # no special attack stillframe
    frames = [
        show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # cut fast
    # with sound
    frames = [
    show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20,
    show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i, show_scissors_win_20j,
    show_scissors_win_20k, show_scissors_win_20l,
    ]

    fps = 120
    delay = 1.0 / fps

    clear_screen()

    sound_sword_slice()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # pre cut
    frames = [
        show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # cut
    frames = [
        show_scissors_win_21,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    sound_blood_splatter_explode()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blood splatter
    frames = [
        show_scissors_win_21a, show_scissors_win_21b, show_scissors_win_21a, show_scissors_win_21b,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_breeze_of_blood()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # rip
    frames = [
        show_scissors_win_22,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    sound_body_rips_apart()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score slow
    frames = [
        show_scissors_win_23, show_scissors_win_24,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

# scissors win final
def show_scissors_win_final_animation():

    # stillframe
    frames = [
        show_scissors_win_1,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # 3 step slow
    frames = [
        show_scissors_win_2, show_scissors_win_3, show_scissors_win_4,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        sound_snow_step_1()
        frame()
        time.sleep(delay)

    # anime teleport fast
    frames = [
         show_scissors_win_9a, show_scissors_win_10a, show_scissors_win_9a, show_scissors_win_10a,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_whoosh_motion()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blank
    frames = [
         show_scissors_win_11,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # anime clash attack fast
    # with sound effect
    frames = [
        show_scissors_win_12a, show_scissors_win_12b, show_scissors_win_12c, show_scissors_win_12d, show_scissors_win_12e,
        show_scissors_win_12f, show_scissors_win_12g, show_scissors_win_12h, show_scissors_win_12i, show_scissors_win_12j,
        show_scissors_win_12k, show_scissors_win_12l, show_scissors_win_12m,
    ]

    fps = 120
    delay = 1.0 / fps

    clear_screen()

    sound_sword_clashhit()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blank
    frames = [
         show_scissors_win_11,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # anime clash post attack fast
    frames = [
        show_scissors_win_14a, show_scissors_win_15a, show_scissors_win_14a, show_scissors_win_15a,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_whoosh_motion()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # reappear
    frames = [
        show_scissors_win_16,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # 3 steps slow
    frames = [
        show_scissors_win_17, show_scissors_win_18, show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        sound_snow_step_1()
        frame()
        time.sleep(delay)

    # no special attack stillframe
    frames = [
        show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)


    # cut fast
    # with sound
    frames = [
    show_scissors_win_20a, show_scissors_win_20b, show_scissors_win_20c, show_scissors_win_20d,
    show_scissors_win_20e, show_scissors_win_20f, show_scissors_win_20,
    show_scissors_win_20g, show_scissors_win_20h, show_scissors_win_20i, show_scissors_win_20j,
    show_scissors_win_20k, show_scissors_win_20l,
    ]

    fps = 120
    delay = 1.0 / fps

    clear_screen()

    sound_sword_slice()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # pre cut
    frames = [
        show_scissors_win_19,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # cut
    frames = [
        show_scissors_win_21,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    sound_blood_splatter_explode()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # blood splatter
    frames = [
        show_scissors_win_21a, show_scissors_win_21b, show_scissors_win_21a, show_scissors_win_21b,
    ]

    fps = 4
    delay = 1.0 / fps

    clear_screen()

    sound_breeze_of_blood()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # rip
    frames = [
        show_scissors_win_22,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    sound_body_rips_apart()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # score slow
    frames = [
        show_scissors_win_23, show_scissors_win_24,
    ]

    fps = 1
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)

    # final score
    frames = [
        show_scissors_win_final_1, show_scissors_win_final_2, show_scissors_win_final_1, show_scissors_win_final_2,
    ]

    fps = 2
    delay = 1.0 / fps

    clear_screen()

    for frame in frames:
        reset_cursor()
        frame()
        time.sleep(delay)


# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":

    # to test animations with game_animations_test.bat remove the "." at the top from "from .game_art" - > "from game_art"
    # do the same for game_sounds
    # add back the "." at the end of test for use in main programm game_start.bat
    # do the same for the filepath in game_sounds and add/delete "../"
    show_scissors_win_animation()

# --- CODE END ---
