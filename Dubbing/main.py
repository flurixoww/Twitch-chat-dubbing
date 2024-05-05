from irc_a_v12 import connect_to_twitch
from voice import available_voices
from dotenv import load_dotenv
import os
load_dotenv()

#Displaing available voices 
if os.getenv('SHOW_AVAILABLE_VOICES') == "True":
    available_voices() 

connect_to_twitch() # Connecting to twich 

if __name__ == '__main__':
    connect_to_twitch()