import pyttsx3
import speech_recognition as sr
from playsound import playsound
listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()


def inmoodle():
    print("well congrats you in moodle")
