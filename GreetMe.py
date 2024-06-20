import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        print("Good Morning, Boss")
        speak("Good Morning, Boss")
    elif 12 < hour <= 18:
        print("Good Afternoon, Boss")
        speak("Good Afternoon, Boss")
    else:
        print("Good Evening, Boss")
        speak("Good Evening, Boss")

    speak("Please tell me, How can I help you ?")

