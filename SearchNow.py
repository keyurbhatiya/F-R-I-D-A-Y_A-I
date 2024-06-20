import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


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


query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[2].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1)
            speak(result)

        except:
            speak("No speakable output available")


def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your YouTube search!")

        # Extract the search query from the command
        query = query.replace("youtube", "")
        query = query.replace("Friday", "")

        # Open YouTube search results in the default web browser
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)

        # Play the first video in the search results using pywhatkit
        pywhatkit.playonyt(query)

        speak("Done, Sir")

# Rest of your code remains unchanged



'''def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        print(results)
        speak(results)'''
def searchWikipedia(query):
    try:
        # Check if the query contains 'wikipedia' and proceed if it does
        if "wikipedia" in query.lower():
            print("Searching from Wikipedia...")
            # Removing unnecessary terms from the query
            query = query.replace("wikipedia", "").replace("search wikipedia", "").replace("Friday", "")
            # Fetching summary from Wikipedia
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia:")
            print(results)
            speak("According to Wikipedia:")
            speak(results)
            return results
        else:
            print("Please provide a valid Wikipedia query.")
            return "Please provide a valid Wikipedia query."
    except wikipedia.exceptions.DisambiguationError as e:
        # Handling DisambiguationError (if multiple results are found)
        print("Multiple results found. Please be more specific with your query.")
        print("Suggestions:", e.options[:5])  # Printing first 5 suggestions
        return "Multiple results found. Please be more specific with your query."
    except wikipedia.exceptions.PageError:
        # Handling PageError (if the page does not exist)
        print("The requested page does not exist on Wikipedia.")
        return "The requested page does not exist on Wikipedia."
    except Exception as e:
        # Handling other unexpected errors
        print("An error occurred:", str(e))
        return "An error occurred. Please try again later."

