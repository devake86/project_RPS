"""
project_RPS - game_loop_sneak_a_peek_quiz
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
    show_header_sneak_a_peek_question,
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

# import every single questions dictionary in questions_lfall_de before importing questions_lfall_de to prevent NameError
from .game_loop_quiz_dictionary import (
    questions_lf01_de, questions_lf02_de, questions_lf03_de, questions_lf04_de, questions_lf05_de,
    questions_lf06_de,
)

from .game_menu_sneak_a_peek_ingame import game_menu_sneak_a_peek_ingame

from .game_loop_sneak_a_peek_quiz_cache_clear import game_loop_sneak_a_peek_quiz_cache_clear_ingame

# game loop function
def game_loop_sneak_a_peek_quiz(input_lernfeld_de):

    # variables
    input_player = 0
    input_player_int = 0
    input_computer = 0
    rounds = 0
    score_player = 0
    score_computer = 0
    chance_sneak_a_peek = 0
    snuck_a_peek = 0
    input_question_answer = 0
    input_question_answer_int = 0

    # main loop
    while True:

        # if win condition player show final rounds and score then break loop
        if score_player >= MINIMUM_POINTS and score_player - score_computer >= 2:
            print(f"     GAME MODE - SNEAK-A-PEEK QUIZ")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Player wins!")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            break

        # elif win condition computer show final rounds and score then break loop
        elif score_computer >= MINIMUM_POINTS and score_computer - score_player >= 2:
            print(f"     GAME MODE - SNEAK-A-PEEK QUIZ")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Computer wins!")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            break

        # else show rounds and score if 0 rounds show how to elif snuck_a_peek 1 show snuck a peek else computer waiting
        else:
            print(f"     GAME MODE - SNEAK-A-PEEK QUIZ")
            print(f"     ")
            print(f"     ")
            print(f"     ROUND:    {rounds}")
            print(f"     PLAYER:   {score_player}")
            print(f"     COMPUTER: {score_computer}")
            print(f"     ")
            print(f"     ")
            if rounds == 0:
                print(f"     Choose ROCK, PAPER or SCISSORS, then answer a question.")
                print(f"     Right answer: Get an additive 10% Sneak-a-Peek-Chance.")
                print(f"     See the Computer's hand and automatically change yours.")
            elif snuck_a_peek == 1:
                print(f"     ")
                print(f"     Player snuck a peek with a {chance_sneak_a_peek}% Sneak-a-Peek-Chance")
                print(f"     ")
            else:
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

        # question loop
        while True:

            # clear screen before redraw new output
            # cls = clear screen command for Windows consoles
            # nt = Windows
            # clear = clear screen command for Linux/MacOS consoles
            os.system("cls" if os.name == "nt" else "clear")

            # questions header
            show_header_sneak_a_peek_question()

            # set question pool with input_lernfeld_de choice
            if input_lernfeld_de == 1:
                question_pool = questions_lf01_de
            elif input_lernfeld_de == 2:
                question_pool = questions_lf02_de
            elif input_lernfeld_de == 3:
                question_pool = questions_lf03_de
            elif input_lernfeld_de == 4:
                question_pool = questions_lf04_de
            elif input_lernfeld_de == 5:
                question_pool = questions_lf05_de
            elif input_lernfeld_de == 6:
                question_pool = questions_lf06_de
            else:
                pass


            # open cache as read write append "a+" as cache_list
            with open("game_caches/game_loop_sneak_a_peek_quiz_cache.txt", "a+") as cache_list:
                # because of "a+" append the file starts at the end
                # .seek(0) sets to pointer to the beginning of the file
                cache_list.seek(0)
                # question_id_list is made by going through every line (line for line) in cache list
                # stripping the \n with . strip() and putting the value into a list [line.strip() for line in cache_list]
                question_id_list = [line.strip() for line in cache_list]


            # check every question in question_pool and get question_id
            # check if in question_id_list
            # all() = only True if every question in cache
            if all(question["question_id"] in question_id_list for question in question_pool):
                input_lernfeld_de = game_loop_sneak_a_peek_quiz_cache_clear_ingame(input_lernfeld_de)
                continue


            # if not all in question_id_list get random question from question_pool
            random_question = random.choice(question_pool)


            # if not all in question_id_list check which question_id is not in question_id_list and do stuff
            if random_question["question_id"] not in question_id_list:

                # print question true false
                print(f"     GAME MODE - SNEAK-A-PEEK QUIZ")
                print(f"     ")
                print(f"     ")
                print(random_question["question"])
                # reserved 5 extra lines here in dictionary
                print(f"     ")
                print(f"     ")
                print(f"     [{YES}] TRUE")
                print(f"     ")
                print(f"     [{NO}] FALSE")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")
                print(f"     ")


                while True:
                    input_question_answer = input(f"     YOUR ANSWER: ").strip()

                    if len(input_question_answer) == 1 and input_question_answer in ("1", "0"):
                        break

                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[2K")
                    sys.stdout.flush()

                input_question_answer_int = int(input_question_answer)

                for _ in range(9):
                    sys.stdout.write("\033[F")
                    sys.stdout.write("\033[2K")
                    sys.stdout.flush()

                if input_question_answer_int == random_question["answer"]:
                    if chance_sneak_a_peek < 100:
                        chance_sneak_a_peek += 10
                    print(f"     Your answer is RIGHT.")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     Added 10% to Sneak-a-Peek-Chance.")
                    print(f"     Your total Sneak-a-Peek-Chance is now at {chance_sneak_a_peek}%.")
                    print(f"     ")
                    print(f"     ")

                    # put right answer in "cache" file
                    with open("game_caches/game_loop_sneak_a_peek_quiz_cache.txt", "a+") as cache_list:
                        cache_list.write(random_question["question_id"] + "\n")

                else:
                    print(f"     Your answer is WRONG.")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     Nothing was added to Sneak-a-Peek-Chance.")
                    print(f"     Your total Sneak-a-Peek-Chance is still at {chance_sneak_a_peek}%.")
                    print(f"     ")
                    print(f"     ")

                input(f"     PRESS ENTER TO SEE ROUND RESULTS...")

                break

            else:
                pass


        # computer random choice 1, 2 or 3
        input_computer = random.randint(1,3)

        # round win roll chance rolls for sneak a peek chance 10, 20, ..., 90, 100%
        snuck_a_peek = 0

        if chance_sneak_a_peek == 10:
            chance = random.randint(1,10)
            if chance == 1:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 20:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 30:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 40:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 50:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4 or chance == 5:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 60:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4 or chance == 5 or chance == 6:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 70:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4 or chance == 5 or chance == 6 or chance == 7:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 80:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4 or chance == 5 or chance == 6 or chance == 7 or chance == 8:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 90:
            chance = random.randint(1,10)
            if chance == 1 or chance == 2 or chance == 3 or chance == 4 or chance == 5 or chance == 6 or chance == 7 or chance == 8 or chance == 9:
                snuck_a_peek = 1
                if input_computer == 1:
                    input_player_int = 2
                elif input_computer == 2:
                    input_player_int = 3
                else:
                    input_player_int = 1

        elif chance_sneak_a_peek == 100:
            snuck_a_peek = 1
            if input_computer == 1:
                input_player_int = 2
            elif input_computer == 2:
                input_player_int = 3
            else:
                input_player_int = 1

        else:
            pass

        os.system("cls" if os.name == "nt" else "clear")

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
            return input_new_game_int, input_lernfeld_de
        else:
            return input_new_game_int, input_lernfeld_de











# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
