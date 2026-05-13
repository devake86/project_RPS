"""
project_RPS - __init__
"""

# __init__ = collection of functions and constants
# to be used in game_main.py with "from game_modules import function_or_constant_name"
# public API

# --- CODE START ---

# multiline import with "()" ; end last function/constant with "," and to close ")" in new line = easy new imports
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
    show_rock_loss, show_rock_loss_final,
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
    show_paper_loss, show_paper_loss_final,
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
    show_scissors_loss, show_scissors_loss_final,
)

from .game_animations import (
    show_rock_draw_animation,
    show_rock_win_animation,
    show_rock_win_final_animation,
    show_paper_draw_animation,
    show_paper_win_animation,
    show_paper_win_final_animation,
    show_scissors_draw_animation,
    show_scissors_win_animation,
    show_scissors_win_final_animation,
)

from .game_constants import (
    ROCK, PAPER, SCISSORS,
    WIN_CONDITION,
    YES, NO,
)

from .game_menu import game_menu

from .game_loop import game_loop

from .game_new import game_new


# list __all__ = [exported, functions, and, constants]
__all__ = [
    "show_header_1", "show_header_2", "show_header_3", "show_header_4", "show_header_5", "show_header_6",
    "show_rock_draw_1", "show_rock_draw_2", "show_rock_draw_3", "show_rock_draw_4", "show_rock_draw_5",
    "show_rock_draw_6", "show_rock_draw_7", "show_rock_draw_8", "show_rock_draw_9", "show_rock_draw_10",
    "show_rock_draw_11", "show_rock_draw_12", "show_rock_draw_13", "show_rock_draw_14",
    "show_rock_win_1", "show_rock_win_2", "show_rock_win_3", "show_rock_win_4", "show_rock_win_5",
    "show_rock_win_6", "show_rock_win_7", "show_rock_win_8", "show_rock_win_9", "show_rock_win_10",
    "show_rock_win_11", "show_rock_win_12", "show_rock_win_13", "show_rock_win_14", "show_rock_win_15",
    "show_rock_win_16", "show_rock_win_17", "show_rock_win_18", "show_rock_win_19", "show_rock_win_20",
    "show_rock_win_21", "show_rock_win_22", "show_rock_win_23", "show_rock_win_24", "show_rock_win_25",
    "show_rock_win_26", "show_rock_win_27", "show_rock_win_28", "show_rock_win_final_1", "show_rock_win_final_2",
    "show_rock_loss", "show_rock_loss_final",
    "show_paper_draw_1", "show_paper_draw_2", "show_paper_draw_3", "show_paper_draw_4", "show_paper_draw_5",
    "show_paper_draw_6", "show_paper_draw_7", "show_paper_draw_8", "show_paper_draw_9",
    "show_paper_win_1", "show_paper_win_2", "show_paper_win_3", "show_paper_win_4", "show_paper_win_5",
    "show_paper_win_6", "show_paper_win_7", "show_paper_win_8", "show_paper_win_9", "show_paper_win_10",
    "show_paper_win_11", "show_paper_win_12", "show_paper_win_13", "show_paper_win_14", "show_paper_win_15",
    "show_paper_win_16", "show_paper_win_17", "show_paper_win_18", "show_paper_win_19", "show_paper_win_20",
    "show_paper_win_21", "show_paper_win_22", "show_paper_win_23", "show_paper_win_24", "show_paper_win_25",
    "show_paper_win_26", "show_paper_win_27", "show_paper_win_28", "show_paper_win_29", "show_paper_win_30",
    "show_paper_win_31", "show_paper_win_32", "show_paper_win_33", "show_paper_win_34", "show_paper_win_35",
    "show_paper_win_36", "show_paper_win_final_1", "show_paper_win_final_2",
    "show_paper_loss", "show_paper_loss_final",
    "show_scissors_draw_1", "show_scissors_draw_2", "show_scissors_draw_3", "show_scissors_draw_4", "show_scissors_draw_5",
    "show_scissors_draw_6", "show_scissors_draw_7", "show_scissors_draw_8", "show_scissors_draw_9",
    "show_scissors_win_1", "show_scissors_win_2", "show_scissors_win_3", "show_scissors_win_4", "show_scissors_win_5",
    "show_scissors_win_6", "show_scissors_win_7", "show_scissors_win_8", "show_scissors_win_9", "show_scissors_win_10",
    "show_scissors_win_11", "show_scissors_win_12", "show_scissors_win_13", "show_scissors_win_14", "show_scissors_win_15",
    "show_scissors_win_16", "show_scissors_win_17", "show_scissors_win_18",
    "show_scissors_win_19", "show_scissors_win_19a", "show_scissors_win_19b",
    "show_scissors_win_20", "show_scissors_win_20a", "show_scissors_win_20b", "show_scissors_win_20c", "show_scissors_win_20d",
    "show_scissors_win_20e", "show_scissors_win_20f", "show_scissors_win_20g", "show_scissors_win_20h", "show_scissors_win_20i",
    "show_scissors_win_20j", "show_scissors_win_20k", "show_scissors_win_20l",
    "show_scissors_win_21", "show_scissors_win_22", "show_scissors_win_23", "show_scissors_win_24",
    "show_scissors_win_final_1", "show_scissors_win_final_2",
    "show_scissors_loss", "show_scissors_loss_final",
    "show_rock_draw_animation",
    "show_rock_win_animation",
    "show_rock_win_final_animation",
    "show_paper_draw_animation",
    "show_paper_win_animation",
    "show_paper_win_final_animation",
    "show_scissors_draw_animation",
    "show_scissors_win_animation",
    "show_scissors_win_final_animation",
    "ROCK", "PAPER", "SCISSORS",
    "WIN_CONDITION",
    "YES", "NO",
    "game_menu",
    "game_loop",
    "game_new",
]

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
