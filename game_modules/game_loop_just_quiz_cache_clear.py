"""
project_RPS - game_loop_sneak_a_peek_quiz
"""

# --- CODE START ---

import sys
import os

from .game_art import show_header_lernfeld

from .game_constants import YES, NO

from .game_menu_just_quiz_ingame import game_menu_just_quiz_ingame



def game_loop_just_quiz_cache_clear_inmenu():

    with open("game_caches/game_loop_just_quiz_cache.txt", "w"):
        pass



def game_loop_just_quiz_cache_clear_ingame(input_lernfeld_de):

    input_delete_cache = 0

    # print delete cache message
    os.system("cls" if os.name == "nt" else "clear")
    show_header_lernfeld()
    print(f"     GAME MODE - JUST QUIZ")
    print(f"     ")
    print(f"     ")
    print(f"     You already gave RIGHT answers to all questions")
    print(f"     in Lernfeld {input_lernfeld_de:02d}.")
    print(f"     ")
    print(f"     To CONTINUE delete RIGHT answers for Lernfeld {input_lernfeld_de:02d}")
    print(f"     or pick a different Lernfeld.")
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     [{YES}] DELETE ANSWERS FOR LERNFELD {input_lernfeld_de:02d} AND CONTINUE")
    print(f"     ")
    print(f"     [{NO}] PICK A DIFFERENT LERNFELD AND CONTINUE")
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
    print(f"     ")

    while True:
        input_delete_cache = input(f"     YOUR CHOICE: ").strip()

        # check if input is length of not 1 or value is not 1 or 0
        if len(input_delete_cache) !=1 or input_delete_cache not in ("1","0"):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()
            continue

        # return input as int
        if int(input_delete_cache) == 1:

            # for deleting specific lines that start with "value" you have to read the file with .readlines() and "memorize" it
            # (read_cache_list = cache_list.readlines())
            with open("game_caches/game_loop_just_quiz_cache.txt", "a+") as cache_list:
                cache_list.seek(0)
                read_cache_list = cache_list.readlines()

            # then delete everyting with "w" and and write back every line (for line in read_cache_list:)
            # that doesn't start with "value" you want to delete (if not line.startswith("value"))
            # (cache_list.write(""))
            with open("game_caches/game_loop_just_quiz_cache.txt", "w") as cache_list:
                for line in read_cache_list:
                    if not line.startswith(f"LF{input_lernfeld_de:02d}"):
                        cache_list.write(line)

            for _ in range(9):
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[2K")
                sys.stdout.flush()

            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     ")
            print(f"     Deleted all RIGHT answers for Lernfeld {input_lernfeld_de:02d}.")
            print(f"     ")
            print(f"     ")
            print(f"     ")

            input(f"     PRESS ENTER TO CONTINUE WITH LERNFELD {input_lernfeld_de:02d}...")

            return input_lernfeld_de






        else:
            input_lernfeld_de = game_menu_just_quiz_ingame()
            return int(input_lernfeld_de)













# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
