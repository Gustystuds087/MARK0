import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # range to set different voice [0/1 FOR MALE AND FEMAIL]

voicespeed = 140  # setting speed
engine.setProperty('rate', voicespeed)


def speak(audio):  # creating function name 'speak'
    engine.say(audio)
    engine.runAndWait()

speak("i love to watch anime")  # text in to speach