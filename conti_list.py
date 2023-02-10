import speech_recognition as sr
import webbrowser as wb

# obtain audio from the microphone
r = sr.Recognizer()
# engine = pyttsx3.init()
source = sr.Microphone()
print("Please wait. Calibrating microphone...")
r.adjust_for_ambient_noise(source, duration=5)


def speaking():
    with source:
        print("Say something!")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        said = list(text.split(" "))
        print(said)
        print(text)
        if "coco" in said:
            print("I thinks you said '" + r.recognize_google(audio) + "'")

        else:
            speaking()
    except sr.RequestError as e:
        print("error; {0}".format(e))

    except Exception as e:
        print(e)


speaking()
