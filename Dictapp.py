import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt"}


def openappweb(query):

    if ".com" in query or ".in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        speak (f"Opening {query} now")
        webbrowser.open(f"https://www.{query}")
    else:
        query = query.replace ("open" , "")
        query = query.replace ("jarvis" , "")
        speak (f"Opening {query} now")
        pyautogui.hotkey ("super" , interval = 0.1)  # Use hotkey for "super" instead of separate press
        pyautogui.typewrite (query , interval = 0.1)  # Adjust the typing interval
        pyautogui.press ("enter" , interval = 0.1)


def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("one tabs closed")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("two tabs closed")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("three tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("four tabs closed")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("five tabs closed")

    elif 'open new window' in query :
        pyautogui.hotkey ('ctrl' , 'n')

    elif 'open incognito window' in query :
        pyautogui.hotkey ('ctrl' , 'shift' , 'n')


    elif 'minimise this window' in query :
        pyautogui.hotkey ('alt' , 'space')
        sleep (1)
        pyautogui.press ('n')

    elif 'open history' in query :
        pyautogui.hotkey ('ctrl' , 'h')

    elif 'open downloads' in query :
        pyautogui.hotkey ('ctrl' , 'j')

    elif 'previous tab' in query :
        pyautogui.hotkey ('ctrl' , 'shift' , 'tab')

    elif 'next tab' in query :
        pyautogui.hotkey ('ctrl' , 'tab')

    elif 'close tab' in query :
        pyautogui.hotkey ('ctrl' , 'w')

    elif 'close window' in query :
        pyautogui.hotkey ('ctrl' , 'shift' , 'w')

    elif 'clear browsing history' in query :
        pyautogui.hotkey ('ctrl' , 'shift' , 'delete')

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
