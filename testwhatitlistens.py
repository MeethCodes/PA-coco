import pyttsx3
import speech_recognition as sr
# from playsound import playsound
listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()


def listening():
    islistening = True
    while islistening:
        try:
            with source:
                print("listening...")
                voice = listener.listen(source, timeout=5)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(command)

        except():
            print("couldn't understand")


listening()
