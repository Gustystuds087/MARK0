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
    date=int(datetime.datetime.now().day)
    year= int(datetime.datetime.now().year) #calls current year from the module datetime
    month = int(datetime.datetime.now().month) # calls date

    speak("And the date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():   #wish u when program is runned 
    speak("System is online SIR ")   
    time()
    date()
    hour = datetime.datetime.now().hour

#if its morning it will wish goodmorning
    if hour >=6 and hour <=12:
        speak("good morning sir ")  
            
#if it is afternoon it will wish goodafternoon 
    elif hour>=12 and hour <=2:
        speak("Good afternoon sir")

#if it is evening it will wish goodevening 
    elif hour>=12 and hour <=2:
        speak("Good evening sir")

#if it is night it will wish goodnight 
    else :
        speak("Good night sir")   

    speak ("How can i help u")    

wishme() #calling wishme fucntion    