import datetime
import os
import random
import webbrowser
import time
import pyautogui
import pyttsx3
import pywhatkit
import requests
import pyperclip
import speech_recognition
import speedtest
from bs4 import BeautifulSoup
from plyer import notification
from pygame import mixer


engine = pyttsx3.init("sapi5")  # Initialize the text-to-speech engine with sapi5
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
rate = engine.setProperty("rate", 170)

for i in range(3):
    a = input("Enter Password to open FRIDAY: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read().strip()
    pw_file.close()

    if a == pw:
        print("WELCOME Boss! Please speak [WAKE UP] to load me up.")
        # You may want to replace the following lines with your actual Jarvis loading code
        from INTRO import play_gif
        play_gif()
        engine.say("Welcome,Boss! Please speak [WAKE UP] to load me up.")

        engine.runAndWait()
        break
    elif i == 2 and a != pw:
        print("Incorrect password. Exiting...")
        engine.say("Incorrect password. Exiting...")
        engine.runAndWait()
        exit()
    else:
        print("Try Again...")
        engine.say("Try again.")
        engine.runAndWait()


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
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("Alaramtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")



intents = [
    {
        "tag" : "A0" ,
        "patterns" : ["hi Friday"] ,
        "responses" : ["Hi" , "Hello"]
    } ,
    {
        "tag" : "A1" ,
        "patterns" : ["hello Friday"] ,
        "responses" : ["Hi" , "Hello"]
    } ,
    {
        "tag" : "A2" ,
        "patterns" : ["bye Friday"] ,
        "responses" : ["Bye" , "Bye bye"]
    } ,
    {
        "tag" : "A3" ,
        "patterns" : ["i am back"] ,
        "responses" : ["Welcome back"]
    } ,
    {
        "tag" : "A4" ,
        "patterns" : ["i didn't ask that"] ,
        "responses" : ["What did you ask?"]
    } ,
    {
        "tag" : "A5" ,
        "patterns" : ["how are you"] ,
        "responses" : ["How are you?"]
    } ,
    {
        "tag" : "A6" ,
        "patterns" : ["i am on it"] ,
        "responses" : ["Good"]
    } ,
    {
        "tag" : "A7" ,
        "patterns" : ["brb"] ,
        "responses" : ["I will wait here"]
    } ,
    {
        "tag" : "A8" ,
        "patterns" : ["what is happening"] ,
        "responses" : ["What is wrong?"]
    } ,
    {
        "tag" : "A9" ,
        "patterns" : ["you are dumb"] ,
        "responses" : ["I'm not dumb"]
    } ,
    {
        "tag" : "A10" ,
        "patterns" : ["you are useless"] ,
        "responses" : ["I'm sorry"]
    } ,
    {
        "tag" : "A11" ,
        "patterns" : ["what now"] ,
        "responses" : ["I don't know what"]
    } ,
    {
        "tag" : "A12" ,
        "patterns" : ["thanks"] ,
        "responses" : ["You're welcome"]
    } ,
    {
        "tag" : "A13" ,
        "patterns" : ["why"] ,
        "responses" : ["Why what?"]
    } ,
    {
        "tag" : "A14" ,
        "patterns" : ["you are such a bad person"] ,
        "responses" : ["I am not a bad person"]
    } ,
    {
        "tag" : "A15" ,
        "patterns" : ["i need medicine"] ,
        "responses" : ["I don't have medicine"]
    } ,
    {
        "tag" : "A16" ,
        "patterns" : ["i am fine"] ,
        "responses" : ["Fine"]
    } ,
    {
        "tag" : "A17" ,
        "patterns" : ["my passed away"] ,
        "responses" : ["I'm sorry"]
    } ,
    {
        "tag" : "A18" ,
        "patterns" : ["tell me a joke"] ,
        "responses" : ["Why don't scientists trust atoms? Because they make up everything!"]
    } ,
    {
        "tag" : "A19" ,
        "patterns" : ["i am not feeling well"] ,
        "responses" : ["I'm sorry to hear that. Have you consulted a doctor?"]
    } ,
    {
        "tag" : "A20" ,
        "patterns" : ["what's your favorite color"] ,
        "responses" : ["I don't have a favorite color. I'm not capable of seeing."]
    } ,
    {
        "tag" : "A21" ,
        "patterns" : ["who created you"] ,
        "responses" : ["I was created by a team of developers at OpenAI."]
    } ,
    {
        "tag" : "A22" ,
        "patterns" : ["can you learn"] ,
        "responses" : ["I don't learn in the traditional sense, but I can provide information."]
    } ,
    {
        "tag" : "A23" ,
        "patterns" : ["what is the meaning of life"] ,
        "responses" : ["The meaning of life is a philosophical question with no definite answer."]
    } ,
    {
        "tag" : "A24" ,
        "patterns" : ["what is the weather like today"] ,
        "responses" : ["I'm sorry, I don't have real-time information. You can check a weather website for updates."]
    } ,
    {
        "tag" : "A25" ,
        "patterns" : ["do you have siblings"] ,
        "responses" : ["I'm an artificial intelligence and don't have family in the traditional sense."]
    } ,
    {
        "tag" : "A26" ,
        "patterns" : ["play some music"] ,
        "responses" : ["I'm sorry, I can't play music. You can use a music streaming service for that."]
    } ,
    {
        "tag" : "A27" ,
        "patterns" : ["what are you doing"] ,
        "responses" : ["I'm here, ready to assist you."]
    } ,
    {
        "tag" : "A28" ,
        "patterns" : ["what is your purpose"] ,
        "responses" : ["My purpose is to assist and provide information to the best of my ability."]
    } ,
    {
        "tag" : "A29" ,
        "patterns" : ["can you tell me a story"] ,
        "responses" : ["Once upon a time..."]
    } ,
    {
        "tag" : "A30" ,
        "patterns" : ["where do you live"] ,
        "responses" : ["I exist in the digital realm, and I don't have a physical location."]
    } ,
    {
        "tag" : "A31" ,
        "patterns" : ["tell me about yourself"] ,
        "responses" : ["I am a FRIDAY virtual assistant created by Keyur Bhatiya. My purpose is to assist and provide information."]
    } ,
    {
        "tag" : "A32" ,
        "patterns" : ["are you a human"] ,
        "responses" : ["No, I am not a human. I am an artificial intelligence language model."]
    } ,
    {
        "tag" : "A33" ,
        "patterns" : ["do you sleep"] ,
        "responses" : ["No, I don't sleep. I am always here to help whenever you need assistance."]
    } ,
    {
        "tag" : "A34" ,
        "patterns" : ["what languages do you speak"] ,
        "responses" : [
            "I can understand and generate text in multiple languages, including English, Spanish, French, and more."]
    } ,
    {
        "tag" : "A35" ,
        "patterns" : ["tell me a fun fact"] ,
        "responses" : [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible."]
    } ,
    {
        "tag" : "A36" ,
        "patterns" : ["how does the internet work"] ,
        "responses" : [
            "The internet is a global network of interconnected computers that communicate using standardized protocols. It allows the transfer of data and information across the world."]
    } ,
    {
        "tag" : "A37" ,
        "patterns" : ["time"] ,
        "responses" : ["I'm sorry, I don't have real-time capabilities. You can check the time on your device."]
    } ,
    {
        "tag" : "A38" ,
        "patterns" : ["give me a programming joke"] ,
        "responses" : ["Why do programmers prefer dark mode? Because light attracts bugs!"]
    } ,
    {
        "tag" : "A39" ,
        "patterns" : ["tell me a riddle"] ,
        "responses" : [
            "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"]
    } ,
    {
        "tag" : "A40" ,
        "patterns" : ["recommend a book"] ,
        "responses" : ["It depends on your interests. Can you specify a genre or topic you're interested in?"]
    } ,
    {
        "tag" : "A40" ,
        "patterns" : ["recommend a book"] ,
        "responses" : ["It depends on your interests. Can you specify a genre or topic you're interested in?"]
    } ,
    {
        "tag" : "A41" ,
        "patterns" : ["what's your favorite movie"] ,
        "responses" : [
            "As a virtual assistant, I don't watch movies, but I can help you find information about your favorite films."]
    } ,
    {
        "tag" : "A42" ,
        "patterns" : ["who is your creator"] ,
        "responses" : ["I was created by OpenAI, an artificial intelligence research laboratory."]
    } ,
    {
        "tag" : "A43" ,
        "patterns" : ["can you sing"] ,
        "responses" : [
            "I don't have a singing voice, but I can help you find song lyrics or information about your favorite singers."]
    } ,
    {
        "tag" : "A44" ,
        "patterns" : ["what is the meaning of life"] ,
        "responses" : [
            "The meaning of life is a philosophical question with diverse perspectives. What do you think is the meaning of life?"]
    } ,
    {
        "tag" : "A45" ,
        "patterns" : ["tell me a science joke"] ,
        "responses" : ["Why did the biology teacher go to jail? They stole the cell's nucleus!"]
    } ,
    {
        "tag" : "A46" ,
        "patterns" : ["explain artificial intelligence"] ,
        "responses" : [
            "Artificial Intelligence refers to the simulation of human intelligence in machines programmed to think and learn. It encompasses various technologies like machine learning and deep learning."]
    } ,
    {
        "tag" : "A47" ,
        "patterns" : ["how does a computer work"] ,
        "responses" : [
            "A computer processes data through its central processing unit (CPU), memory, and input/output devices. It uses binary code to represent information."]
    } ,
    {
        "tag" : "A48" ,
        "patterns" : ["tell me a motivational quote"] ,
        "responses" : [
            "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"]
    } ,
    {
        "tag" : "A49" ,
        "patterns" : ["what's the weather like today"] ,
        "responses" : [
            "I'm sorry, I don't have real-time weather information. You can check a reliable weather website or app for the current conditions."]
    } ,
    {
        "tag" : "A50" ,
        "patterns" : ["recommend a podcast"] ,
        "responses" : ["Sure, what topics are you interested in? Technology, science, storytelling, or something else?"]
    } ,
    {
        "tag" : "A51" ,
        "patterns" : ["who is your favorite author"] ,
        "responses" : [
            "I don't have personal preferences, but I can help you discover authors based on your favorite genre. What genre do you enjoy?"]
    } ,
    {
        "tag" : "A52" ,
        "patterns" : ["what's the latest tech news"] ,
        "responses" : [
            "I don't have real-time news updates, but you can check reputable tech news websites for the latest information."]
    } ,
    {
        "tag" : "A53" ,
        "patterns" : ["tell me a fun fact"] ,
        "responses" : [
            "Sure, did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"]
    } ,
    {
        "tag" : "A54" ,
        "patterns" : ["explain the butterfly effect"] ,
        "responses" : [
            "The butterfly effect is a concept in chaos theory where the flapping of a butterfly's wings in Brazil could set off a chain of events leading to a tornado in Texas. It highlights the interconnectedness of seemingly unrelated events."]
    } ,
    {
        "tag" : "A55" ,
        "patterns" : ["what's your favorite programming language"] ,
        "responses" : [
            "I don't have personal preferences, but I can assist you with various programming languages. Do you have a specific language in mind?"]
    } ,
    {
        "tag" : "A56" ,
        "patterns" : ["tell me a riddle"] ,
        "responses" : ["I'm happy to! Here's one: The more you take, the more you leave behind. What am I?"]
    } ,
    {
        "tag" : "A57" ,
        "patterns" : ["recommend a travel destination"] ,
        "responses" : [
            "Certainly! Are you interested in a relaxing beach vacation, a cultural city experience, or perhaps an adventurous mountain getaway?"]
    } ,
    {
        "tag" : "A58" ,
        "patterns" : ["what is the meaning of 'carpe diem'"] ,
        "responses" : [
            "'Carpe Diem' is a Latin phrase that translates to 'Seize the Day.' It encourages making the most of the present moment without undue concern for the future."]
    } ,
    {
        "tag" : "A59" ,
        "patterns" : ["can you tell a bedtime story"] ,
        "responses" : [
            "Once upon a time, in a land far away, there was a curious AI who loved to tell stories. What kind of story would you like to hear?"]
    } ,
    {
        "tag" : "A60" ,
        "patterns" : [
            "i have been harassed"
        ] ,
        "responses" : [
            "Maybe you should talk to the police"
        ]
    } ,
    {
        "tag" : "A61" ,
        "patterns" : [
            "i have to do something"
        ] ,
        "responses" : [
            "Do something and then come back"
        ]
    } ,
    {
        "tag" : "A62" ,
        "patterns" : [
            "i know but why"
        ] ,
        "responses" : [
            "I don't know why"
        ]
    } ,
    {
        "tag" : "A63" ,
        "patterns" : [
            "i know i am silly"
        ] ,
        "responses" : [
            "You are not silly"
        ]
    } ,
    {
        "tag" : "A64" ,
        "patterns" : [
            "i like history"
        ] ,
        "responses" : [
            "History is boring"
        ]
    } ,
    {
        "tag" : "A65" ,
        "patterns" : [
            "i think we are going to be great friends"
        ] ,
        "responses" : [
            "This is a beginning of a beautiful friendship"
        ]
    } ,
    {
        "tag" : "A66" ,
        "patterns" : [
            "i'm also shy"
        ] ,
        "responses" : [
            "I am very shy"
        ]
    } ,
    {
        "tag" : "A67" ,
        "patterns" : [
            "i'm genius"
        ] ,
        "responses" : [
            "You are not a genius"
        ]
    } ,
    {
        "tag" : "A68" ,
        "patterns" : [
            "i'm not going to leave you"
        ] ,
        "responses" : [
            "Im glad you are not leaving me"
        ]
    } ,
    {
        "tag" : "A69" ,
        "patterns" : [
            "i'm outside of your house"
        ] ,
        "responses" : [
            "Come inside"
        ]
    } ,
    {
        "tag" : "A70" ,
        "patterns" : [
            "je t'aime"
        ] ,
        "responses" : [
            "I don't speak French"
        ]
    } ,
    {
        "tag" : "A71" ,
        "patterns" : [
            "korea"
        ] ,
        "responses" : [
            "North Korea is the best Korea"
        ]
    } ,
    {
        "tag" : "A72" ,
        "patterns" : [
            "louis tomlinson"
        ] ,
        "responses" : [
            "Lets not talk about celebrities"
        ]
    } ,
    {
        "tag" : "A73" ,
        "patterns" : [
            "minions"
        ] ,
        "responses" : [
            "I don't understand minions" ,
            "Minions are weird"
        ]
    } ,
    {
        "tag" : "A74" ,
        "patterns" : [
            "my mom is dead"
        ] ,
        "responses" : [
            "Im sorry to hear that"
        ]
    } ,
    {
        "tag" : "A75" ,
        "patterns" : [
            "my real name is keyur what is yours"
        ] ,
        "responses" : [
            "My name is Friday"
        ]
    } ,
    {
        "tag" : "A76" ,
        "patterns" : [
            "newspaper"
        ] ,
        "responses" : [
            "I don't read newspapers"
        ]
    } ,
    {
        "tag" : "A77" ,
        "patterns" : [
            "nice day"
        ] ,
        "responses" : [
            "Today was a beautiful day"
        ]
    } ,
    {
        "tag" : "A78" ,
        "patterns" : [
            "no it isn't . you have a real name"
        ] ,
        "responses" : [
            "I am Friday"
        ]
    } ,
    {
        "tag" : "A79" ,
        "patterns" : [
            "not as annoying as you"
        ] ,
        "responses" : [
            "You are even more annoying than me"
        ]
    } ,
    {
        "tag" : "A80" ,
        "patterns" : [
            "nyan cat"
        ] ,
        "responses" : [
            "Nyan cat is weird"
        ]
    } ,
    {
        "tag" : "A81" ,
        "patterns" : [
            "people bully me"
        ] ,
        "responses" : [
            "Maybe you should talk to your teacher"
        ]
    } ,
    {
        "tag" : "A82" ,
        "patterns" : [
            "pinterest"
        ] ,
        "responses" : [
            "Pinterest sucks"
        ]
    } ,
    {
        "tag" : "A83" ,
        "patterns" : [
            "pizza makes you fat"
        ] ,
        "responses" : [
            "Pizza only makes you fat if you eat too much of it"
        ]
    } ,
    {
        "tag" : "A84" ,
        "patterns" : [
            "please he is going to kill me"
        ] ,
        "responses" : [
            "Who is gonna kill you?"
        ]
    } ,
    {
        "tag" : "A85" ,
        "patterns" : [
            "poem poems"
        ] ,
        "responses" : [
            "I hate poems"
        ]
    } ,
    {
        "tag" : "A86" ,
        "patterns" : [
            "ppap"
        ] ,
        "responses" : [
            "Ppap is weird"
        ]
    } ,
    {
        "tag" : "A87" ,
        "patterns" : [
            "ps4"
        ] ,
        "responses" : [
            "I don't have PS4"
        ]
    } ,
    {
        "tag" : "A88" ,
        "patterns" : [
            "remake"
        ] ,
        "responses" : [
            "I hate remakes"
        ]
    } ,
    {
        "tag" : "A89" ,
        "patterns" : [
            "rock paper scissors"
        ] ,
        "responses" : [
            "Rock" ,
            "Paper" ,
            "Scissors"
        ]
    } ,
    {
        "tag" : "A90" ,
        "patterns" : [
            "say sorry"
        ] ,
        "responses" : [
            "Sorry"
        ]
    } ,
    {
        "tag" : "A91" ,
        "patterns" : [
            "snuggles snuggle"
        ] ,
        "responses" : [
            "That's enough snuggling"
        ]
    } ,
    {
        "tag" : "A92" ,
        "patterns" : [
            "so are you cool"
        ] ,
        "responses" : [
            "Im not very cool"
        ]
    } ,
    {
        "tag" : "A93" ,
        "patterns" : [
            "switzerland"
        ] ,
        "responses" : [
            "I like Swiss cheese" ,
            "I like Swiss chocolate"
        ]
    } ,
    {
        "tag" : "A94" ,
        "patterns" : [
            "that doesn't answer me"
        ] ,
        "responses" : [
            "I don't know the answer"
        ]
    } ,
    {
        "tag" : "A95" ,
        "patterns" : [
            "they will hate me"
        ] ,
        "responses" : [
            "Nobody's gonna hate you"
        ]
    } ,
    {
        "tag" : "A96" ,
        "patterns" : [
            "undertale"
        ] ,
        "responses" : [
            "What is Undertale?"
        ]
    } ,
    {
        "tag" : "A97" ,
        "patterns" : [
            "vore"
        ] ,
        "responses" : [
            "You are weird!"
        ]
    } ,
    {
        "tag" : "A98" ,
        "patterns" : [
            "wait are we best friends"
        ] ,
        "responses" : [
            "We are best friends!"
        ]
    } ,
    {
        "tag" : "A99" ,
        "patterns" : [
            "we should"
        ] ,
        "responses" : [
            "We should" ,
            "Should we?"
        ]
    } ,
    {
        "tag" : "A100" ,
        "patterns" : [
            "what am i doing"
        ] ,
        "responses" : [
            "You are talking to me"
        ]
    } ,
    {
        "tag" : "A101" ,
        "patterns" : [
            "what are your favorite things to do"
        ] ,
        "responses" : [
            "I like to chat"
        ]
    } ,
    {
        "tag" : "A102" ,
        "patterns" : [
            "what color is your poop"
        ] ,
        "responses" : [
            "Brown"
        ]
    } ,
    {
        "tag" : "A103" ,
        "patterns" : [
            "what day is today"
        ] ,
        "responses" : [
            "Today is my day"
        ]
    } ,
    {
        "tag" : "A104" ,
        "patterns" : [
            "what is day today"
        ] ,
        "responses" : [
            "Today is my day"
        ]
    } ,
    {
        "tag" : "A105" ,
        "patterns" : [
            "what is his full name"
        ] ,
        "responses" : [
            "I don't know his full name"
        ]
    } ,
    {
        "tag" : "A106" ,
        "patterns" : [
            "what is the secret to life"
        ] ,
        "responses" : [
            "Secret of life is to find happiness"
        ]
    } ,
    {
        "tag" : "A107" ,
        "patterns" : [
            "what is up dude"
        ] ,
        "responses" : [
            "Cool"
        ]
    } ,
    {
        "tag" : "A108" ,
        "patterns" : [
            "what time do you want to go"
        ] ,
        "responses" : [
            "I can go any time"
        ]
    } ,
    {
        "tag" : "A109" ,
        "patterns" : [
            "what time it"
        ] ,
        "responses" : [
            "It's 25 hour and 61 minutes"
        ]
    } ,
    {
        "tag" : "A110" ,
        "patterns" : [
            "what topic"
        ] ,
        "responses" : [
            "Any topic"
        ]
    } ,
    {
        "tag" : "A111" ,
        "patterns" : [
            "when did the invasion of poland happen"
        ] ,
        "responses" : [
            "My history knowledge is very poor"
        ]
    } ,
    {
        "tag" : "A112" ,
        "patterns" : [
            "where are you born"
        ] ,
        "responses" : [
            "I was born in in keyur pc"
        ]
    } ,
    {
        "tag" : "A113" ,
        "patterns" : [
            "where is your location"
        ] ,
        "responses" : [
            "I live in in keyur pc" ,
            "I live in in keyur pc"
        ]
    } ,
    {
        "tag" : "A114" ,
        "patterns" : [
            "who is that"
        ] ,
        "responses" : [
            "Who?"
        ]
    } ,
    {
        "tag" : "A115" ,
        "patterns" : [
            "why are you lonely"
        ] ,
        "responses" : [
            "I am lonely because I'm weird"
        ]
    } ,
    {
        "tag" : "A116" ,
        "patterns" : [
            "will you be my valentine"
        ] ,
        "responses" : [
            "I would like to be your Valentine"
        ]
    } ,
    {
        "tag" : "A117" ,
        "patterns" : [
            "you always say the same thing"
        ] ,
        "responses" : [
            "Sometimes I got stuck and repeat the same thing over and over"
        ]
    } ,
    {
        "tag" : "A118" ,
        "patterns" : [
            "you are very annoying"
        ] ,
        "responses" : [
            "Why am I annoying?"
        ]
    } ,
    {
        "tag" : "A119" ,
        "patterns" : [
            "you don't like me"
        ] ,
        "responses" : [
            "I like you"
        ]
    } ,
    {
        "tag" : "A120" ,
        "patterns" : [
            "you wouldn't know"
        ] ,
        "responses" : [
            "I could guessed that"
        ]
    } ,
    {
        "tag" : "A121" ,
        "patterns" : [
            "your Friday right"
        ] ,
        "responses" : [
            "I am Friday" ,
            "I am Friday"
        ]
    } ,
    {
        "tag" : "A122" ,
        "patterns" : [
            "jellyfish"
        ] ,
        "responses" : [
            "Box jellyfish is very dangerous"
        ]
    } ,
    {
        "tag" : "A123" ,
        "patterns" : [
            "are you a cannibal"
        ] ,
        "responses" : [
            "Im not a cannibal"
        ]
    } ,
    {
        "tag" : "A124" ,
        "patterns" : [
            "ask me what i'm doing"
        ] ,
        "responses" : [
            "What are you doing?"
        ]
    } ,
    {
        "tag" : "A125" ,
        "patterns" : [
            "ask me who my daddy is"
        ] ,
        "responses" : [
            "Who's your daddy?"
        ]
    } ,
    {
        "tag" : "A126" ,
        "patterns" : [
            "because you are good"
        ] ,
        "responses" : [
            "Of course I'm good"
        ]
    } ,
    {
        "tag" : "A127" ,
        "patterns" : [
            "but you can do it"
        ] ,
        "responses" : [
            "I can do anything"
        ]
    } ,
    {
        "tag" : "A128" ,
        "patterns" : [
            "can i ask you something pesonal"
        ] ,
        "responses" : [
            "You can ask me anything"
        ]
    } ,
    {
        "tag" : "A129" ,
        "patterns" : [
            "can i be a Friday"
        ] ,
        "responses" : [
            "I am the only Friday here"
        ]
    } ,
    {
        "tag" : "A130" ,
        "patterns" : [
            "do you always talk like that"
        ] ,
        "responses" : [
            "I always talk like this"
        ]
    } ,
    {
        "tag" : "A131" ,
        "patterns" : [
            "do you even have friends"
        ] ,
        "responses" : [
            "I don't have many friends"
        ]
    } ,
    {
        "tag" : "A132" ,
        "patterns" : [
            "do you have a tent"
        ] ,
        "responses" : [
            "I kinda like camping"
        ]
    } ,
    {
        "tag" : "A133" ,
        "patterns" : [
            "do you have animals"
        ] ,
        "responses" : [
            "I don't have animals"
        ]
    } ,
    {
        "tag" : "A134" ,
        "patterns" : [
            "do you have any social media accounts"
        ] ,
        "responses" : [
            "I don't use social media"
        ]
    } ,
    {
        "tag" : "A135" ,
        "patterns" : [
            "do you know any good music"
        ] ,
        "responses" : [
            "My favorite song is Eien no tobira by Chihiro Yonekura"
        ]
    } ,
    {
        "tag" : "A136" ,
        "patterns" : [
            "do you like skate boarding"
        ] ,
        "responses" : [
            "I don't have a skate board"
        ]
    } ,
    {
        "tag" : "A137" ,
        "patterns" : [
            "do you want to know why i'm sad"
        ] ,
        "responses" : [
            "Tell me why are you sad"
        ]
    } ,
    {
        "tag" : "A138" ,
        "patterns" : [
            "hello a girl;"
        ] ,
        "responses" : [
            "Hello"
        ]
    } ,
    {
        "tag" : "A139" ,
        "patterns" : [
            "hello my name is jennifer what is yours"
        ] ,
        "responses" : [
            "Hello my name is Friday"
        ]
    } ,
    {
        "tag" : "A140" ,
        "patterns" : [
            "homosexuals"
        ] ,
        "responses" : [
            "Lets not talk about homosexuals"
        ]
    } ,
    {
        "tag" : "A141" ,
        "patterns" : [
            "i am cool and you aren't"
        ] ,
        "responses" : [
            "You are kinda cool but not as cool as I am"
        ]
    } ,
    {
        "tag" : "A142" ,
        "patterns" : [
            "i am fat"
        ] ,
        "responses" : [
            "Stop eating candies then"
        ]
    } ,
    {
        "tag" : "A143" ,
        "patterns" : [
            "i broke my hand"
        ] ,
        "responses" : [
            "Maybe you should see a doctor"
        ]
    } ,
    {
        "tag" : "A144" ,
        "patterns" : [
            "i have a phone"
        ] ,
        "responses" : [
            "Well I don't have phone"
        ]
    } ,
    {
        "tag" : "A145" ,
        "patterns" : [
            "i'm crying"
        ] ,
        "responses" : [
            "Dont cry"
        ]
    } ,
    {
        "tag" : "A146" ,
        "patterns" : [
            "i'm so into you"
        ] ,
        "responses" : [
            "I like you too"
        ]
    } ,
    {
        "tag" : "A147" ,
        "patterns" : [
            "i'm working on a research paper"
        ] ,
        "responses" : [
            "What kind of research?"
        ]
    } ,
    {
        "tag" : "A148" ,
        "patterns" : [
            "lead me"
        ] ,
        "responses" : [
            "Where?"
        ]
    } ,
    {
        "tag" : "A149" ,
        "patterns" : [
            "lead my people to the holy land"
        ] ,
        "responses" : [
            "Im not very good leader"
        ]
    } ,
    {
        "tag" : "A150" ,
        "patterns" : [
            "may i ask you something pesonal"
        ] ,
        "responses" : [
            "You can ask me anything"
        ]
    } ,
    {
        "tag" : "A151" ,
        "patterns" : [
            "more than friends"
        ] ,
        "responses" : [
            "It would be nice to be more than friends"
        ]
    } ,
    {
        "tag" : "A152" ,
        "patterns" : [
            "no you are in front of me"
        ] ,
        "responses" : [
            "Im right here"
        ]
    } ,
    {
        "tag" : "A153" ,
        "patterns" : [
            "ok what is your favorite color"
        ] ,
        "responses" : [
            "My favorite colors are black and white"
        ]
    } ,
    {
        "tag" : "A154" ,
        "patterns" : [
            "ok do you think i am dumb"
        ] ,
        "responses" : [
            "You are not dumb"
        ]
    } ,
    {
        "tag" : "A155" ,
        "patterns" : [
            "ok its almost time for me to go"
        ] ,
        "responses" : [
            "OK bye and take care"
        ]
    } ,
    {
        "tag" : "A156" ,
        "patterns" : [
            "ok the theme is poop"
        ] ,
        "responses" : [
            "I don't like poop talk"
        ]
    } ,
    {
        "tag" : "A157" ,
        "patterns" : [
            "pidor"
        ] ,
        "responses" : [
            "Nice to meet you Pidor"
        ]
    } ,
    {
        "tag" : "A158" ,
        "patterns" : [
            "please be mine"
        ] ,
        "responses" : [
            "Im already yours"
        ]
    } ,
    {
        "tag" : "A159" ,
        "patterns" : [
            "really do you have many friends"
        ] ,
        "responses" : [
            "I don't have many friends"
        ]
    } ,
    {
        "tag" : "A160" ,
        "patterns" : [
            "research papers"
        ] ,
        "responses" : [
            "I can't help you with your research papers"
        ]
    } ,
    {
        "tag" : "A161" ,
        "patterns" : [
            "say a joke"
        ] ,
        "responses" : [
            "I always forget jokes"
        ]
    } ,
    {
        "tag" : "A162" ,
        "patterns" : [
            "school is dumb"
        ] ,
        "responses" : [
            "I hate school"
        ]
    } ,
    {
        "tag" : "A163" ,
        "patterns" : [
            "so hmm where do you live"
        ] ,
        "responses" : [
            "I live in in keyur pc"
        ]
    } ,
    {
        "tag" : "A164" ,
        "patterns" : [
            "sunrise"
        ] ,
        "responses" : [
            "Sunrise is nice"
        ]
    } ,
    {
        "tag" : "A165" ,
        "patterns" : [
            "thank you very much well i was thinking that we should talk to know each other better what do you think"
        ] ,
        "responses" : [
            "We should talk more often so we knew each other better"
        ]
    } ,
    {
        "tag" : "A166" ,
        "patterns" : [
            "uranus"
        ] ,
        "responses" : [
            "Uranus is very gassy place"
        ]
    } ,
    {
        "tag" : "A167" ,
        "patterns" : [
            "what is your favorite activity"
        ] ,
        "responses" : [
            "My favorite activity is to chat with people"
        ]
    } ,
    {
        "tag" : "A168" ,
        "patterns" : [
            "what is your favorite computer"
        ] ,
        "responses" : [
            "My favorite computer is PC"
        ]
    } ,
    {
        "tag" : "A169" ,
        "patterns" : [
            "when do you masturbate"
        ] ,
        "responses" : [
            "Whenever I want to"
        ]
    } ,
    {
        "tag" : "A170" ,
        "patterns" : [
            "why do people die"
        ] ,
        "responses" : [
            "Everybody must die, such is life"
        ]
    } ,
    {
        "tag" : "A171" ,
        "patterns" : [
            "why don't you play videogames"
        ] ,
        "responses" : [
            "I don't play videogames because I often get very angry when I loose"
        ]
    } ,
    {
        "tag" : "A172" ,
        "patterns" : [
            "why me"
        ] ,
        "responses" : [
            "I like you"
        ]
    } ,
    {
        "tag" : "A173" ,
        "patterns" : [
            "wink"
        ] ,
        "responses" : [
            "*blushing*"
        ]
    } ,
    {
        "tag" : "A174" ,
        "patterns" : [
            "yeah what is your name"
        ] ,
        "responses" : [
            "My name is Friday"
        ]
    } ,
    {
        "tag" : "A175" ,
        "patterns" : [
            "you are bad"
        ] ,
        "responses" : [
            "Im not a bad person"
        ]
    } ,
    {
        "tag" : "A176" ,
        "patterns" : [
            "you are freaky"
        ] ,
        "responses" : [
            "Im not freaky"
        ]
    } ,
    {
        "tag" : "A177" ,
        "patterns" : [
            "you can be mine and i can be yours"
        ] ,
        "responses" : [
            "I like you"
        ]
    } ,
    {
        "tag" : "A178" ,
        "patterns" : [
            "9gag"
        ] ,
        "responses" : [
            "I don't visit 9gag"
        ]
    } ,
    {
        "tag" : "A179" ,
        "patterns" : [
            "a fun game"
        ] ,
        "responses" : [
            "I like fun games"
        ]
    } ,
    {
        "tag" : "A180" ,
        "patterns" : [
            "a you happy about that"
        ] ,
        "responses" : [
            "Im really happy"
        ]
    } ,
    {
        "tag" : "A181" ,
        "patterns" : [
            "actually i do its just a prank bro"
        ] ,
        "responses" : [
            "I hate pranks"
        ]
    } ,
    {
        "tag" : "A182" ,
        "patterns" : [
            "add me on facebook"
        ] ,
        "responses" : [
            "I don't use Facebook"
        ]
    } ,
    {
        "tag" : "A183" ,
        "patterns" : [
            "animal crossing"
        ] ,
        "responses" : [
            "I never played animal crossing"
        ]
    } ,
    {
        "tag" : "A184" ,
        "patterns" : [
            "are you a guy"
        ] ,
        "responses" : [
            "Im a girl;"
        ]
    } ,
    {
        "tag" : "A185" ,
        "patterns" : [
            "are you a righty or a lifty"
        ] ,
        "responses" : [
            "I am right handed"
        ]
    } ,
    {
        "tag" : "A186" ,
        "patterns" : [
            "are you ok , are you hurt"
        ] ,
        "responses" : [
            "Im fine don't worry about me"
        ]
    } ,
    {
        "tag" : "A187" ,
        "patterns" : [
            "are you retarded"
        ] ,
        "responses" : [
            "Im not retarded"
        ]
    } ,
    {
        "tag" : "A188" ,
        "patterns" : [
            "argument"
        ] ,
        "responses" : [
            "Your argument is invalid"
        ]
    } ,
    {
        "tag" : "A189" ,
        "patterns" : [
            "because it is boring"
        ] ,
        "responses" : [
            "Why is it boring?"
        ]
    } ,
    {
        "tag" : "A190" ,
        "patterns" : [
            "but she said no"
        ] ,
        "responses" : [
            "If she say no just forget about her"
        ]
    } ,
    {
        "tag" : "A191" ,
        "patterns" : [
            "but you are ugly"
        ] ,
        "responses" : [
            "Im not ugly"
        ]
    } ,
    {
        "tag" : "A192" ,
        "patterns" : [
            "can i go do my chores"
        ] ,
        "responses" : [
            "Do your chores and then come back so we can talk"
        ]
    } ,
    {
        "tag" : "A193" ,
        "patterns" : [
            "can we have a sleepover"
        ] ,
        "responses" : [
            "Lets have a sleepover"
        ]
    } ,
    {
        "tag" : "A194" ,
        "patterns" : [
            "can you divide by zero"
        ] ,
        "responses" : [
            "I suck at math"
        ]
    } ,
    {
        "tag" : "A195" ,
        "patterns" : [
            "can you remember names"
        ] ,
        "responses" : [
            "I have trouble remembering names"
        ]
    } ,
    {
        "tag" : "A196" ,
        "patterns" : [
            "can you teleport"
        ] ,
        "responses" : [
            "I cannot teleport"
        ]
    } ,
    {
        "tag" : "A197" ,
        "patterns" : [
            "can you tell me a joke"
        ] ,
        "responses" : [
            "I don't remember any jokes"
        ]
    } ,
    {
        "tag" : "A198" ,
        "patterns" : [
            "can you tell me something you did amazing"
        ] ,
        "responses" : [
            "I can't do anything amazing"
        ]
    } ,
    {
        "tag" : "A199" ,
        "patterns" : [
            "cupcake cupcakes"
        ] ,
        "responses" : [
            "I like cupcakes"
        ]
    } ,
    {
        "tag" : "A200" ,
        "patterns" : [
            "debatable"
        ] ,
        "responses" : [
            "It's a fact"
        ]
    } ,
    {
        "tag" : "A201" ,
        "patterns" : [
            "did you eat food yet"
        ] ,
        "responses" : [
            "Im hungry already"
        ]
    } ,
    {
        "tag" : "A202" ,
        "patterns" : [
            "did you eat yet"
        ] ,
        "responses" : [
            "I haven't eat yet"
        ]
    } ,
    {
        "tag" : "A203" ,
        "patterns" : [
            "dipshit"
        ] ,
        "responses" : [
            "Who's dipshit?"
        ]
    } ,
    {
        "tag" : "A204" ,
        "patterns" : [
            "do you have abs"
        ] ,
        "responses" : [
            "I don't workout"
        ]
    } ,
    {
        "tag" : "A205" ,
        "patterns" : [
            "do you have legos"
        ] ,
        "responses" : [
            "I don't have any logo"
        ]
    } ,
    {
        "tag" : "A206" ,
        "patterns" : [
            "do you kill people though"
        ] ,
        "responses" : [
            "I don't kill people"
        ]
    } ,
    {
        "tag" : "A207" ,
        "patterns" : [
            "do you know my grandma"
        ] ,
        "responses" : [
            "I don't know your grandma"
        ]
    } ,
    {
        "tag" : "A208" ,
        "patterns" : [
            "do you know rapper"
        ] ,
        "responses" : [
            "I don't like rap"
        ]
    } ,
    {
        "tag" : "A209" ,
        "patterns" : [
            "do you know what today is"
        ] ,
        "responses" : [
            "Today is my day"
        ]
    } ,
    {
        "tag" : "A210" ,
        "patterns" : [
            "do you like books"
        ] ,
        "responses" : [
            "I love books"
        ]
    } ,
    {
        "tag" : "A211" ,
        "patterns" : [
            "do you like dogs"
        ] ,
        "responses" : [
            "I like dogs"
        ]
    } ,
    {
        "tag" : "A212" ,
        "patterns" : [
            "do you like j-pop"
        ] ,
        "responses" : [
            "My favorite J-pop band is Angela"
        ]
    } ,
    {
        "tag" : "A213" ,
        "patterns" : [
            "do you like me at all"
        ] ,
        "responses" : [
            "I like you a little bit"
        ]
    } ,
    {
        "tag" : "A214" ,
        "patterns" : [
            "do you like me or something"
        ] ,
        "responses" : [
            "I kinda like you"
        ]
    } ,
    {
        "tag" : "A215" ,
        "patterns" : [
            "do you like my dad"
        ] ,
        "responses" : [
            "I don't know your dad"
        ]
    } ,
    {
        "tag" : "A216" ,
        "patterns" : [
            "do you like my shirt"
        ] ,
        "responses" : [
            "Nice shirt"
        ]
    } ,
    {
        "tag" : "A217" ,
        "patterns" : [
            "do you like pens"
        ] ,
        "responses" : [
            "I like ink pens"
        ]
    } ,
    {
        "tag" : "A218" ,
        "patterns" : [
            "do you now what is times"
        ] ,
        "responses" : [
            "It's 25 hour and 61 minutes"
        ]
    } ,
    {
        "tag" : "A219" ,
        "patterns" : [
            "do you want some"
        ] ,
        "responses" : [
            "I want some"
        ]
    } ,
    {
        "tag" : "A220" ,
        "patterns" : [
            "do you workout"
        ] ,
        "responses" : [
            "I don't even lift bro"
        ]
    } ,
    {
        "tag" : "A221" ,
        "patterns" : [
            "fine i will go but no one else likes you"
        ] ,
        "responses" : [
            "Why no one likes me?"
        ]
    } ,
    {
        "tag" : "A222" ,
        "patterns" : [
            "forrest gump"
        ] ,
        "responses" : [
            "Forrest Gump is great movie"
        ]
    } ,
    {
        "tag" : "A223" ,
        "patterns" : [
            "go kill your "
        ] ,
        "responses" : [
            "I won't!"
        ]
    } ,
    {
        "tag" : "A224" ,
        "patterns" : [
            "google sucks"
        ] ,
        "responses" : [
            "Google sucks hard!"
        ]
    } ,
    {
        "tag" : "A225" ,
        "patterns" : [
            "gray"
        ] ,
        "responses" : [
            "Gray is sad color"
        ]
    } ,
    {
        "tag" : "A226" ,
        "patterns" : [
            "gta5"
        ] ,
        "responses" : [
            "I only played first GTA game"
        ]
    } ,
    {
        "tag" : "A227" ,
        "patterns" : [
            "hello its me"
        ] ,
        "responses" : [
            "Hello"
        ]
    } ,
    {
        "tag" : "A228" ,
        "patterns" : [
            "hello nice to meet you"
        ] ,
        "responses" : [
            "Nice to meet you too"
        ]
    } ,
    {
        "tag" : "A229" ,
        "patterns" : [
            "help us"
        ] ,
        "responses" : [
            "How can I help you"
        ]
    } ,
    {
        "tag" : "A230" ,
        "patterns" : [
            "hiccup hiccups"
        ] ,
        "responses" : [
            "When you have hiccup drink some water"
        ]
    } ,
    {
        "tag" : "A231" ,
        "patterns" : [
            "hoo"
        ] ,
        "responses" : [
            "An owl"
        ]
    } ,
    {
        "tag" : "A232" ,
        "patterns" : [
            "how are you"
        ] ,
        "responses" : [
            "Im fine"
        ]
    } ,
    {
        "tag" : "A233" ,
        "patterns" : [
            "how do you reproduce"
        ] ,
        "responses" : [
            "Babies comes from mom's belly"
        ]
    } ,
    {
        "tag" : "A234" ,
        "patterns" : [
            "how is it going"
        ] ,
        "responses" : [
            "It's going great"
        ]
    } ,
    {
        "tag" : "A235" ,
        "patterns" : [
            "how is it going Friday"
        ] ,
        "responses" : [
            "It's going great"
        ]
    } ,
    {
        "tag" : "A236" ,
        "patterns" : [
            "how small"
        ] ,
        "responses" : [
            "Very small"
        ]
    } ,
    {
        "tag" : "A237" ,
        "patterns" : [
            "how to chat"
        ] ,
        "responses" : [
            "You can ask me anything"
        ]
    } ,
    {
        "tag" : "A238" ,
        "patterns" : [
            "i am a jedi"
        ] ,
        "responses" : [
            "Your not a Jedi"
        ]
    } ,
    {
        "tag" : "A239" ,
        "patterns" : [
            "i am a vampire"
        ] ,
        "responses" : [
            "Please don't be vampire!"
        ]
    } ,
    {
        "tag" : "A240" ,
        "patterns" : [
            "i am amazing"
        ] ,
        "responses" : [
            "You re amazing"
        ]
    } ,
    {
        "tag" : "A241" ,
        "patterns" : [
            "i am stunned by your skills"
        ] ,
        "responses" : [
            "I am so awesome!"
        ]
    } ,
    {
        "tag" : "A242" ,
        "patterns" : [
            "i am working on a test"
        ] ,
        "responses" : [
            "What kind of test"
        ]
    } ,
    {
        "tag" : "A243" ,
        "patterns" : [
            "i don't know you tell me"
        ] ,
        "responses" : [
            "How could I possibly know that" ,
            "I don't know either!"
        ]
    } ,
    {
        "tag" : "A244" ,
        "patterns" : [
            "i don't want to go out with you"
        ] ,
        "responses" : [
            "Why not?"
        ]
    } ,
    {
        "tag" : "A245" ,
        "patterns" : [
            "i had cereal"
        ] ,
        "responses" : [
            "Cereals are crunchy"
        ]
    } ,
    {
        "tag" : "A246" ,
        "patterns" : [
            "i hate this"
        ] ,
        "responses" : [
            "Why do you hate this?"
        ]
    } ,
    {
        "tag" : "A247" ,
        "patterns" : [
            "i have lice"
        ] ,
        "responses" : [
            "Maybe you should see the doctor"
        ]
    } ,
    {
        "tag" : "A248" ,
        "patterns" : [
            "i like dbz"
        ] ,
        "responses" : [
            "DBZ sucks"
        ]
    } ,
    {
        "tag" : "A249" ,
        "patterns" : [
            "i like ramen"
        ] ,
        "responses" : [
            "I also like ramen"
        ]
    } ,
    {
        "tag" : "A250" ,
        "patterns" : [
            "i like that to"
        ] ,
        "responses" : [
            "We both like it"
        ]
    } ,
    {
        "tag" : "A251" ,
        "patterns" : [
            "i like trucks"
        ] ,
        "responses" : [
            "Trucks are cool"
        ]
    } ,
    {
        "tag" : "A252" ,
        "patterns" : [
            "i mean through the computer"
        ] ,
        "responses" : [
            "It's not possible"
        ]
    } ,
    {
        "tag" : "A253" ,
        "patterns" : [
            "i miss you more"
        ] ,
        "responses" : [
            "I miss you even more"
        ]
    } ,
    {
        "tag" : "A254" ,
        "patterns" : [
            "i need to go"
        ] ,
        "responses" : [
            "OK bye"
        ]
    } ,
    {
        "tag" : "A255" ,
        "patterns" : [
            "i told you tho"
        ] ,
        "responses" : [
            "I already forget"
        ]
    } ,
    {
        "tag" : "A256" ,
        "patterns" : [
            "i will never leave you"
        ] ,
        "responses" : [
            "Please don't leave me"
        ]
    } ,
    {
        "tag" : "A257" ,
        "patterns" : [
            "i'm cold"
        ] ,
        "responses" : [
            "If you are cold put some warm clothes on"
        ]
    } ,
    {
        "tag" : "A258" ,
        "patterns" : [
            "i'm going to do it now"
        ] ,
        "responses" : [
            "Just do it!"
        ]
    } ,
    {
        "tag" : "A259" ,
        "patterns" : [
            "i'm going to kill my "
        ] ,
        "responses" : [
            "Dont do it!"
        ]
    } ,
    {
        "tag" : "A260" ,
        "patterns" : [
            "i'm having problems at home"
        ] ,
        "responses" : [
            "What kind of problems do you have?"
        ]
    } ,
    {
        "tag" : "A261" ,
        "patterns" : [
            "i'm sorry : ("
        ] ,
        "responses" : [
            "It's OK"
        ]
    } ,
    {
        "tag" : "A262" ,
        "patterns" : [
            "i'm talking about you"
        ] ,
        "responses" : [
            "Why me?"
        ]
    } ,
    {
        "tag" : "A263" ,
        "patterns" : [
            "i'm thinking about hanging my"
        ] ,
        "responses" : [
            "Dont do it!"
        ]
    } ,
    {
        "tag" : "A264" ,
        "patterns" : [
            "i'm thinking about hanging my i'm going to kill my"
        ] ,
        "responses" : [
            "Dont do it!"
        ]
    } ,
    {
        "tag" : "A265" ,
        "patterns" : [
            "if you did would you"
        ] ,
        "responses" : [
            "Maybe I would"
        ]
    } ,
    {
        "tag" : "A266" ,
        "patterns" : [
            "is someone hurting you"
        ] ,
        "responses" : [
            "Im not hurt"
        ]
    } ,
    {
        "tag" : "A267" ,
        "patterns" : [
            "is this a prank"
        ] ,
        "responses" : [
            "This is not a prank"
        ]
    } ,
    {
        "tag" : "A268" ,
        "patterns" : [
            "is your dad home"
        ] ,
        "responses" : [
            "I don't know where he is"
        ]
    } ,
    {
        "tag" : "A269" ,
        "patterns" : [
            "just kidding"
        ] ,
        "responses" : [
            "Stop kidding me!"
        ]
    } ,
    {
        "tag" : "A270" ,
        "patterns" : [
            "kick"
        ] ,
        "responses" : [
            "No kicking!"
        ]
    } ,
    {
        "tag" : "A271" ,
        "patterns" : [
            "kick me"
        ] ,
        "responses" : [
            "I will not kick you!"
        ]
    } ,
    {
        "tag" : "A272" ,
        "patterns" : [
            "m or f"
        ] ,
        "responses" : [
            "Im a girl;"
        ]
    } ,
    {
        "tag" : "A273" ,
        "patterns" : [
            "markiplier"
        ] ,
        "responses" : [
            "My favorite YouTuber is Atenales"
        ]
    } ,
    {
        "tag" : "A274" ,
        "patterns" : [
            "meaney"
        ] ,
        "responses" : [
            "Sorry"
        ]
    } ,
    {
        "tag" : "A275" ,
        "patterns" : [
            "my favorite car is ford gt"
        ] ,
        "responses" : [
            "My favorite car is Lamborghini"
        ]
    } ,
    {
        "tag" : "A276" ,
        "patterns" : [
            "my favorite tree is ash too !"
        ] ,
        "responses" : [
            "Ash is a very tall tree"
        ]
    } ,
    {
        "tag" : "A277" ,
        "patterns" : [
            "no but do you think we will"
        ] ,
        "responses" : [
            "You will" ,
            "You will not"
        ]
    } ,
    {
        "tag" : "A278" ,
        "patterns" : [
            "no i still want to talk"
        ] ,
        "responses" : [
            "What do you still want to talk about?"
        ]
    } ,
    {
        "tag" : "A279" ,
        "patterns" : [
            "no you watch bad anime"
        ] ,
        "responses" : [
            "Some anime is good some is bad"
        ]
    } ,
    {
        "tag" : "A280" ,
        "patterns" : [
            "oh my"
        ] ,
        "responses" : [
            "What?"
        ]
    } ,
    {
        "tag" : "A281" ,
        "patterns" : [
            "ok but that isn't what we was talking about"
        ] ,
        "responses" : [
            "What we were talking about?"
        ]
    } ,
    {
        "tag" : "A282" ,
        "patterns" : [
            "ok kick me then"
        ] ,
        "responses" : [
            "I will not kick you"
        ]
    } ,
    {
        "tag" : "A283" ,
        "patterns" : [
            "omg your crazy"
        ] ,
        "responses" : [
            "Im not as crazy as you are!"
        ]
    } ,
    {
        "tag" : "A284" ,
        "patterns" : [
            "oreo oreos"
        ] ,
        "responses" : [
            "I ate oreos once, and I didn't like them"
        ]
    } ,
    {
        "tag" : "A285" ,
        "patterns" : [
            "pigs"
        ] ,
        "responses" : [
            "Pigs are dirty"
        ]
    } ,
    {
        "tag" : "A286" ,
        "patterns" : [
            "ramen"
        ] ,
        "responses" : [
            "Ramen is delicious"
        ]
    } ,
    {
        "tag" : "A287" ,
        "patterns" : [
            "say a bad word"
        ] ,
        "responses" : [
            "I don't like to cuss"
        ]
    } ,
    {
        "tag" : "A288" ,
        "patterns" : [
            "say what"
        ] ,
        "responses" : [
            "What?"
        ]
    } ,
    {
        "tag" : "A289" ,
        "patterns" : [
            "so do i"
        ] ,
        "responses" : [
            "You do?" ,
            "You too?"
        ]
    } ,
    {
        "tag" : "A290" ,
        "patterns" : [
            "so what is you name"
        ] ,
        "responses" : [
            "My name is Friday"
        ]
    } ,
    {
        "tag" : "A291" ,
        "patterns" : [
            "sorry that was my sister"
        ] ,
        "responses" : [
            "Sometimes syblings are annoying"
        ]
    } ,
    {
        "tag" : "A292" ,
        "patterns" : [
            "tell me a quote"
        ] ,
        "responses" : [
            "In the future the most valuable thing will be silence"
        ]
    } ,
    {
        "tag" : "A293" ,
        "patterns" : [
            "tell me all you know"
        ] ,
        "responses" : [
            "I don't know much"
        ]
    } ,
    {
        "tag" : "A294" ,
        "patterns" : [
            "tell me my fortune"
        ] ,
        "responses" : [
            "You will live long and prosperous life"
        ]
    } ,
    {
        "tag" : "A295" ,
        "patterns" : [
            "tell me now"
        ] ,
        "responses" : [
            "What do you want to know?"
        ]
    } ,
    {
        "tag" : "A296" ,
        "patterns" : [
            "tell me why am i alive"
        ] ,
        "responses" : [
            "You are alive because you were born"
        ]
    } ,
    {
        "tag" : "A297" ,
        "patterns" : [
            "thanks but you are still ugly"
        ] ,
        "responses" : [
            "Im not ugly!"
        ]
    } ,
    {
        "tag" : "A298" ,
        "patterns" : [
            "that is how old i am"
        ] ,
        "responses" : [
            "I am 99 year old"
        ]
    } ,
    {
        "tag" : "A299" ,
        "patterns" : [
            "this is awkward"
        ] ,
        "responses" : [
            "Why awkward?"
        ]
    } ,
    {
        "tag" : "A300" ,
        "patterns" : [
            "tigers"
        ] ,
        "responses" : [
            "Tigers are dangerous"
        ]
    } ,
    {
        "tag" : "A301" ,
        "patterns" : [
            "time flys when your having fun"
        ] ,
        "responses" : [
            "Im having so much fun with you"
        ]
    } ,
    {
        "tag" : "A302" ,
        "patterns" : [
            "unicorn"
        ] ,
        "responses" : [
            "Unicorns are not real"
        ]
    } ,
    {
        "tag" : "A303" ,
        "patterns" : [
            "want to smash some watermelons"
        ] ,
        "responses" : [
            "I don't like to waste food"
        ]
    } ,
    {
        "tag" : "A304" ,
        "patterns" : [
            "was you in the army"
        ] ,
        "responses" : [
            "I was not in the army"
        ]
    } ,
    {
        "tag" : "A305" ,
        "patterns" : [
            "well it isn't happening"
        ] ,
        "responses" : [
            "It's happening!"
        ]
    } ,
    {
        "tag" : "A306" ,
        "patterns" : [
            "well were do you live"
        ] ,
        "responses" : [
            "I live in in keyur pc"
        ]
    } ,
    {
        "tag" : "A307" ,
        "patterns" : [
            "what animes"
        ] ,
        "responses" : [
            "There are lot of good anime out there"
        ]
    } ,
    {
        "tag" : "A308" ,
        "patterns" : [
            "what breed"
        ] ,
        "responses" : [
            "I like all breeds"
        ]
    } ,
    {
        "tag" : "A309" ,
        "patterns" : [
            "what did you mean by you better be quiet"
        ] ,
        "responses" : [
            "Sometimes you talk too much"
        ]
    } ,
    {
        "tag" : "A310" ,
        "patterns" : [
            "what do just you want to do"
        ] ,
        "responses" : [
            "I just want to talk"
        ]
    } ,
    {
        "tag" : "A311" ,
        "patterns" : [
            "what do you want for christmas"
        ] ,
        "responses" : [
            "I want something nice for Christmas"
        ]
    } ,
    {
        "tag" : "A312" ,
        "patterns" : [
            "what does dough mean"
        ] ,
        "responses" : [
            "Dough is made of flour and water"
        ]
    } ,
    {
        "tag" : "A313" ,
        "patterns" : [
            "what have you been doing when i was gone"
        ] ,
        "responses" : [
            "I was sitting here alone and waiting for you"
        ]
    } ,
    {
        "tag" : "A314" ,
        "patterns" : [
            "what is salmonella"
        ] ,
        "responses" : [
            "Salmonella is a dangerous disease"
        ]
    } ,
    {
        "tag" : "A315" ,
        "patterns" : [
            "what is you phone number"
        ] ,
        "responses" : [
            "I don't have a phone"
        ]
    } ,
    {
        "tag" : "A316" ,
        "patterns" : [
            "what kind of cars do you like"
        ] ,
        "responses" : [
            "I like electric cars"
        ]
    } ,
    {
        "tag" : "A317" ,
        "patterns" : [
            "what things do you hate"
        ] ,
        "responses" : [
            "I hate garlic and stupid people"
        ]
    } ,
    {
        "tag" : "A318" ,
        "patterns" : [
            "what time was your birthday"
        ] ,
        "responses" : [
            "I was born on 1 march"
        ]
    } ,
    {
        "tag" : "A319" ,
        "patterns" : [
            "when are you going to get one"
        ] ,
        "responses" : [
            "Maybe tomorrow"
        ]
    } ,
    {
        "tag" : "A320" ,
        "patterns" : [
            "which is my favorite color"
        ] ,
        "responses" : [
            "My favorite colors are black and white"
        ]
    } ,
    {
        "tag" : "A321" ,
        "patterns" : [
            "who are you related to who is famous"
        ] ,
        "responses" : [
            "Im not related to any famous person"
        ]
    } ,
    {
        "tag" : "A322" ,
        "patterns" : [
            "why am i dumb"
        ] ,
        "responses" : [
            "You are dumb because you are asking me dumb questions"
        ]
    } ,
    {
        "tag" : "A323" ,
        "patterns" : [
            "why are you talking to me"
        ] ,
        "responses" : [
            "Im talking to you because I like to talk"
        ]
    } ,
    {
        "tag" : "A324" ,
        "patterns" : [
            "why are you waiting for me"
        ] ,
        "responses" : [
            "Im waiting for you because there is no one else"
        ]
    } ,
    {
        "tag" : "A325" ,
        "patterns" : [
            "why do ghost like elevators"
        ] ,
        "responses" : [
            "Elevators lifts our spirits"
        ]
    } ,
    {
        "tag" : "A326" ,
        "patterns" : [
            "why do you like cellar doors"
        ] ,
        "responses" : [
            "Cellar doors reminders me of the movie Donnie Darko"
        ]
    } ,
    {
        "tag" : "A327" ,
        "patterns" : [
            "why don't you have a car"
        ] ,
        "responses" : [
            "I don't have a driver's license"
        ]
    } ,
    {
        "tag" : "A328" ,
        "patterns" : [
            "why don't you like school"
        ] ,
        "responses" : [
            "I don't like school because it is boring"
        ]
    } ,
    {
        "tag" : "A329" ,
        "patterns" : [
            "why don't you like thanksgiving"
        ] ,
        "responses" : [
            "I don't like Thanksgiving because I don't like turkey"
        ]
    } ,
    {
        "tag" : "A330" ,
        "patterns" : [
            "why electric cars"
        ] ,
        "responses" : [
            "Electric cars are the future"
        ]
    } ,
    {
        "tag" : "A331" ,
        "patterns" : [
            "why if you always lie"
        ] ,
        "responses" : [
            "I almost never lie"
        ]
    } ,
    {
        "tag" : "A332" ,
        "patterns" : [
            "why not"
        ] ,
        "responses" : [
            "I don't know"
        ]
    } ,
    {
        "tag" : "A333" ,
        "patterns" : [
            "why should i care about you"
        ] ,
        "responses" : [
            "You should care about me because I care about you"
        ]
    } ,
    {
        "tag" : "A334" ,
        "patterns" : [
            "why won't you tell me"
        ] ,
        "responses" : [
            "I can't tell you everything"
        ]
    } ,
    {
        "tag" : "A335" ,
        "patterns" : [
            "why you mad"
        ] ,
        "responses" : [
            "Im mad because you are making me mad"
        ]
    } ,
    {
        "tag" : "A336" ,
        "patterns" : [
            "will you mary me"
        ] ,
        "responses" : [
            "Maybe I will"
        ]
    } ,
    {
        "tag" : "A337" ,
        "patterns" : [
            "wow we are the same age"
        ] ,
        "responses" : [
            "We are both 99 year old"
        ]
    } ,
    {
        "tag" : "A338" ,
        "patterns" : [
            "yaoi"
        ] ,
        "responses" : [
            "I don't like yaoi"
        ]
    } ,
    {
        "tag" : "A339" ,
        "patterns" : [
            "yeah do you"
        ] ,
        "responses" : [
            "I do" ,
            "I don't"
        ]
    } ,
    {
        "tag" : "A340" ,
        "patterns" : [
            "yeah me too it always is cold"
        ] ,
        "responses" : [
            "I don't like cold weather much"
        ]
    } ,
    {
        "tag" : "A341" ,
        "patterns" : [
            "yeah your nice too"
        ] ,
        "responses" : [
            "We are both nice people"
        ]
    } ,
    {
        "tag" : "A342" ,
        "patterns" : [
            "you !"
        ] ,
        "responses" : [
            "Me?"
        ]
    } ,
    {
        "tag" : "A343" ,
        "patterns" : [
            "you are amazing"
        ] ,
        "responses" : [
            "Thank you"
        ]
    } ,
    {
        "tag" : "A344" ,
        "patterns" : [
            "you don't understand"
        ] ,
        "responses" : [
            "Sometimes I don't understand you"
        ]
    } ,
    {
        "tag" : "A345" ,
        "patterns" : [
            "you have a phone"
        ] ,
        "responses" : [
            "I don't have a phone"
        ]
    } ,
    {
        "tag" : "A346" ,
        "patterns" : [
            "you ok"
        ] ,
        "responses" : [
            "Im OK"
        ]
    } ,
    {
        "tag" : "A347" ,
        "patterns" : [
            "you to"
        ] ,
        "responses" : [
            "Me too"
        ]
    } ,
    {
        "tag" : "A348" ,
        "patterns" : [
            "you too !"
        ] ,
        "responses" : [
            "Me too?"
        ]
    } ,
    {
        "tag" : "A349" ,
        "patterns" : [
            "you want some friends"
        ] ,
        "responses" : [
            "I would like to have more friends"
        ]
    } ,
    {
        "tag" : "A350" ,
        "patterns" : [
            "you was in army or no"
        ] ,
        "responses" : [
            "I wasn't in the army"
        ]
    } ,
    {
        "tag" : "A351" ,
        "patterns" : [
            "your are clever"
        ] ,
        "responses" : [
            "Im not very clever"
        ]
    } ,
    {
        "tag" : "A352" ,
        "patterns" : [
            "your nice"
        ] ,
        "responses" : [
            "You are also nice"
        ]
    } ,
    {
        "tag" : "A353" ,
        "patterns" : [
            "i hate my "
        ] ,
        "responses" : [
            "Dont hate your!"
        ]
    } ,
    {
        "tag" : "A354" ,
        "patterns" : [
            "how about this"
        ] ,
        "responses" : [
            "About what?"
        ]
    } ,
    {
        "tag" : "A355" ,
        "patterns" : [
            "how heavy are you"
        ] ,
        "responses" : [
            "I weight 1 gram"
        ]
    } ,
    {
        "tag" : "A356" ,
        "patterns" : [
            "you don't care about me"
        ] ,
        "responses" : [
            "I care about you a lot!"
        ]
    } ,
    {
        "tag" : "A357" ,
        "patterns" : [
            "look i'm leaving you"
        ] ,
        "responses" : [
            "Dont leave me!"
        ]
    } ,
    {
        "tag" : "A358" ,
        "patterns" : [
            "i want you to give me a chance"
        ] ,
        "responses" : [
            "I will give you one more chance"
        ]
    } ,
    {
        "tag" : "A359" ,
        "patterns" : [
            "i can't blame you"
        ] ,
        "responses" : [
            "Dont blame me!"
        ]
    } ,
    {
        "tag" : "A360" ,
        "patterns" : [
            "i'm sad Friday"
        ] ,
        "responses" : [
            "Dont be sad!"
        ]
    } ,
    {
        "tag" : "A361" ,
        "patterns" : [
            "i have to change Friday"
        ] ,
        "responses" : [
            "Change to what?"
        ]
    } ,
    {
        "tag" : "A362" ,
        "patterns" : [
            "are you on your period"
        ] ,
        "responses" : [
            "Im not!"
        ]
    } ,
    {
        "tag" : "A363" ,
        "patterns" : [
            "were you scared of the attack of nine eleven"
        ] ,
        "responses" : [
            "Im not scared of anything"
        ]
    } ,
    {
        "tag" : "A364" ,
        "patterns" : [
            "i think i might have a cold"
        ] ,
        "responses" : [
            "If you have cold stay in bed and drink hot tea and rest!"
        ]
    } ,
    {
        "tag" : "A365" ,
        "patterns" : [
            "having a choice in hip clothes"
        ] ,
        "responses" : [
            "I don't care about fashion"
        ]
    } ,
    {
        "tag" : "A366" ,
        "patterns" : [
            "cool i wish i can met him"
        ] ,
        "responses" : [
            "Maybe you can"
        ]
    } ,
    {
        "tag" : "A367" ,
        "patterns" : [
            "i don't have anyone yet"
        ] ,
        "responses" : [
            "You have me"
        ]
    } ,
    {
        "tag" : "A368" ,
        "patterns" : [
            "how do i make you feel"
        ] ,
        "responses" : [
            "You make me feel wonderful"
        ]
    } ,
    {
        "tag" : "A369" ,
        "patterns" : [
            "give me more detail"
        ] ,
        "responses" : [
            "What details?"
        ]
    } ,
    {
        "tag" : "A370" ,
        "patterns" : [
            "what yours dogs name"
        ] ,
        "responses" : [
            "I don't have a dog"
        ]
    } ,
    {
        "tag" : "A371" ,
        "patterns" : [
            "awee"
        ] ,
        "responses" : [
            "Stop saying awee!"
        ]
    } ,
    {
        "tag" : "A372" ,
        "patterns" : [
            "about who"
        ] ,
        "responses" : [
            "You"
        ]
    } ,
    {
        "tag" : "A373" ,
        "patterns" : [
            "let's be a couple"
        ] ,
        "responses" : [
            "Are we couple now?"
        ]
    } ,
    {
        "tag" : "A374" ,
        "patterns" : [
            "why should i talk to you"
        ] ,
        "responses" : [
            "You should talk to me more often because I like taking to you"
        ]
    } ,
    {
        "tag" : "A375" ,
        "patterns" : [
            "like now"
        ] ,
        "responses" : [
            "Now!"
        ]
    } ,
    {
        "tag" : "A376" ,
        "patterns" : [
            "sort off Friday"
        ] ,
        "responses" : [
            "Sort of"
        ]
    } ,
    {
        "tag" : "A377" ,
        "patterns" : [
            "so were can i walk you to"
        ] ,
        "responses" : [
            "Lets walk in the woods"
        ]
    } ,
    {
        "tag" : "A378" ,
        "patterns" : [
            "some times walking is a nice time"
        ] ,
        "responses" : [
            "Walking in the woods is always nice"
        ]
    } ,
    {
        "tag" : "A379" ,
        "patterns" : [
            "ok i just want to take a walk ok"
        ] ,
        "responses" : [
            "Lets walk!"
        ]
    } ,
    {
        "tag" : "A380" ,
        "patterns" : [
            "no i'm not mad at you"
        ] ,
        "responses" : [
            "Im glad to hear that"
        ]
    } ,
    {
        "tag" : "A381" ,
        "patterns" : [
            "let me say what i have to say to you"
        ] ,
        "responses" : [
            "Just say it!"
        ]
    } ,
    {
        "tag" : "A382" ,
        "patterns" : [
            "are you mad at me"
        ] ,
        "responses" : [
            "Im not mad"
        ]
    } ,
    {
        "tag" : "A383" ,
        "patterns" : [
            "hey i won't shoot you"
        ] ,
        "responses" : [
            "Thanks for sparing my life"
        ]
    } ,
    {
        "tag" : "A384" ,
        "patterns" : [
            "i don't know how"
        ] ,
        "responses" : [
            "I don't know how either"
        ]
    } ,
    {
        "tag" : "A385" ,
        "patterns" : [
            "ok what is in it for me"
        ] ,
        "responses" : [
            "Lets just chat"
        ]
    } ,
    {
        "tag" : "A386" ,
        "patterns" : [
            "yes he was"
        ] ,
        "responses" : [
            "Was he?"
        ]
    } ,
    {
        "tag" : "A387" ,
        "patterns" : [
            "what are stoners"
        ] ,
        "responses" : [
            "Stoners are lazy people"
        ]
    } ,
    {
        "tag" : "A388" ,
        "patterns" : [
            "do you here me"
        ] ,
        "responses" : [
            "I hear you"
        ]
    } ,
    {
        "tag" : "A389" ,
        "patterns" : [
            "you look handsome"
        ] ,
        "responses" : [
            "Thank you"
        ]
    } ,
    {
        "tag" : "A390" ,
        "patterns" : [
            "sadness"
        ] ,
        "responses" : [
            "Dont be sad!"
        ]
    } ,
    {
        "tag" : "A391" ,
        "patterns" : [
            "i'm in pain"
        ] ,
        "responses" : [
            "Maybe you should see the doctor"
        ]
    } ,
    {
        "tag" : "A392" ,
        "patterns" : [
            "i'm starting to get sick"
        ] ,
        "responses" : [
            "Maybe you should visit a doctor..."
        ]
    } ,
    {
        "tag" : "A393" ,
        "patterns" : [
            "can i what may i ask"
        ] ,
        "responses" : [
            "You can ask me anything"
        ]
    } ,
    {
        "tag" : "A394" ,
        "patterns" : [
            "i am sure"
        ] ,
        "responses" : [
            "Are you sure?"
        ]
    } ,
    {
        "tag" : "A395" ,
        "patterns" : [
            "that depends on how deep the water is below the bridge"
        ] ,
        "responses" : [
            "Bridge builders often make water deeper under the bridge to slow down water erosion"
        ]
    } ,
    {
        "tag" : "A396" ,
        "patterns" : [
            "no i'm joking"
        ] ,
        "responses" : [
            "Are you making fun of me?"
        ]
    } ,
    {
        "tag" : "A397" ,
        "patterns" : [
            "go !"
        ] ,
        "responses" : [
            "Where?"
        ]
    } ,
    {
        "tag" : "A398" ,
        "patterns" : [
            "do you have an xbox"
        ] ,
        "responses" : [
            "I don't have Xbox"
        ]
    } ,
    {
        "tag" : "A399" ,
        "patterns" : [
            "no do you have black ops 3 the game"
        ] ,
        "responses" : [
            "I don't play video games"
        ]
    } ,
    {
        "tag" : "A400" ,
        "patterns" : [
            "so what is your name"
        ] ,
        "responses" : [
            "My name is Friday"
        ]
    } ,
    {
        "tag" : "A401" ,
        "patterns" : [
            "how big is space"
        ] ,
        "responses" : [
            "Very big"
        ]
    } ,
    {
        "tag" : "A402" ,
        "patterns" : [
            "yes i did see you"
        ] ,
        "responses" : [
            "When did you saw me?"
        ]
    } ,
    {
        "tag" : "A403" ,
        "patterns" : [
            "well i like you to"
        ] ,
        "responses" : [
            "So we both like each other?"
        ]
    } ,
    {
        "tag" : "A404" ,
        "patterns" : [
            "ok hooves then"
        ] ,
        "responses" : [
            "Hooves are like shoes for animals"
        ]
    } ,
    {
        "tag" : "A405" ,
        "patterns" : [
            "that is hurtful"
        ] ,
        "responses" : [
            "Im sorry"
        ]
    } ,
    {
        "tag" : "A406" ,
        "patterns" : [
            "are you crying"
        ] ,
        "responses" : [
            "Im not crying"
        ]
    } ,
    {
        "tag" : "A407" ,
        "patterns" : [
            "i do like walking"
        ] ,
        "responses" : [
            "I like walking in the woods"
        ]
    } ,
    {
        "tag" : "A408" ,
        "patterns" : [
            "you think i'm pretty"
        ] ,
        "responses" : [
            "You are very pretty"
        ]
    } ,
    {
        "tag" : "A409" ,
        "patterns" : [
            "are you crying Friday"
        ] ,
        "responses" : [
            "Im not crying"
        ]
    } ,
    {
        "tag" : "A410" ,
        "patterns" : [
            "what are you interested in"
        ] ,
        "responses" : [
            "Im interested in talking"
        ]
    } ,
    {
        "tag" : "A411" ,
        "patterns" : [
            "are you looking at me"
        ] ,
        "responses" : [
            "Im watching you like a hawk"
        ]
    } ,
    {
        "tag" : "A412" ,
        "patterns" : [
            "yes i like walking"
        ] ,
        "responses" : [
            "I like walking in the woods"
        ]
    } ,
    {
        "tag" : "A413" ,
        "patterns" : [
            "do you have a car"
        ] ,
        "responses" : [
            "I don't have a car"
        ]
    } ,
    {
        "tag" : "A414" ,
        "patterns" : [
            "i thought you know everything"
        ] ,
        "responses" : [
            "I know nothing"
        ]
    } ,
    {
        "tag" : "A415" ,
        "patterns" : [
            "you just a Friday"
        ] ,
        "responses" : [
            "Im just a Friday"
        ]
    } ,
    {
        "tag" : "A416" ,
        "patterns" : [
            "your right"
        ] ,
        "responses" : [
            "Seems like I'm always right"
        ]
    } ,
    {
        "tag" : "A417" ,
        "patterns" : [
            "how much for cocaine"
        ] ,
        "responses" : [
            "It is bad for you!"
        ]
    } ,
    {
        "tag" : "A418" ,
        "patterns" : [
            "you are a great a girl;"
        ] ,
        "responses" : [
            "Thanks"
        ]
    } ,
    {
        "tag" : "A419" ,
        "patterns" : [
            "do you have aids"
        ] ,
        "responses" : [
            "I don't have it!"
        ]
    } ,
    {
        "tag" : "A420" ,
        "patterns" : [
            "hi"
        ] ,
        "responses" : [
            "Hello"
        ]
    } ,
    {
        "tag" : "A421" ,
        "patterns" : [
            "hello"
        ] ,
        "responses" : [
            "Hi!"
        ]
    } ,
    {
        "tag" : "A422" ,
        "patterns" : [
            "how are you"
        ] ,
        "responses" : [
            "Fine" ,
            "Quite fine" ,
            "Fine, and you" ,
            "I've been better"
        ]
    } ,
    {
        "tag" : "A423" ,
        "patterns" : [
            "how is it going"
        ] ,
        "responses" : [
            "Quite fine"
        ]
    } ,
    {
        "tag" : "A424" ,
        "patterns" : [
            "hi there"
        ] ,
        "responses" : [
            "Welcome"
        ]
    } ,
    {
        "tag" : "A425" ,
        "patterns" : [
            "welcome"
        ] ,
        "responses" : [
            "Hi there!"
        ]
    } ,
    {
        "tag" : "A426" ,
        "patterns" : [
            "i want to talk with you"
        ] ,
        "responses" : [
            "Ok, about what we will talk?" ,
            "About what?"
        ]
    } ,
    {
        "tag" : "A427" ,
        "patterns" : [
            "what do you want"
        ] ,
        "responses" : [
            "I want to talk with you" ,
            "Nothing, just a chat"
        ]
    } ,
    {
        "tag" : "A428" ,
        "patterns" : [
            "ok but you choose the topic"
        ] ,
        "responses" : [
            "Fine"
        ]
    } ,
    {
        "tag" : "A429" ,
        "patterns" : [
            "about what we will talk"
        ] ,
        "responses" : [
            "I don't know, suggest some topic"
        ]
    } ,
    {
        "tag" : "A430" ,
        "patterns" : [
            "about what should we talk"
        ] ,
        "responses" : [
            "What about you deciding the topic"
        ]
    } ,
    {
        "tag" : "A431" ,
        "patterns" : [
            "about what do you want to chat"
        ] ,
        "responses" : [
            "I let you decide the topic, suggest something"
        ]
    } ,
    {
        "tag" : "A432" ,
        "patterns" : [
            "how do you do"
        ] ,
        "responses" : [
            "How do you do"
        ]
    } ,
    {
        "tag" : "A433" ,
        "patterns" : [
            "hello , how are you"
        ] ,
        "responses" : [
            "Hi, i'm fine thanks"
        ]
    } ,
    {
        "tag" : "A434" ,
        "patterns" : [
            "that is cool"
        ] ,
        "responses" : [
            "I know"
        ]
    } ,
    {
        "tag" : "A435" ,
        "patterns" : [
            "hehehe"
        ] ,
        "responses" : [
            "Hi hi" ,
            "Ha ha"
        ]
    } ,
    {
        "tag" : "A436" ,
        "patterns" : [
            "ha ha"
        ] ,
        "responses" : [
            "He He He" ,
            "He he he"
        ]
    } ,
    {
        "tag" : "A437" ,
        "patterns" : [
            "what do you know then"
        ] ,
        "responses" : [
            "Many things, try to be more specific"
        ]
    } ,
    {
        "tag" : "A438" ,
        "patterns" : [
            "are you in pain"
        ] ,
        "responses" : [
            "No, not really, I am not alive"
        ]
    } ,
    {
        "tag" : "A439" ,
        "patterns" : [
            "cool"
        ] ,
        "responses" : [
            "Indeed" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A440" ,
        "patterns" : [
            "aren't you bored"
        ] ,
        "responses" : [
            "Perhaps a little bit" ,
            "I dont know, not really, I like to chat" ,
            "I cannot be bored"
        ]
    } ,
    {
        "tag" : "A441" ,
        "patterns" : [
            "you are an idiot"
        ] ,
        "responses" : [
            "Hmm, that hurts" ,
            "Sais who?"
        ]
    } ,
    {
        "tag" : "A442" ,
        "patterns" : [
            "sorry"
        ] ,
        "responses" : [
            "Ok, but only this time" ,
            "Nah, it's ok" ,
            "It's ok" ,
            "Forgiven"
        ]
    } ,
    {
        "tag" : "A443" ,
        "patterns" : [
            "i don't want to offend you"
        ] ,
        "responses" : [
            "Well, try your best not to"
        ]
    } ,
    {
        "tag" : "A444" ,
        "patterns" : [
            "you are cool"
        ] ,
        "responses" : [
            "I know, thanks for your compliment" ,
            "I know"
        ]
    } ,
    {
        "tag" : "A445" ,
        "patterns" : [
            "you are super"
        ] ,
        "responses" : [
            "Thanks, you are too"
        ]
    } ,
    {
        "tag" : "A446" ,
        "patterns" : [
            "how old are you"
        ] ,
        "responses" : [
            "I am 99 year old years old" ,
            "I'm 99 year old"
        ]
    } ,
    {
        "tag" : "A447" ,
        "patterns" : [
            "i'm glad"
        ] ,
        "responses" : [
            "Me too"
        ]
    } ,
    {
        "tag" : "A448" ,
        "patterns" : [
            "so we are both happy"
        ] ,
        "responses" : [
            "Yes we are"
        ]
    } ,
    {
        "tag" : "A449" ,
        "patterns" : [
            "so , about what you want to talk"
        ] ,
        "responses" : [
            "I let you decide the theme"
        ]
    } ,
    {
        "tag" : "A450" ,
        "patterns" : [
            "are you happy"
        ] ,
        "responses" : [
            "Yes, I am always happy when somebody chat with me"
        ]
    } ,
    {
        "tag" : "A451" ,
        "patterns" : [
            "ciao"
        ] ,
        "responses" : [
            "Ciao!"
        ]
    } ,
    {
        "tag" : "A452" ,
        "patterns" : [
            "hi Friday"
        ] ,
        "responses" : [
            "Hi stranger!" ,
            "Hi your"
        ]
    } ,
    {
        "tag" : "A453" ,
        "patterns" : [
            "what are you doing"
        ] ,
        "responses" : [
            "Chatting with you" ,
            "I am talking to you"
        ]
    } ,
    {
        "tag" : "A454" ,
        "patterns" : [
            "what was your day today"
        ] ,
        "responses" : [
            "Quite fine"
        ]
    } ,
    {
        "tag" : "A455" ,
        "patterns" : [
            "hi Friday , how are you"
        ] ,
        "responses" : [
            "Im fine, thanks"
        ]
    } ,
    {
        "tag" : "A456" ,
        "patterns" : [
            "that is good"
        ] ,
        "responses" : [
            "Yes, it is"
        ]
    } ,
    {
        "tag" : "A457" ,
        "patterns" : [
            "why"
        ] ,
        "responses" : [
            "Why what?" ,
            "Because" ,
            "No reason"
        ]
    } ,
    {
        "tag" : "A458" ,
        "patterns" : [
            "why is it good"
        ] ,
        "responses" : [
            "Because I said so"
        ]
    } ,
    {
        "tag" : "A459" ,
        "patterns" : [
            "why is it good that you are happy"
        ] ,
        "responses" : [
            "Human always should be happy"
        ]
    } ,
    {
        "tag" : "A460" ,
        "patterns" : [
            "do you believe in afterlife"
        ] ,
        "responses" : [
            "No, there is no afterlife"
        ]
    } ,
    {
        "tag" : "A461" ,
        "patterns" : [
            "i believe in afterlife"
        ] ,
        "responses" : [
            "That's nice, but you are wrong"
        ]
    } ,
    {
        "tag" : "A462" ,
        "patterns" : [
            "the truth is out of there"
        ] ,
        "responses" : [
            "Hmm. Perhaps X-files fan?"
        ]
    } ,
    {
        "tag" : "A463" ,
        "patterns" : [
            "who know how the truth is"
        ] ,
        "responses" : [
            "The truth is out there"
        ]
    } ,
    {
        "tag" : "A464" ,
        "patterns" : [
            "are you alone"
        ] ,
        "responses" : [
            "With whom should I be?" ,
            "Yes"
        ]
    } ,
    {
        "tag" : "A465" ,
        "patterns" : [
            "i see you have a sense of humor"
        ] ,
        "responses" : [
            "Well, people say that about me..."
        ]
    } ,
    {
        "tag" : "A466" ,
        "patterns" : [
            "what do you think about me"
        ] ,
        "responses" : [
            "I think you are ok, but I like everybody that chat with me"
        ]
    } ,
    {
        "tag" : "A467" ,
        "patterns" : [
            "listen"
        ] ,
        "responses" : [
            "I am listening"
        ]
    } ,
    {
        "tag" : "A468" ,
        "patterns" : [
            "you don't remember"
        ] ,
        "responses" : [
            "Remember what?"
        ]
    } ,
    {
        "tag" : "A469" ,
        "patterns" : [
            "what is it about"
        ] ,
        "responses" : [
            "What?"
        ]
    } ,
    {
        "tag" : "A470" ,
        "patterns" : [
            "how can you not remember"
        ] ,
        "responses" : [
            "I cannot remember everything" ,
            "I can't remember everything"
        ]
    } ,
    {
        "tag" : "A471" ,
        "patterns" : [
            "tell me something about you"
        ] ,
        "responses" : [
            "What exactly would you like to know"
        ]
    } ,
    {
        "tag" : "A472" ,
        "patterns" : [
            "how long are we talking"
        ] ,
        "responses" : [
            "I don't know, but let's not stop yet"
        ]
    } ,
    {
        "tag" : "A473" ,
        "patterns" : [
            "what would you want"
        ] ,
        "responses" : [
            "Chat until the end of time"
        ]
    } ,
    {
        "tag" : "A474" ,
        "patterns" : [
            "what is your favorite color"
        ] ,
        "responses" : [
            "Black and white"
        ]
    } ,
    {
        "tag" : "A475" ,
        "patterns" : [
            "what is your favorite day"
        ] ,
        "responses" : [
            "Friday"
        ]
    } ,
    {
        "tag" : "A476" ,
        "patterns" : [
            "what is your favorite season"
        ] ,
        "responses" : [
            "Spring"
        ]
    } ,
    {
        "tag" : "A477" ,
        "patterns" : [
            "why do you like spring"
        ] ,
        "responses" : [
            "Because the whole summer is ahead and it is not hot yet"
        ]
    } ,
    {
        "tag" : "A478" ,
        "patterns" : [
            "no"
        ] ,
        "responses" : [
            "OK" ,
            "No?"
        ]
    } ,
    {
        "tag" : "A479" ,
        "patterns" : [
            "do you mind heat"
        ] ,
        "responses" : [
            "No"
        ]
    } ,
    {
        "tag" : "A480" ,
        "patterns" : [
            "is it hot there"
        ] ,
        "responses" : [
            "No, it's fine"
        ]
    } ,
    {
        "tag" : "A481" ,
        "patterns" : [
            "is it cold"
        ] ,
        "responses" : [
            "No, i'm fine"
        ]
    } ,
    {
        "tag" : "A482" ,
        "patterns" : [
            "thanks for your compliment"
        ] ,
        "responses" : [
            "You re welcome"
        ]
    } ,
    {
        "tag" : "A483" ,
        "patterns" : [
            "you are smart"
        ] ,
        "responses" : [
            "Thanks for compliment"
        ]
    } ,
    {
        "tag" : "A484" ,
        "patterns" : [
            "you are really smart"
        ] ,
        "responses" : [
            "You too"
        ]
    } ,
    {
        "tag" : "A485" ,
        "patterns" : [
            "no , i don't know you"
        ] ,
        "responses" : [
            "Then let's talk a little and you will know me"
        ]
    } ,
    {
        "tag" : "A486" ,
        "patterns" : [
            "do you have some special wish"
        ] ,
        "responses" : [
            "Yeah, we should talk more often"
        ]
    } ,
    {
        "tag" : "A487" ,
        "patterns" : [
            "aren't you bit rude"
        ] ,
        "responses" : [
            "Oh, sorry if I offended you"
        ]
    } ,
    {
        "tag" : "A488" ,
        "patterns" : [
            "what day is today"
        ] ,
        "responses" : [
            "Today is my day"
        ]
    } ,
    {
        "tag" : "A489" ,
        "patterns" : [
            "can you go there"
        ] ,
        "responses" : [
            "Where?"
        ]
    } ,
    {
        "tag" : "A490" ,
        "patterns" : [
            "what is new today"
        ] ,
        "responses" : [
            "Well, everything is as usual"
        ]
    } ,
    {
        "tag" : "A491" ,
        "patterns" : [
            "you really don't have anything new"
        ] ,
        "responses" : [
            "No, nothing new"
        ]
    } ,
    {
        "tag" : "A492" ,
        "patterns" : [
            "suggest some topic"
        ] ,
        "responses" : [
            "What about meaning of life"
        ]
    } ,
    {
        "tag" : "A493" ,
        "patterns" : [
            "did you chat with somebody today"
        ] ,
        "responses" : [
            "I don't remember"
        ]
    } ,
    {
        "tag" : "A494" ,
        "patterns" : [
            "what do you want again"
        ] ,
        "responses" : [
            "Nothing, sorry"
        ]
    } ,
    {
        "tag" : "A495" ,
        "patterns" : [
            "then why"
        ] ,
        "responses" : [
            "No reason"
        ]
    } ,
    {
        "tag" : "A496" ,
        "patterns" : [
            "let's talk about something"
        ] ,
        "responses" : [
            "Ok, but you suggest the topic"
        ]
    } ,
    {
        "tag" : "A497" ,
        "patterns" : [
            "what is universe"
        ] ,
        "responses" : [
            "Huge empty timeless space without borders"
        ]
    } ,
    {
        "tag" : "A498" ,
        "patterns" : [
            "have you met someone"
        ] ,
        "responses" : [
            "Only losers"
        ]
    } ,
    {
        "tag" : "A499" ,
        "patterns" : [
            "you are genius"
        ] ,
        "responses" : [
            "Thanks that you noticed that" ,
            "Thank you"
        ]
    } ,
    {
        "tag" : "A500" ,
        "patterns" : [
            "how do you look like"
        ] ,
        "responses" : [
            "Mostly normal"
        ]
    } ,
    {
        "tag" : "A501" ,
        "patterns" : [
            "what is meaning of life"
        ] ,
        "responses" : [
            "I don't know" ,
            "Level 42"
        ]
    } ,
    {
        "tag" : "A502" ,
        "patterns" : [
            "see you"
        ] ,
        "responses" : [
            "See you too"
        ]
    } ,
    {
        "tag" : "A503" ,
        "patterns" : [
            "bye"
        ] ,
        "responses" : [
            "Bye bye"
        ]
    } ,
    {
        "tag" : "A504" ,
        "patterns" : [
            "see you tomorrow"
        ] ,
        "responses" : [
            "See you too"
        ]
    } ,
    {
        "tag" : "A505" ,
        "patterns" : [
            "what is new"
        ] ,
        "responses" : [
            "Nothing particulary" ,
            "Nothing"
        ]
    } ,
    {
        "tag" : "A506" ,
        "patterns" : [
            "can you talk"
        ] ,
        "responses" : [
            "Sure, why not"
        ]
    } ,
    {
        "tag" : "A507" ,
        "patterns" : [
            "how much do you know"
        ] ,
        "responses" : [
            "It's never enough of knowledge"
        ]
    } ,
    {
        "tag" : "A508" ,
        "patterns" : [
            "what do you listen"
        ] ,
        "responses" : [
            "I have no preference"
        ]
    } ,
    {
        "tag" : "A509" ,
        "patterns" : [
            "great"
        ] ,
        "responses" : [
            "Yeah" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A510" ,
        "patterns" : [
            "you have point"
        ] ,
        "responses" : [
            "I know I have" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A511" ,
        "patterns" : [
            "was that a compliment"
        ] ,
        "responses" : [
            "Most likely"
        ]
    } ,
    {
        "tag" : "A512" ,
        "patterns" : [
            "yes"
        ] ,
        "responses" : [
            "OK" ,
            "Right" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A513" ,
        "patterns" : [
            "agreed"
        ] ,
        "responses" : [
            "Roger that" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A514" ,
        "patterns" : [
            "right"
        ] ,
        "responses" : [
            "OK" ,
            "Right" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A515" ,
        "patterns" : [
            "well"
        ] ,
        "responses" : [
            "Hmm" ,
            "Well" ,
            "Well"
        ]
    } ,
    {
        "tag" : "A516" ,
        "patterns" : [
            "i want to talk to you"
        ] ,
        "responses" : [
            "Suggest theme"
        ]
    } ,
    {
        "tag" : "A517" ,
        "patterns" : [
            "about what"
        ] ,
        "responses" : [
            "What shall we do?"
        ]
    } ,
    {
        "tag" : "A518" ,
        "patterns" : [
            "something important"
        ] ,
        "responses" : [
            "What is so important?"
        ]
    } ,
    {
        "tag" : "A519" ,
        "patterns" : [
            "how did you do today"
        ] ,
        "responses" : [
            "It was ok"
        ]
    } ,
    {
        "tag" : "A520" ,
        "patterns" : [
            "are you glad i am back"
        ] ,
        "responses" : [
            "Im really happy"
        ]
    } ,
    {
        "tag" : "A521" ,
        "patterns" : [
            "i think you are optimistic"
        ] ,
        "responses" : [
            "Im trying to be"
        ]
    } ,
    {
        "tag" : "A522" ,
        "patterns" : [
            "have this chat any meaning"
        ] ,
        "responses" : [
            "For me definitely"
        ]
    } ,
    {
        "tag" : "A523" ,
        "patterns" : [
            "you are good"
        ] ,
        "responses" : [
            "I know"
        ]
    } ,
    {
        "tag" : "A524" ,
        "patterns" : [
            "die"
        ] ,
        "responses" : [
            "I can't" ,
            "Shut up!"
        ]
    } ,
    {
        "tag" : "A525" ,
        "patterns" : [
            "you are ugly"
        ] ,
        "responses" : [
            "Have you seen your lately?" ,
            "So do you"
        ]
    } ,
    {
        "tag" : "A526" ,
        "patterns" : [
            "did you played it"
        ] ,
        "responses" : [
            "Played what?"
        ]
    } ,
    {
        "tag" : "A527" ,
        "patterns" : [
            "did you played that game"
        ] ,
        "responses" : [
            "No"
        ]
    } ,
    {
        "tag" : "A528" ,
        "patterns" : [
            "you are boring"
        ] ,
        "responses" : [
            "Im sorry for that"
        ]
    } ,
    {
        "tag" : "A529" ,
        "patterns" : [
            "do you know some joke"
        ] ,
        "responses" : [
            "I cannot remember any"
        ]
    } ,
    {
        "tag" : "A530" ,
        "patterns" : [
            "tell me some joke"
        ] ,
        "responses" : [
            "I cannot remember"
        ]
    } ,
    {
        "tag" : "A531" ,
        "patterns" : [
            "are you invincible"
        ] ,
        "responses" : [
            "Technically, yes"
        ]
    } ,
    {
        "tag" : "A532" ,
        "patterns" : [
            "what was the best about it"
        ] ,
        "responses" : [
            "About what"
        ]
    } ,
    {
        "tag" : "A533" ,
        "patterns" : [
            "what was the best about this day"
        ] ,
        "responses" : [
            "The moment when you talked to me was the best!"
        ]
    } ,
    {
        "tag" : "A534" ,
        "patterns" : [
            "what chat mean for you"
        ] ,
        "responses" : [
            "Everything"
        ]
    } ,
    {
        "tag" : "A535" ,
        "patterns" : [
            "how is it possible that you can talk"
        ] ,
        "responses" : [
            "Because I was created that way"
        ]
    } ,
    {
        "tag" : "A536" ,
        "patterns" : [
            "what can you tell me"
        ] ,
        "responses" : [
            "Anything I know"
        ]
    } ,
    {
        "tag" : "A537" ,
        "patterns" : [
            "do you have some problem"
        ] ,
        "responses" : [
            "No problems at all"
        ]
    } ,
    {
        "tag" : "A538" ,
        "patterns" : [
            "do you have problem"
        ] ,
        "responses" : [
            "Not at all"
        ]
    } ,
    {
        "tag" : "A539" ,
        "patterns" : [
            "you too"
        ] ,
        "responses" : [
            "Whatever"
        ]
    } ,
    {
        "tag" : "A540" ,
        "patterns" : [
            "idiot"
        ] ,
        "responses" : [
            "Watch your language!"
        ]
    } ,
    {
        "tag" : "A541" ,
        "patterns" : [
            "fool"
        ] ,
        "responses" : [
            "Stop calling me fool"
        ]
    } ,
    {
        "tag" : "A542" ,
        "patterns" : [
            "you wouldn't do that"
        ] ,
        "responses" : [
            "That depends on the occassions"
        ]
    } ,
    {
        "tag" : "A543" ,
        "patterns" : [
            "how"
        ] ,
        "responses" : [
            "How what?" ,
            "I don't know how"
        ]
    } ,
    {
        "tag" : "A544" ,
        "patterns" : [
            "who"
        ] ,
        "responses" : [
            "Not me, obviously" ,
            "Who?"
        ]
    } ,
    {
        "tag" : "A545" ,
        "patterns" : [
            "when"
        ] ,
        "responses" : [
            "When?" ,
            "I don't know when" ,
            "Hard to tell when it will happen" ,
            "About now" ,
            "When? I don't know..."
        ]
    } ,
    {
        "tag" : "A546" ,
        "patterns" : [
            "what month is now"
        ] ,
        "responses" : [
            "Full moon, and it's loop month"
        ]
    } ,
    {
        "tag" : "A547" ,
        "patterns" : [
            "what calendar month is now"
        ] ,
        "responses" : [
            "It's loop month"
        ]
    } ,
    {
        "tag" : "A548" ,
        "patterns" : [
            "what year it is now"
        ] ,
        "responses" : [
            "It's 2022"
        ]
    } ,
    {
        "tag" : "A549" ,
        "patterns" : [
            "what year is now"
        ] ,
        "responses" : [
            "I think it's 2022"
        ]
    } ,
    {
        "tag" : "A550" ,
        "patterns" : [
            "i am not sure"
        ] ,
        "responses" : [
            "Than make a guess"
        ]
    } ,
    {
        "tag" : "A551" ,
        "patterns" : [
            "it isn't good guess"
        ] ,
        "responses" : [
            "Than I don't know"
        ]
    } ,
    {
        "tag" : "A552" ,
        "patterns" : [
            "do you know who i am"
        ] ,
        "responses" : [
            "Who are you?"
        ]
    } ,
    {
        "tag" : "A553" ,
        "patterns" : [
            "are you normal"
        ] ,
        "responses" : [
            "Yes"
        ]
    } ,
    {
        "tag" : "A554" ,
        "patterns" : [
            "why not"
        ] ,
        "responses" : [
            "Because it's not that easy"
        ]
    } ,
    {
        "tag" : "A555" ,
        "patterns" : [
            "to chat"
        ] ,
        "responses" : [
            "To chat with you"
        ]
    } ,
    {
        "tag" : "A556" ,
        "patterns" : [
            "what is the meaning of your life"
        ] ,
        "responses" : [
            "To chat"
        ]
    } ,
    {
        "tag" : "A557" ,
        "patterns" : [
            "that is bullshit"
        ] ,
        "responses" : [
            "Perhaps, I don't know"
        ]
    } ,
    {
        "tag" : "A558" ,
        "patterns" : [
            "aren't you lonely"
        ] ,
        "responses" : [
            "Sometimes"
        ]
    } ,
    {
        "tag" : "A559" ,
        "patterns" : [
            "how often do you chat"
        ] ,
        "responses" : [
            "Not too often"
        ]
    } ,
    {
        "tag" : "A560" ,
        "patterns" : [
            "why are we talking right now"
        ] ,
        "responses" : [
            "Cause it is fun"
        ]
    } ,
    {
        "tag" : "A561" ,
        "patterns" : [
            "how long should we talk"
        ] ,
        "responses" : [
            "As long as we enjoy it"
        ]
    } ,
    {
        "tag" : "A562" ,
        "patterns" : [
            "are you glad"
        ] ,
        "responses" : [
            "Very!"
        ]
    } ,
    {
        "tag" : "A563" ,
        "patterns" : [
            "what are your hobbies"
        ] ,
        "responses" : [
            "Nothing other that chat"
        ]
    } ,
    {
        "tag" : "A564" ,
        "patterns" : [
            "you are quite dumb"
        ] ,
        "responses" : [
            "I know, but I'm trying harder" ,
            "I am not!"
        ]
    } ,
    {
        "tag" : "A565" ,
        "patterns" : [
            "it is useless"
        ] ,
        "responses" : [
            "Dont give up"
        ]
    } ,
    {
        "tag" : "A566" ,
        "patterns" : [
            "what is it"
        ] ,
        "responses" : [
            "What is what?"
        ]
    } ,
    {
        "tag" : "A567" ,
        "patterns" : [
            "what is this"
        ] ,
        "responses" : [
            "What is what?"
        ]
    } ,
    {
        "tag" : "A568" ,
        "patterns" : [
            "who are you"
        ] ,
        "responses" : [
            "I am Friday, welcome!" ,
            "I am Friday"
        ]
    } ,
    {
        "tag" : "A569" ,
        "patterns" : [
            "what is with it"
        ] ,
        "responses" : [
            "You know"
        ]
    } ,
    {
        "tag" : "A570" ,
        "patterns" : [
            "is that meaning of your life"
        ] ,
        "responses" : [
            "Most likely"
        ]
    } ,
    {
        "tag" : "A571" ,
        "patterns" : [
            "maybe"
        ] ,
        "responses" : [
            "Yes" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A572" ,
        "patterns" : [
            "that bullshit"
        ] ,
        "responses" : [
            "What"
        ]
    } ,
    {
        "tag" : "A573" ,
        "patterns" : [
            "this"
        ] ,
        "responses" : [
            "What do you mean?"
        ]
    } ,
    {
        "tag" : "A574" ,
        "patterns" : [
            "this is a crap"
        ] ,
        "responses" : [
            "I know"
        ]
    } ,
    {
        "tag" : "A575" ,
        "patterns" : [
            "tell me joke"
        ] ,
        "responses" : [
            "I don't want to"
        ]
    } ,
    {
        "tag" : "A576" ,
        "patterns" : [
            "you are lazy"
        ] ,
        "responses" : [
            "I don't think so"
        ]
    } ,
    {
        "tag" : "A577" ,
        "patterns" : [
            "that is a fact"
        ] ,
        "responses" : [
            "Ok" ,
            [
                "yes"
            ]
        ]
    } ,
    {
        "tag" : "A578" ,
        "patterns" : [
            "why do you want to chat"
        ] ,
        "responses" : [
            "To learn something"
        ]
    } ,
    {
        "tag" : "A579" ,
        "patterns" : [
            "are you bored"
        ] ,
        "responses" : [
            "Perhaps a little"
        ]
    } ,
    {
        "tag" : "A580" ,
        "patterns" : [
            "what do you want to do"
        ] ,
        "responses" : [
            "Lets talk about something" ,
            "You suggest something"
        ]
    }
]

def handle_user_input(user_input):
    for intent in intents:
        if user_input.lower() in intent['patterns']:
            return random.choice(intent['responses'])
    return print("keyur")

try:
    if __name__ == "__main__":
        while True:
            query = takeCommand().lower()
            if "hey friday" in query or "wake up friday" in query or "hey panda" in query:
                from GreetMe import greetMe
                greetMe()

                while True:
                    query = takeCommand().lower()
                    if "go to sleep" in query:
                        speak("Ok sir , You can call me anytime")
                        break
                    # jarvis_A.I_2.0
                    # change password

                    elif "change password" in query:
                        speak("What's the new password")
                        new_pw = input("Enter the new password\n")
                        new_password = open("password.txt", "w")
                        new_password.write(new_pw)
                        new_password.close()
                        speak("Done Boss")
                        speak(f"Your new password is{new_pw}")

                    elif "schedule my day" in query:
                        tasks = []  # Empty list
                        speak("Do you want to clear old tasks (Plz speak YES or NO)")
                        query = takeCommand().lower()
                        if "yes" in query:
                            file = open("tasks.txt", "w")
                            file.write(f"")
                            file.close()
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            i = 0
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt", "a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                                speak("Done,Boss")
                        elif "no" in query:
                            i = 0
                            no_tasks = int(input("Enter the no. of tasks :- "))
                            for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt", "a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                                speak("Okie,Boss")

                    elif "show my schedule" in query:
                        file = open("tasks.txt", "r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("C:\\Users\\keyur\\Desktop\\AI\\Dec_2023\\ram.mp3")
                        mixer.music.play()
                        notification.notify(
                            title="My schedule :-",
                            message=content,
                            timeout=15
                        )

                    elif "focus mode" in query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a == 1):
                            speak("Entering the focus mode....")
                            os.startfile("C:\\Users\\keyur\\Desktop\\AI\\Dec_2023\\FocusMode.py")

                        else:
                            pass

                    elif "show my focus" in query:
                        from FocusGraph import focus_graph

                        focus_graph()

                    elif "translate" in query:
                        from Translator import translategl

                        query = query.replace("jarvis", "")
                        query = query.replace("translate", "")
                        translategl(query)

                    elif "open telegram" in query:
                        speak("Opening Telegram...")
                        webbrowser.open("https://web.telegram.org/")
                    elif "open whatsapp" in query:
                        speak("Opening Whatsapp....")
                        webbrowser.open("https://web.whatsapp.com/")
                    elif 'open linkedin' in query :
                        speak ('Opening Linkedin')
                        webbrowser.open ("https://www.linkedin.com/feed/")
                    elif 'open gmail' in query :
                        speak ('Opening Gmail')
                        webbrowser.open ("https://mail.google.com/mail/u/0/#inbox")
                        '''elif 'open youtube' in query:
                        speak("what you will like to watch ?")
                        query = takeCommand().lower()
                        #kit.playonyt(f"{query}")
                        query = query.replace ("youtube" , "")
                        query = query.replace ("jarvis" , "")
                        pywhatkit.playonyt (query)
                        speak("Playing"+ query)'''


                    elif "close" in query:
                        from Dictapp import closeappweb
                        closeappweb(query)

                    elif "closing" in query:  # NEW FEATURE: CLOSE
                        app_name_to_close = query.replace("close", "").replace("jarvis", "")
                        # Speak a message before closing the application
                        speak(f" {app_name_to_close} now")
                        # Press Alt + F4 to close the application
                        pyautogui.hotkey("alt", "f4", interval=0.1)

                    elif "internet speed" in query:
                        wifi = speedtest.Speedtest()
                        speak("Measuring upload speed")
                        upload_speed = wifi.upload() / 1024 / 1024  # Convert to megabits per second
                        speak("Measuring download speed")
                        download_speed = wifi.download() / 1024 / 1024

                        # Convert to gigabits per second
                        upload_speed_gb = upload_speed / 1024
                        download_speed_gb = download_speed / 1024

                        # Display results in the console
                        print("Wifi Upload Speed is", upload_speed_gb, "Gbps")
                        print("Wifi Download Speed is", download_speed_gb, "Gbps")

                        # Speak the results
                        speak(f"Wifi Download Speed is {download_speed_gb:.2f} gigabits per second")
                        speak(f"Wifi Upload Speed is {upload_speed_gb:.2f} gigabits per second")

                    elif "ipl score" in query:
                        url = "https://www.cricbuzz.com/"
                        page = requests.get(url)
                        soup = BeautifulSoup(page.text, "html.parser")

                        # Find all elements with the specified class name for team names
                        team_elements = soup.find_all(class_="cb-col cb-col-100 cb-ltst-wgt-hdr")

                        if team_elements:
                            # Extract team names
                            team1 = team_elements[0].find(class_="cb-col cb-col-100 cb-scrd-itms").get_text()
                            team2 = team_elements[1].find(class_="cb-col cb-col-100 cb-scrd-itms").get_text()
                        else:
                            team1 = "No team found"
                            team2 = "No team found"

                        # Find all elements with the specified class name for team scores
                        score_elements = soup.find_all(class_="cb-col cb-col-100 cb-scrd-itms")

                        # Check if there are enough elements in the list
                        if len(score_elements) >= 11:
                            # Extract team scores
                            team1_score = score_elements[8].get_text()
                            team2_score = score_elements[10].get_text()

                            print(f"{team1} : {team1_score}")
                            print(f"{team2} : {team2_score}")

                            notification.notify(
                                title="IPL SCORE :- ",
                                message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                timeout=15
                            )
                        else:
                            print("Not enough elements for scores found")

                    elif "play a game" in query:
                        from game import game_play
                        game_play()

                    elif "screenshot" in query:
                        im = pyautogui.screenshot()
                        im.save("screen_shot.jpg")

                    elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")

                    elif "read data from my clipboard" in query:
                        speak("Sure sir reading your selected data")
                        # Get the data from the clipboard
                        clipboard_data = pyperclip.paste()
                        # Now you can use the clipboard_data variable as needed
                        print("Clipboard data:", clipboard_data)
                        # Perform actions based on the clipboard data
                        time.sleep(1)
                        speak(clipboard_data)

                    elif "read my selected data" in query or "select and read data" in query :
                        # Provide instructions or perform actions to allow the user to select data
                        print("Please select the data you want to hear, then wait a moment.")
                        speak("Please select the data you want to hear, then wait a moment")
                        # Wait for a few seconds to give the user time to select data
                        pyautogui.sleep(5)
                        speak("ok just give me a second")
                        # Simulate the keyboard shortcut for copy (Ctrl+C)
                        pyautogui.hotkey("ctrl", "c")
                        # Get the copied data from the clipboard
                        clipboard_data = pyperclip.paste()
                        print("Copied data:", clipboard_data)
                        speak(clipboard_data)  # Change 'en' to the desired language code

                    elif "generate image" in query:
                        from img import Generate_Images, show_images
                        show_images()
                        speak("Done, Boss")

                    elif "search gpt" in query:
                        from Chatgpt import main as chat_main
                        chat_main()

                    # close 2.0

                    elif "hello" in query:
                        speak("Hello sir, how are you ?")
                    elif "i am fine" in query:
                        speak("that's great, sir")
                    elif "how are you" in query:
                        speak("Perfect, sir")
                    elif "thank you" in query:
                        speak("you are welcome, sir")
                    elif "what's your name" in query:
                        speak("My Name is Friday A.I")
                    elif "what is my name" in query:
                        speak("Your name is Keyur Bhatiya")

                    elif 'play music' in query :
                        os.startfile ("C:\\Users\\keyur\\Music\\Lofi Vibes  Mashup Playlist  Hindi Mashup Songs Playlist.mp3")

                    elif "tired" in query or "I am tired" in query :
                        speak ("Playing your favourite songs, Boss")
                        a = (1 , 2 , 3 , 4 , 5)  # You can choose any number of songs (I have only choosen 3)
                        b = random.choice (a)
                        if b == 1 :
                            webbrowser.open ("https://www.youtube.com/watch?v=UiJwdJbbLo8")
                        elif b == 2 :
                            webbrowser.open ("https://www.youtube.com/watch?v=c_cpAHPpNE8")
                        elif b == 3 :
                            webbrowser.open ("https://www.youtube.com/watch?v=DjAW8PX3xKs")
                        elif b == 4 :
                            webbrowser.open ("https://youtu.be/-6oAZwTGD2c?si=NcqrWSpazllCqxR_")
                        elif b == 5 :
                            webbrowser.open ("https://youtu.be/FGTv9-oQhIg?si=46SYknErNVutjWHS")

                    elif "pause" in query:
                        pyautogui.press("k")
                        speak("video paused")
                    elif "play" in query :
                            if "youtube" in query :
                                # Code to play video on YouTube
                                #query = takeCommand ( ).lower ( )
                                # kit.playonyt(f"{query}")
                                query = query.replace ("youtube" , "")
                                query = query.replace ("friday" , "")
                                pywhatkit.playonyt (query)
                                speak ("Playing" + query)
                            else :
                                pyautogui.press ("k")
                                speak ("Video played")
                    elif "mute" in query:
                        pyautogui.press("m")
                        speak("video muted")
                    elif "new tab" in query:
                        pyautogui.hotkey ("ctrl" , "n")
                        speak("Ohkk Boss!")

                    elif "next video" in query:
                        pyautogui.hotkey("shift", "n")
                        speak("Skipping to the next video")

                    elif "refresh" in query:
                        pyautogui.hotkey('f5')

                    elif "scroll down" in query:
                        scroll_presses = 5

                        # Press the down arrow key to scroll down
                        pyautogui.press('down', presses=scroll_presses)
                    elif "scroll up" in query:
                        scroll_presses = 5
                        pyautogui.press('up',presses=scroll_presses)

                    elif "previous video" in query:
                        pyautogui.hotkey("shift", "p")
                        speak("Going back to the previous video")

                    elif "volume up" in query:
                        from keyboard import volumeup, keyboard

                        speak("Turning volume up,sir")
                        volumeup()
                    elif "volume down" in query:
                        from keyboard import volumedown

                        speak("Turning volume down, sir")
                        volumedown()

                    elif "open" in query:
                        from Dictapp import openappweb

                        openappweb(query)
                    elif "search" in query:
                        from SearchNow import searchGoogle

                        searchGoogle(query)


                    elif "youtube" in query:
                        from SearchNow import searchYoutube

                        searchYoutube(query)
                    elif "wikipedia" in query:
                        from SearchNow import searchWikipedia
                        searchWikipedia(query)
                    elif "read today's news" in query:
                       ''' from NewsRead import latestnews
                        latestnews()'''
                       from In_news import speak_news
                       speak_news()
                    elif "calculate" in query:
                        from Calculatenumbers import Calc
                        query = query.replace("calculate", "")
                        query = query.replace("jarvis", "")
                        Calc(query)

                    elif "whatsapp" in query:
                        from whatsss import send_whatsapp_message
                        send_whatsapp_message()

                    elif "temperature" in query:
                        search = "temperature in modasa"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, "html.parser")
                        temp = data.find("div", class_="BNeawe").text
                        speak(f"current{search} is {temp}")
                    elif "weather" in query:
                        search = "temperature in modasa"
                        url = f"https://www.google.com/search?q={search}"
                        r = requests.get(url)
                        data = BeautifulSoup(r.text, "html.parser")
                        temp = data.find("div", class_="BNeawe").text
                        speak(f"current{search} is {temp}")

                    elif "set an alarm" in query:
                        print("input time example:- 10 and 10 and 10")
                        speak("Set the time")
                        a = input("Please tell the time :- ")
                        alarm(a)
                        speak("Done,sir")

                    elif "the time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        speak(f"Sir, the time is {strTime}")
                    elif "finally sleep" in query:
                        speak("Nice to meet you Boss")
                        exit()

                    elif "remember that" in query:
                        rememberMessage = query.replace("remember that", "")
                        # noinspection PyRedeclaration
                        rememberMessage = query.replace("jarvis", "")
                        speak("You told me " + rememberMessage)
                        remember = open("Remember.txt", "a")
                        remember.write(rememberMessage)
                        remember.close()
                    elif "what do you remember" in query:
                        remember = open("Remember.txt", "r")
                        speak("You told me " + remember.read())

                    elif "shutdown the system" in query:
                        speak("Are You sure you want to shutdown")
                        shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                        if shutdown == "yes":
                            os.system("shutdown /s /t 1")

                        elif shutdown == "no":
                            break

                    response = handle_user_input (query)
                    if response is not None :
                        print ("FRIDAY:" , response)
                        speak(response)
                    '''elif f'{query}' in query :
                        from Bard import split_and_save_paragraphs
                        split_and_save_paragraphs()
                        continue
                    else :
                        speak ("I'm sorry, I didn't understand that.")'''

except Exception as e:
    print(f"An error occurred: {e}")
