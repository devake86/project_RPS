"""
project_RPS - game_loop
"""

# --- CODE START ---

# import for all dependencies (functions and constants) needed in THIS file
# random for input_computer 1, 2 or 3
import random
# os for screen clear and redraw art after input_player_int
# os doesn't work in Thonny
# to use start game with game_start.bat!
import os
# used to delete input line if not correct before it is shown again (screen scroll prevention)
# with sys.stdout.write /.flush
# sys doesn't work in Thonny
# to use start game with game_start.bat!
import sys

from .game_art import (
    show_rock_draw, show_rock_win, show_rock_loss,
    show_paper_draw, show_paper_win, show_paper_loss,
    show_scissors_draw, show_scissors_win, show_scissors_loss,
    show_rock_win_final, show_paper_win_final, show_scissors_win_final,
    show_rock_loss_final, show_paper_loss_final, show_scissors_loss_final,
)

from .game_constants import (
    ROCK, PAPER, SCISSORS,
    WIN_CONDITION,
)

# game loop function
def game_loop():

    # variables
    input_player = 0
    input_player_int = 0
    input_computer = 0
    rounds = 0
    score_player = 0
    score_computer = 0

    # main loop
    while True:

        # show rounds and score
        if score_player >= WIN_CONDITION and score_player - score_computer >= 2 or score_computer >= WIN_CONDITION and score_computer - score_player >= 2:
            print(f"ROUND:    {rounds+1}")
            print(f"PLAYER:   {score_player}")
            print(f"COMPUTER: {score_computer}")
            print(f"\n\n")
            break
        else:
            print(f"ROUND:    {rounds+1}")
            print(f"PLAYER:   {score_player}")
            print(f"COMPUTER: {score_computer}")
            print(f"\n\n")

        # player input ; if input correct end while-loop (break) and go to next line under while-loop
        while True:
            input_player = input(f"[{ROCK}] ROCK [{PAPER}] PAPER [{SCISSORS}] SCISSORS: ").strip()
            # check if input is length of 1 and value is 1 or 2 or 3
            if len(input_player) == 1 and input_player in ("1", "2", "3"):
                break

            # after enter from input which creates new line
            # sys.stdout.write("\033[F") = go up one line and ("\033[2K") to delete line
            # .flush() = show everything written in .write immediately
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()

        # computer random choice
        input_computer = random.randint(1,3)

        input_player_int = int(input_player)

        # clear screen before redraw new output
        # cls = clear screen command for Windows consoles
        # nt = Windows
        # clear = clear screen command for Linux/MacOS consoles
        os.system("cls" if os.name == "nt" else "clear")

        # player choices rock
        # rock draw
        if input_player_int == ROCK and input_computer == ROCK:
            show_rock_draw()

        # rock win
        elif input_player_int == ROCK and input_computer == SCISSORS:
            score_player += 1
            if score_player >= WIN_CONDITION and score_player - score_computer >= 2:
                show_rock_win_final()
            else:
                show_rock_win()

        # rock loss
        elif input_player_int == ROCK and input_computer == PAPER:
            score_computer += 1
            if score_computer >= WIN_CONDITION and score_computer - score_player >= 2:
                show_rock_loss_final()
            else:
                show_rock_loss()

        # player choices paper
        # paper draw
        elif input_player_int == PAPER and input_computer == PAPER:
            show_paper_draw()

        # paper win
        elif input_player_int == PAPER and input_computer == ROCK:
            score_player += 1
            if score_player >= WIN_CONDITION and score_player - score_computer >= 2:
                show_paper_win_final()
            else:
                show_paper_win()

        # paper loss
        elif input_player_int == PAPER and input_computer == SCISSORS:
            score_computer += 1
            if score_computer >= WIN_CONDITION and score_computer - score_player >= 2:
                show_paper_loss_final()
            else:
                show_paper_loss()

        # player choices scissors
        # scissors draw
        elif input_player_int == SCISSORS and input_computer == SCISSORS:
            show_scissors_draw()

        # scissors win
        elif input_player_int == SCISSORS and input_computer == PAPER:
            score_player += 1
            if score_player >= WIN_CONDITION and score_player - score_computer >= 2:
                show_scissors_win_final()
            else:
                show_scissors_win()

        # scissors loss
        else:
            score_computer += 1
            if score_computer >= WIN_CONDITION and score_computer - score_player >= 2:
                show_scissors_loss_final()
            else:
                show_scissors_loss()

        # rounds count +1
        rounds += 1

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
