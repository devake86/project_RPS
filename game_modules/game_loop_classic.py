"""
project_RPS - game_loop_classic
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
    show_header_6,
    show_rock_loss, show_paper_loss, show_scissors_loss,
    show_rock_loss_final, show_paper_loss_final, show_scissors_loss_final,
)

from .game_constants import (
    ROCK, PAPER, SCISSORS,
    MINIMUM_POINTS,
    YES, NO,
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

# game loop function
def game_loop_classic():

    # variables
    input_player = 0
    input_player_int = 0
    input_computer = 0
    rounds = 0
    score_player = 0
    score_computer = 0

    # main loop
    while True:

        # if win condition show final rounds and score
        if score_player >= MINIMUM_POINTS and score_player - score_computer >= 2:
            print(f"     GAME MODE - CLASSIC")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Player won after {rounds} rounds with {score_player} to {score_computer} points.")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            break

        elif score_computer >= MINIMUM_POINTS and score_computer - score_player >= 2:
            print(f"     GAME MODE - CLASSIC")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Computer won after {rounds} rounds with {score_computer} to {score_player} points.")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            break

        # else show rounds and score
        else:
            print(f"     GAME MODE - CLASSIC")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Computer is waiting for your move.")
            print(f"     ")
            print(f"     ")
            print(f"     ")

        # player input ; if input correct end while-loop (break) and go to next line under while-loop
        while True:
            input_player = input(f"     [{ROCK}] ROCK [{PAPER}] PAPER [{SCISSORS}] SCISSORS: ").strip()
            # check if input is length of 1 and value is 1 or 2 or 3
            if len(input_player) == 1 and input_player in ("1", "2", "3"):
                break

            # after enter from input which creates new line
            # stdin = standard input
            # stdout = standard output
            # stderr = standard error output
            # sys.stdout.write("\033[F") = go up one line and ("\033[2K") to delete line
            # .flush() = show everything written in .write immediately
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()

        # if input_player = 1 or 2 or 3 change to int
        input_player_int = int(input_player)

        # clear screen before redraw new output
        # cls = clear screen command for Windows consoles
        # nt = Windows
        # clear = clear screen command for Linux/MacOS consoles
        os.system("cls" if os.name == "nt" else "clear")

        # computer random choice 1, 2 or 3
        input_computer = random.randint(1,3)

        # player choice vs computer choice with art output
        # player choices rock
        # rock draw
        if input_player_int == ROCK and input_computer == ROCK:
            show_rock_draw_animation()

        # rock win
        elif input_player_int == ROCK and input_computer == SCISSORS:
            score_player += 1
            if score_player >= MINIMUM_POINTS and score_player - score_computer >= 2:
                show_rock_win_final_animation()
            else:
                show_rock_win_animation()

        # rock loss
        elif input_player_int == ROCK and input_computer == PAPER:
            score_computer += 1
            if score_computer >= MINIMUM_POINTS and score_computer - score_player >= 2:
                show_rock_loss_final()
            else:
                show_rock_loss()

        # player choices paper
        # paper draw
        elif input_player_int == PAPER and input_computer == PAPER:
            show_paper_draw_animation()

        # paper win
        elif input_player_int == PAPER and input_computer == ROCK:
            score_player += 1
            if score_player >= MINIMUM_POINTS and score_player - score_computer >= 2:
                show_paper_win_final_animation()
            else:
                show_paper_win_animation()

        # paper loss
        elif input_player_int == PAPER and input_computer == SCISSORS:
            score_computer += 1
            if score_computer >= MINIMUM_POINTS and score_computer - score_player >= 2:
                show_paper_loss_final()
            else:
                show_paper_loss()

        # player choices scissors
        # scissors draw
        elif input_player_int == SCISSORS and input_computer == SCISSORS:
            show_scissors_draw_animation()

        # scissors win
        elif input_player_int == SCISSORS and input_computer == PAPER:
            score_player += 1
            if score_player >= MINIMUM_POINTS and score_player - score_computer >= 2:
                show_scissors_win_final_animation()
            else:
                show_scissors_win_animation()

        # scissors loss
        else:
            score_computer += 1
            if score_computer >= MINIMUM_POINTS and score_computer - score_player >= 2:
                show_scissors_loss_final()
            else:
                show_scissors_loss()

        # rounds count +1
        rounds += 1


    # variables
    input_new_game = 0
    input_new_game_int = 0

    # new game yes or no ; .strip() = delete spaces before or after input()
    # continue = go to beginning of while-loop
    # break = end while-loop-> go to next line -> no new lines -> starts main() while-loop again with show_header()
    # return = close whole function
    while True:
        input_new_game = input(f"     NEW GAME? [{YES}] YES [{NO}] QUIT TO MAIN MENU: ").strip()

        # check if input is length of not 1 or value is not 1 or 0
        if len(input_new_game) !=1 or input_new_game not in ("1","0"):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()
            continue

        input_new_game_int = int(input_new_game)

        # restart by closing function and restarting it with input_lernfeld_de or close back to main menu
        if input_new_game_int == 1:
            os.system("cls" if os.name == "nt" else "clear")
            show_header_6()
            return input_new_game_int
        else:
            return input_new_game_int









# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
