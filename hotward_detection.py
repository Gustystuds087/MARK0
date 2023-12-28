import speech_recognition as sr
import os

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)   

        return "None"
    return query    

while True:
        wake_up = takeCommand()
        if 'wake up' in wake_up:
            os.startfile('C:\\Users\\Anshul\\OneDrive\\Desktop\\MARK0\\Main.py')

        elif 'are you up' in wake_up:
            os.startfile('C:\\Users\\Anshul\\OneDrive\\Desktop\\MARK0\\Main.py')

        else:
            print("none     ")    