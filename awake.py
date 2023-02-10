import pyttsx3
import speech_recognition as sr
from playsound import playsound
import cococheckdb
import cocodbconnect
import cocoindb
import cocomoodle
import cocoyt

listener = sr.Recognizer()
engine = pyttsx3.init()
source = sr.Microphone()


def listening():
    with source:
        engine.say("hello")
        print("listening...")
        command = ""
        engine.runAndWait()
        while "coco" not in command:
            print("listening...")
            try:
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
            except sr.RequestError as e:
                print("error; {0}".format(e))

            except Exception as e:
                print(e)
        cococheckcred()
def cococheckcred():
    engine.say("hello there, can you please enter your username")
    engine.runAndWait()
    username = input("enter your username: ")
    print(username)
    if cocodbconnect.connecttodb():
        if cococheckdb.checkforusername(username):
            engine.say(f"ooh an account with the username {username} exist")
            engine.say("can u please enter the password so i can log you in to the account?")
            engine.runAndWait()
            password = input(f"enter the password for account name {username}: ")
            if cococheckdb.checkforpassword(password):
                cocoawake(username)
            else:
                engine.say("oh looks like the password u just entered was incorrect i guess it was a typing error would you like to re-enter the password")
                engine.runAndWait()
                try:
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    print(command)
                    if "yes" in command:
                        password = input(f"enter the password for account name {username}: ")
                        if cococheckdb.checkforpassword(password):
                            cocoawake(username)
                        else:
                            engine.say("oops incorrect again... i am going to sleep now u can call me if you need me")
                            engine.runAndWait()
                            listening()
                except sr.RequestError as e:
                    print("error; {0}".format(e))

                except Exception as e:
                    print(e)

        else:
            engine.say(f"oh there is no username {username} in the database would you like to create a profile with username {username}")
            engine.runAndWait()
            while True:
                print("listening...")
                try:
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    print(command)
                    if "yes" in command:
                        engine.say("ok that's great and you would require a password for your profile can please enter it:-")
                        engine.runAndWait()
                        password = input(f"set the password for the profile {username}: ")
                        print(password)
                        cocoindb.createuser(username, password)
                        cocoawake(username)
                    else:
                        engine.say("ok got it i am going to sleep now u can call me if you need me")
                        engine.runAndWait()
                        listening()
                except sr.RequestError as e:
                    print("error; {0}".format(e))

                except Exception as e:
                    print(e)

    else:
        engine.say("uh i am sorry but looks like the connection to database failed!, i am going to sleep now u can call me if you need me")
        listening()
def cocoawake(username):
    try:
        engine.say(f"successfully logged in, hello {username}")
        engine.runAndWait()
        print(f"new session with {username} started...")
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        print(command)
        data = list(command.split(" "))
        if "play" in data:
            print("in youtube")
            cocoyt.music(data)
        if "moodle" in data or "assignments" in data:
            print("in moodle")
            cocomoodle.moodlelogin("21106025", "Helloworld@1234")
        else:
            print("can't help you with that")
    except():
        print("bye")