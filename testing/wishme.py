import pyttsx3 #pip install pyttsx3
import datetime
engine = pyttsx3.init() #initialize pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #range to set different voice

voicespeed = 150 #setting speed
engine.setProperty('rate',voicespeed)

def speak(audio): #creating fun name 'speak'
    engine.say(audio)
    engine.runAndWait()
    

def time(): #new function name time 
    time = datetime.datetime.now().strftime("%H:%M:%S")    
    speak("Current time is  ")
    speak(time)

def date():
    date = int(datetime.datetime.now().day)  #calls date
    year = int(datetime.datetime.now().year) #calls current year from the module
    month = int(datetime.datetime.now().month)  #calls month
  
    speak("And the date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():   #wish u when program is runned 
    speak("System is online SIR ")  
    speak("")  
    time()
    date()
    speak("how can i help you sir")

wishme() #calling wishme fucntion    