"""
project_RPS - game_loop
"""

# --- CODE START ---

# import for all dependencies (functions and constants) needed in THIS file
import random

from .game_art import (
    show_header,
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
    input_computer = 0
    rounds = 0
    score_player = 0
    score_computer = 0

    # main loop
    while True:

        # show rounds and score
        if score_player == WIN_CONDITION or score_computer == WIN_CONDITION:
            print(f"ROUND:    {rounds+1}")
            print(f"PLAYER:   {score_player}")
            print(f"COMPUTER: {score_computer}")
            break
        else:
            print(f"ROUND:    {rounds+1}")
            print(f"PLAYER:   {score_player}")
            print(f"COMPUTER: {score_computer}")

        # player input
        input_player = int(input(f"\n\n[{ROCK}] ROCK [{PAPER}] PAPER [{SCISSORS}] SCISSORS: "))

        # computer random choice
        input_computer = random.randint(1,3)

        # player choices rock
        # rock draw
        if input_player == ROCK and input_computer == ROCK:
            show_rock_draw()

        # rock win
        elif input_player == ROCK and input_computer == SCISSORS:
            score_player += 1
            if score_player == WIN_CONDITION:
                show_rock_win_final()
            else:
                show_rock_win()

        # rock loss
        elif input_player == ROCK and input_computer == PAPER:
            score_computer += 1
            if score_computer == WIN_CONDITION:
                show_rock_loss_final()
            else:
                show_rock_loss()

        # player choices paper
        # paper draw
        elif input_player == PAPER and input_computer == PAPER:
            show_paper_draw()

        # paper win
        elif input_player == PAPER and input_computer == ROCK:
            score_player += 1
            if score_player == WIN_CONDITION:
                show_paper_win_final()
            else:
                show_paper_win()

        # paper loss
        elif input_player == PAPER and input_computer == SCISSORS:
            score_computer += 1
            if score_computer == WIN_CONDITION:
                show_paper_loss_final()
            else:
                show_paper_loss()

        # player choices scissors
        # scissors draw
        elif input_player == SCISSORS and input_computer == SCISSORS:
            show_scissors_draw()

        # scissors win
        elif input_player == SCISSORS and input_computer == PAPER:
            score_player += 1
            if score_player == WIN_CONDITION:
                show_scissors_win_final()
            else:
                show_scissors_win()

        # scissors loss
        else:
            score_computer += 1
            if score_computer == WIN_CONDITION:
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
