# game.py

import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query.lower()

def game_play():
    speak("Let's Play Rock, Paper, Scissors!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    me_score = 0
    com_score = 0
    while i < 3:
        choices = ("rock", "paper", "scissors")  # Tuple
        com_choice = random.choice(choices)
        query = takeCommand()
        speak(f"You chose {query}")
        speak(f"Computer chose {com_choice}")

        if query in ("rock", "paper", "scissors"):
            if query == com_choice:
                speak("It's a tie!")
            elif (
                    (query == "rock" and com_choice == "scissors")
                    or (query == "paper" and com_choice == "rock")
                    or (query == "scissors" and com_choice == "paper")
            ):
                speak("You win this round!")
                me_score += 1
            else:
                speak("Computer wins this round!")
                com_score += 1

            print(f"Score: You - {me_score}, Computer - {com_score}")
            i += 1
        else:
            speak("Invalid choice. Please choose rock, paper, or scissors.")

    speak(f"Final Score: You - {me_score}, Computer - {com_score}")
    speak("Thanks for playing!")

if __name__ == "__main__":
    game_play()
