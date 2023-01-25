import selenium
import pywhatkit as pwk

def music(command):
    fdata = []
    data = list(command.split(" "))
    for word in data:
        if word == "youtube" or "play" or "on":
           print(word)
        else:
            fdata = fdata.append(word)

    print(fdata)