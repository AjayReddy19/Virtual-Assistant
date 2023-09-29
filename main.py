import webbrowser
import pyjokes as pyjokes
import pywhatkit as pywhatkit
import speech_recognition as sr
import pyttsx3
import pyaudio
import datetime
import wikipedia
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # You can change the index to choose a different voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your virtual assistant. How can I help you today?")


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""


if __name__ == "__main__":
    wish_me()

    while True:
        query = listen().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break
        elif 'search' in query:
            search = query.replace('search', '')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            print('Here is what i found for ' + search)
            speak('Here is what i found for ' + search)
            break
        elif "hi" in query or "hello" in query:
            speak("Hello! How can i help you")
            break
        elif 'play' in query:
            song = query.replace('play', '')
            speak('Playing' + song)
            print('Playing' + song)
            pywhatkit.playonyt(song)
            break
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
            break
        elif 'map' in query:
            location = query.replace('map', '')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            print('Here is the map of ' + location)
            speak('Here is the map of ' + location)
            break
        elif 'open' in query:
            app = query.replace('open','')
            url = 'https://www.instagram.com/'
            webbrowser.get().open(url)
            print('Here is the map of ' + app)
            speak('Here is the map of ' + app)
            break
        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand. Can you please repeat or ask something else?")
