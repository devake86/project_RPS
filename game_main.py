"""
project_RPS - game_main
"""

# --- CODE START ---

# import show_header and game_loop from "game_modules/__init__.py"
from game_modules import game_menu, game_loop, game_new

# main game function
def main():

    # main loop
    while True:
        game_menu()
        game_loop()

        # if 0 for new game end function
        # if 1 repeat main
        if not game_new():
            return

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    main()

# --- CODE END ---
