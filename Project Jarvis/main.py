import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="<my api key>"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in command:
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open linkedin" in command:
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com")
    
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in command.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=<my api key>")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


    else:
        #let openAI handle the request
        pass

if __name__ == "__main__":
    speak("System initializing")

    # 🎯 VERY IMPORTANT: noise calibration
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Ya")

                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Google API error:", e)
