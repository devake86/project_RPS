"""
project_RPS - game_sounds
"""

# --- CODE START ---

import winsound

# sounds
def sound_sword_clashhit():
    winsound.PlaySound("game_sounds/sword_clashhit.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_sword_slice():
    winsound.PlaySound("game_sounds/sword_slice.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_whoosh_motion():
    winsound.PlaySound("game_sounds/whoosh_motion.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_blood_splatter_explode():
    winsound.PlaySound("game_sounds/blood_splatter_explode.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_breeze_of_blood():
    winsound.PlaySound("game_sounds/breeze_of_blood.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_body_rips_apart():
    winsound.PlaySound("game_sounds/body_rips_apart.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_snow_step_1():
    winsound.PlaySound("game_sounds/snow_step_1.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_crushed_can():
    winsound.PlaySound("game_sounds/crushed_can.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_paper_ball():
    winsound.PlaySound("game_sounds/paper_ball.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def sound_deep_sea_impact():
    winsound.PlaySound("game_sounds/deep_sea_impact.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


# only this file can start code under "if __name__ == "__main__":"
# will not be started when imported by another file
# pass = do nothing (placeholder) ; error prevention ; to be replaced with real code
if __name__ == "__main__":

    # for use with game_sounds_test.bat
    sound_sword_clashhit()

# --- CODE END ---
