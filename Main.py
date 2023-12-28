import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import subprocess
import wikipedia
import webbrowser as wb
import os
from time import sleep
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
voicespeed = 180
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S") 
    speak("Current time is  ")
    speak(time)


def date():
    date = int(datetime.datetime.now().day)
    year = int(datetime.datetime.now().year
               )  #calls current year from the module datetime
    month = int(datetime.datetime.now().month)  # calls date

    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("System is Online and ready to begin")
    hour = datetime.datetime.now().hour

    #if its morning it will wish goodmorning
    if hour < 12:
        speak("good morning")

#if it is afternoon it will wish goodafternoon
    elif hour < 18 and hour > 12:
        speak("Good afternoon")


#if it is night it will wish goodnight
    else:
        speak("Good evening")

    speak("Whats the plan for today sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again sir..")

        return "None"
    return query


def open_chrome():
    #url you want to open
    url = 'http://www.google.com/'

    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


def open_edge():
    #url you want to open
    url = 'http://www.microsoft.com/en-us/edge'

    edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    webbrowser.get(edge_path).open(url)




if __name__ == "__main__":  #task execution fucntion

    wishme()

    while True:
        query = takeCommand().lower()  # take command in queary
        print(query)

        if "time" in query:  # if time in query than assistance will say time
            time()  #function get exicuted if time in the query
        elif "date" in query:  # if date in query than assistance will say time
            date()
        elif "offline" in query:  # quit to end the program
            speak("good bye sir")
            speak("going offline")
            quit()

        elif "open google chrome" in query:
            speak("Opening google chrome")
            open_chrome()

        elif "open recent tabs" in query:
            pyautogui.hotkey('ctrl', 'shift', 'T')
            speak("opening recent tabs sir")

        elif "close google chrome" in query:
            speak("Closing google chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "open microsoft edge" in query:
            speak("Opening edge browser")
            open_edge()

        elif "close microsoft edge" in query:
            speak("Closing sir")
            os.system("taskkill /f /im msedge.exe")

        elif "open notepad" in query:  # if open notepad in statement
            speak("opening notepad")  # speak
            location = "C:/WINDOWS/system32/notepad.exe"  # location
            notepad = subprocess.Popen(
                location)  # location of a software you want tot op

        elif "close notepad" in query:
            speak("closing notepad")
            notepad.terminate()  # terminate

        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        # Logout/Shutdown/Restart
        elif "logout" in query:
            speak('logging out in 5 seconds')
            sleep(5)
            os.system("shutdown - l")

        elif "shutdown" in query:
            speak("shutting down in 5 seconds")
            sleep(5)
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak('restarting in 5 seconds')
            sleep(5)
            os.system("shutdown /r /t 1")

        elif "open hidden menu" in query:
            speak("opening sir")
            pyautogui.hotkey('winleft', 'x')

        elif "close hidden menu" in query:
            speak("closing sir")
            pyautogui.hotkey('esc')

        elif "open task manager" in query:
            speak("opening sir")
            # Ctrl+Shift+Esc: Open the Task Manager
            pyautogui.hotkey('ctrl', 'shift', 'esc')

        elif "close task manager" in query:
            speak("Access denied sir")
            os.system("taskkill /f /im Taskmgr.exe")

        elif "open task view" in query:
            speak("opening sir")
            # Win+Tab: Open the Task view
            pyautogui.hotkey('winleft', 'tab')

        elif "take a screenshot" in query:
            # win+perscr
            pyautogui.hotkey('winleft', 'prtscr')
            speak("done")

            # Take screenshot save in Given location
            '''        
                elif "take screenshot" in query:
                    img = pyautogui.screenshot()
                    img.save("D:/screenshot_1.png")  # file mane and location
                    speak("Done")
                    '''
        elif "snip it" in query:
            pyautogui.hotkey('winleft', 'shift', 's')
            speak("done")

        elif "close task view" in query:
            speak("closing sir")
            pyautogui.hotkey('esc')

        elif "open settings" in query:
            # win+i = open setting
            pyautogui.hotkey('winleft', 'i')
            speak("opening settings")

        elif "close settings" in query:
            speak("Closing settings")
            os.system("taskkill /f /im SystemSettings.exe")

        elif "new virtual desktop" in query:
            # Win+Ctrl+D: Add a new virtual desktop
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        else:

            from database.vocabulary.vocabulary import chatterbox

            reply = chatterbox(query)
            speak(reply)
