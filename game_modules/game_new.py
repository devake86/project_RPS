"""
project_RPS - game_new
"""

# --- CODE START ---

import sys

from .game_constants import YES, NO

def game_new():

    # variables
    input_new_game = 0
    input_new_game_int = 0

    # new game yes or no ; .strip() = delete spaces before or after input()
    # continue = go to beginning of while-loop
    # break = end while-loop-> go to next line -> no new lines -> starts main() while-loop again with show_header()
    # return = close whole function
    while True:
        input_new_game = input(f"NEW GAME? [{YES}] YES [{NO}] NO: ").strip()

        # check if input is length of not 1 or value is not 1 or 0
        if len(input_new_game) !=1 or input_new_game not in ("1","0"):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[2K")
            sys.stdout.flush()
            continue

        # change input to int
        input_new_game_int = int(input_new_game)

        # restart or close
        if input_new_game_int == 1:
            return True
        else:
            return False

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
