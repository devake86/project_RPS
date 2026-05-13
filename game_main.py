"""
project_RPS - game_main
"""

# --- CODE START ---

# import * (all) from "game_modules/__init__.py"
from game_modules import *

# main game function
def main():

    # variables
    new_game = 0

    # main loop
    while True:
        show_header()
        game_loop()

        # new game ; continue = go to beginning of while-loop ; return = close function
        new_game = int(input(f"\n\n NEW GAME? [{YES}] YES [{NO}] NO: "))
        if new_game == 1:
            continue
        else:
            return

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    main()

# --- CODE END ---
