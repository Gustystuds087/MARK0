import pyttsx3 
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #range to set different voice [0/1 for male and fem res]

voicespeed = 150 #setting speed
engine.setProperty('rate',voicespeed)

def speak(audio): #creating function name 'speak'
    engine.say(audio)
    engine.runAndWait()

#new function name time 
def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
#new fucntion name date
def date():
    month = int(datetime.datetime.now().month)  #calls month
    date = int(datetime.datetime.now().day)  #calls date
    year = int(datetime.datetime.now().year) #calls current year from the module

    #calling by using speak function
    speak(date)
    speak(month)
    speak(year)

date() #calling the date function    
time() #calling the date function    
