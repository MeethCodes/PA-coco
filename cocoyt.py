import selenium
import pywhatkit as pwk


def music(data):
    for word in data:
        if word == "play":
            data.remove(word)

        elif word == "on":
            data.remove(word)

        elif word == "youtube":
            data.remove()

        else:
            pass

    print(data)
