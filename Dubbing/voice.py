import pyttsx3
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices")

def available_voices():
    """
    Prints the available voices provided by the TTS engine.
    """
    for voice in voices:
        print(voice)

def dubbing(message):
    """
    Uses the TTS engine to speak the given message.
    The voice used is determined by the VOICE environment variable.
    """
    # Set the voice based on the environment variable
    voice_index = int(os.getenv("VOICE", 0))
    engine.setProperty("voice", voices[voice_index].id)
    
    # Speak the message
    engine.say(message)
    engine.runAndWait()
