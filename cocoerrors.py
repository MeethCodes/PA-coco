import pyttsx3
import speech_recognition as sr
from playsound import playsound
listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()


def moodleerror():
    try:
        with source:
            engine.say("looks like the password and username you entered is incorrect")
            engine.runAndWait()
    except():
        print("moodleerror exception..")
