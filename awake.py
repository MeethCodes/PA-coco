import pyttsx3
import speech_recognition as sr
from playsound import playsound
import cocomoodle
import cocoyt

listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()


def listening():
    try:
        with source:
            print("listening...")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

            if "coco" in command:
                cocoawake()
            else:
                listening()

    except():
        print("Exception..")


def cocoawake():
    print("here")
    engine.say("what can i do for you?")
    engine.runAndWait()
    try:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        data = list(command.split(" "))
        if "play" in data:
            print("in youtube")
            cocoyt.music(data)
        elif "moodle" or "assignments" in data:
            print("in moodle")
            cocomoodle.moodlelogin("2110asd6025","Helloworld@1234")

    except():
        print("bye")
