"""
project_RPS - game_menu_just_quiz
"""

# --- CODE START ---

import os
import sys

from .game_constants import YES, NO

from .game_animations import show_header_animation

from .game_art import show_header_lernfeld

# menu just quiz
def game_menu_just_quiz_ingame():

    os.system("cls" if os.name == "nt" else "clear")
    show_header_lernfeld()
    print(f"     [1] LERNFELD 01 (Test Questions)")
    print(f"     [2] LERNFELD 02 (Test Questions)")
    print(f"     [3] LERNFELD 03 (Test Questions)")
    print(f"     [4] LERNFELD 04 (Test Questions)")
    print(f"     [5] LERNFELD 05 (Test Questions)")
    print(f"     [6] LERNFELD 06 (Test Questions)")
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
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     ")
    print(f"     ")

    # variables
    input_lernfeld_de = 0

    # new game yes or no ; .strip() = delete spaces before or after input()
    # continue = go to beginning of while-loop
    # break = end while-loop-> go to next line -> no new lines -> starts main() while-loop again with show_header()
    # return = close whole function
    while True:
        input_lernfeld_de = input(f"     YOUR CHOICE: ").strip()

        # check if input is length of not 1 or value is not 1, 2, ..., 5, 6
        if len(input_lernfeld_de) !=1 or input_lernfeld_de not in ("1","2","3","4","5","6"):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()
            continue

        # return input as int
        return int(input_lernfeld_de)

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
