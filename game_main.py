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
from game_modules import (
    game_menu, game_menu_sneak_a_peek, game_menu_just_quiz,
    game_loop_classic, game_loop_cheating_computer, game_loop_sneak_a_peek_quiz, game_loop_just_quiz,
    show_header_6,
)

# main game function
def main():

    # simple press enter to start game input
    print(f"     ")
    print(f"     ")
    press_enter_to_start_program = input(f"     PRESS ENTER TO START PROJECT_RPS...")

    # start loop -> game_menu
    while True:

        # define definition game_menu as variable input_start_game
        # to return input choice from game_menu and choose game mode
        # or quit game
        input_start_game = game_menu()

        # if input_start_game == 0 close game
        if input_start_game == 0:
            return

        # if input_start_game from game_menu = 3 get input_lernfeld_de from game_menu_sneak_a_peek
        if input_start_game == 3 :
            input_lernfeld_de = game_menu_sneak_a_peek()

        # if input_start_game from game_menu = 4 get input_lernfeld_de from game_menu_just_quiz
        if input_start_game == 4 :
            input_lernfeld_de = game_menu_just_quiz()

        # start chosen game mode
        while True:
                os.system("cls" if os.name == "nt" else "clear")
                show_header_6()

                # start classic mode
                if input_start_game == 1:
                    input_new_game_int = 1

                    while True:

                        if input_new_game_int == 1:
                            input_new_game_int = game_loop_classic()
                            continue
                        else:
                            break

                # start cheating computer mode
                elif input_start_game == 2:
                    input_new_game_int = 1

                    while True:

                        if input_new_game_int == 1:
                            input_new_game_int = game_loop_cheating_computer()
                            continue
                        else:
                            break

                # Proof of Concept quiz modes 3 & 4

                # start sneak a peek quiz mode (Game + Quiz)
                elif input_start_game == 3:
                    input_new_game_int = 1


                    while True:

                        if input_new_game_int == 1:
                            # give input_lernfeld_de to and start game_loop_sneak_a_peek
                            # for question new game get input_new_game_int, input_lernfeld_de in game_loop
                            # and return here for if statement
                            # need to put argument in def game_loop_sneak_a_peek_quiz(input_lernfeld_de):
                            # in game_loop_sneak_a_peek_quiz.py else it does not work ;) ArgumentError
                            input_new_game_int, input_lernfeld_de = game_loop_sneak_a_peek_quiz(input_lernfeld_de)
                            continue
                        else:
                            break

                # Just Quiz mode for "endless" questions only (and question debug); at the moment you can only exit by closing the cmd
                elif input_start_game == 4:
                    input_lernfeld_de = game_loop_just_quiz(input_lernfeld_de)


                break

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
