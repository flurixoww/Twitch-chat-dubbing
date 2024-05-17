from irc_a_v12 import connect_to_twitch
from voice import available_voices
from dotenv import load_dotenv
import os
from gui import run_login_app

load_dotenv()

# Displaing available voices
if os.getenv("SHOW_AVAILABLE_VOICES") == "True":
    available_voices()


if os.getenv("USE_GUI") == "True":
    run_login_app()
else:
    connect_to_twitch(None, None)


if __name__ == "__main__":
    run_login_app()
    connect_to_twitch()
