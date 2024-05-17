import pyttsx3
from dotenv import load_dotenv

load_dotenv()
import os

engine = pyttsx3.init()
voices = engine.getProperty("voices")


def available_voices():
    for voice in voices:
        print(voice)


def dubbing(message):
    engine.setProperty("voice", voices[int(os.getenv("VOICE"))].id)
    engine.say(message)

    engine.runAndWait()
