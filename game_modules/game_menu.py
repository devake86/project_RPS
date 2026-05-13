"""
project_RPS - game_menu
"""

# --- CODE START ---

import os

from .game_art import show_header

# placeholder menu ; header only for now
def game_menu():
    os.system("cls" if os.name == "nt" else "clear")
    show_header()

# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":
    pass

# --- CODE END ---
