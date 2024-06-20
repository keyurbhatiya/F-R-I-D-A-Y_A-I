import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendMessage():
    speak("Who do you want to message?")
    person_choice = int(input('''Person 1 - 1
Person 2 - 2\n'''))

    if person_choice == 1:
        receiver_phone = "+919773069326"  # Replace with actual phone number
    elif person_choice == 2:
        receiver_phone = "+1234567890"  # Replace with another phone number
    else:
        speak("Invalid choice. Exiting.")
        return

    speak("What's the message?")
    message = str(input("Enter the message: "))

    try:
        now = datetime.now()
        pywhatkit.sendwhatmsg(receiver_phone, message, now.hour, now.minute + 2, tab_close=True)
        speak("Message sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
        speak("Failed to send the message. Please try again later.")

# Main program
sendMessage()