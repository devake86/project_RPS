"""
project_RPS - game_main
"""

# HOW IMPORTS WORK!
# game_main.py doesn't need to import everything to function
# only import what is needed in game_main.py itself
# each file should only import what it needs itself to run its code
# when importing a function or constant in game_main.py,
# the file, the function or constant is from, will be opened and read from top to bottom
# every function or constant used in the files will be loaded into the cache
# game_main.py only needs to call the function or constant and gets the information from the cache

# --- CODE START ---

# import os is needed in this file for clear screen command
import os

# import from "game_modules/__init__.py"
#             "   folder   /    file   "
from game_modules import game_menu, game_loop, game_new, show_header_6

# main game function
def main():

    # start loop -> game_menu
    while True:

        # game menu at game start
        # if returned 1 == False from game_menu for start game -> end function ; game closes
        # if returned 1 == True from game_menu -> got to else and start game
        if not game_menu():
            return

        # if game start True go here
        else:

            # main gameplay loop
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                show_header_6()
                game_loop()

                # new game menu at end of game
                # if returned 1 == False from game_new for new game -> end function ; game closes
                # if returned 1 == True from game_new repeat main
                if not game_new():
                    return

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":

    # start main game function
    # some imports are not usable in Thonny ; use game_start.bat (game opens in CMD window)
    # or other programm like visual studio code to play in console
    main()

    # use for printing every function and constant added to __all__ in (public API) __init__.py
    # all of these can be imported and used with game_main.py
    #from game_modules import __all__
    #print(__all__)

# --- CODE END ---
