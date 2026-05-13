"""
project_RPS - __init__
"""

# __init__ = collection of functions and constants
# to be used in game_main.py with "from game_modules import *"
# public API

# --- CODE START ---

# multiline import with "()" ; if ")" in new line end last function/constant with ","
from .game_art import (
    show_header,
    show_rock_draw, show_rock_win, show_rock_loss,
    show_paper_draw, show_paper_win, show_paper_loss,
    show_scissors_draw, show_scissors_win, show_scissors_loss,
    show_rock_win_final, show_paper_win_final, show_scissors_win_final,
    show_rock_loss_final, show_paper_loss_final, show_scissors_loss_final,
)

from .game_loop import game_loop

from .game_constants import (
    ROCK, PAPER, SCISSORS,
    WIN_CONDITION,
    YES, NO,
)

# list __all__ = [exported, functions, and, constants]
__all__ = [
    "show_header",
    "show_rock_draw", "show_rock_win", "show_rock_loss",
    "show_paper_draw", "show_paper_win", "show_paper_loss",
    "show_scissors_draw", "show_scissors_win", "show_scissors_loss",
    "show_rock_win_final", "show_paper_win_final", "show_scissors_win_final",
    "show_rock_loss_final", "show_paper_loss_final", "show_scissors_loss_final",
    "game_loop",
    "ROCK", "PAPER", "SCISSORS",
    "WIN_CONDITION",
    "YES", "NO",
]

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
