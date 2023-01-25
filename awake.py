import pyttsx3
import speech_recognition as sr
#from playsound import playsound
listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()
import cocoyt

def listening():
    try:
        with source:
            print("listening...")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

            if "coco" in command:
                awake()
            else:
                listening()

    except():
        print("Exception..")


def awake():
    print("here")
    #playsound("P:\git_pr\PA_\hello_meeth_first.mp3")
    engine.say("what can i do for you?")
    engine.runAndWait()
    try:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        if "play" or "youtube" in command:
            cocoyt.music(command)
    except():
        print("bye")
