import os
from os import system, listdir
import subprocess
import pyttsx3
import time
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        return query.lower()  # Convert the query to lowercase for case-insensitive comparison
    except Exception as e:
        print("Say that again")
        return "None"

C = open(r"keys\C", "r").readline()

def Generate_Images(prompt: str):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{C}"')
    return listdir("output")[-3:]

class Show_Image:
    def __init__(self, li: list) -> None:
        self.listd = li
        self.current_index = 0

    def open(self, no):
        try:
            if 0 <= no < len(self.listd):
                image_path = os.path.join("output", self.listd[no])
                subprocess.Popen(["start", " ", image_path], shell=True)
            else:
                print(f"Image index {no} out of range.")
        except Exception as e:
            print(f"Error opening image {self.listd[no]}: {e}")

    def show_next(self):
        if not self.listd:
            print("No images to show.")
            return

        try:
            self.open(self.current_index)  # Open the current image
        except Exception as e:
            print(f"Error: {e}")

        self.current_index = (self.current_index + 1) % len(self.listd)  # Move to the next image
          # Assuming you have a speak function defined somewhere

def show_images():
    # Create an instance of Show_Image and display images
    speak("What do you like to generate images Boss?")
    print("What do you like to generate images Boss?")
    prompt_text = takeCommand()  # Get user input using the takeCommand function
    speak("Wait for Few Minutes Boss")
    query = prompt_text.replace("jarvis", "")
    query = query.replace("generate image", "")
    image_list = Generate_Images(prompt_text)

    show_images = Show_Image(image_list)
    show_images.show_next()  # Show the first image

    while True:
        time.sleep(1)  # Wait for 1 second before checking for the next command
        next_command = takeCommand()
        if "next image" in next_command:
            show_images.show_next()
        elif "exit" in next_command:
            print("Exiting image viewer.")
            break

if __name__ == "__main__":
    show_images()
