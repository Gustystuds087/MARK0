import pyttsx3 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #range to set different voice [0/1 for male and fem res]

voicespeed = 85 #setting speed
engine.setProperty('rate',voicespeed)

def speak(audio): #creating function name 'speak'
    engine.say(audio)
    engine.runAndWait()
speak("Hello Sir I am online")   #text to 
