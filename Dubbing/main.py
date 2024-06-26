from irc_a_v12 import connect_to_twitch
from voice import available_voices
from dotenv import load_dotenv
import os
from gui import run_login_app

# Load environment variables from a .env file
load_dotenv()

# Display available voices if the corresponding environment variable is set
if os.getenv("SHOW_AVAILABLE_VOICES") == "True":
    available_voices()

#Running the app
run_login_app()
