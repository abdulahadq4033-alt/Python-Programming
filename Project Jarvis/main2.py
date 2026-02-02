import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = "<my api key>"
openai_key = "<your openai key>"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key=openai_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis. Give short responses."},
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message.content

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

    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Song not found")

    elif "news" in command:
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsapi}"
        )
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:
                speak(article["title"])

    else:
        output = aiProcess(command)
        speak(output)

if __name__ == "__main__":
    speak("System initializing")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Ya")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            pass

        except sr.RequestError:
            pass
