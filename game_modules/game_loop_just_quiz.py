"""
project_RPS - game_loop_just_quiz
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
    show_header_just_quiz_question,
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

from .game_menu_just_quiz_ingame import game_menu_just_quiz_ingame

from .game_loop_just_quiz_cache_clear import game_loop_just_quiz_cache_clear_ingame

# game loop function
def game_loop_just_quiz(input_lernfeld_de):

    # variables
    input_question_answer = 0
    input_question_answer_int = 0

    # main loop
    while True:


        # question loop
        while True:

            # clear screen before redraw new output
            # cls = clear screen command for Windows consoles
            # nt = Windows
            # clear = clear screen command for Linux/MacOS consoles
            os.system("cls" if os.name == "nt" else "clear")

            # questions header
            show_header_just_quiz_question()

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
            with open("game_caches/game_loop_just_quiz_cache.txt", "a+") as cache_list:
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
                input_lernfeld_de = game_loop_just_quiz_cache_clear_ingame(input_lernfeld_de)
                continue


            # if not all in question_id_list get random question from question_pool
            random_question = random.choice(question_pool)


            # if not all in question_id_list check which question_id is not in question_id_list and do stuff
            if random_question["question_id"] not in question_id_list:

                ##############################
                # ADD QUIT TO MAIN MENU ASAP #
                ##############################

                # print question true false
                #       x-----------------------------------------------------x----x
                #                                                           LF05_000
                print(f"                                       question_id:", random_question["question_id"])
                print(f"     ")
                print(f"     ")
                print(random_question["question"])
                # reserved 5 extra lines here for dictionary text
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

                    print(f"     Your answer is RIGHT.")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")


                    # put right answer in "cache" file
                    with open("game_caches/game_loop_just_quiz_cache.txt", "a+") as cache_list:
                        cache_list.write(random_question["question_id"] + "\n")


                else:
                    print(f"     Your answer is WRONG.")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")
                    print(f"     ")

                input(f"     PRESS ENTER FOR NEXT QUESTION...")

                break

            else:
                pass


        os.system("cls" if os.name == "nt" else "clear")





















# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
