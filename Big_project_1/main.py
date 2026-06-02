import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import time
from google import genai


r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 190)

def speak(text):

    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):

    client = genai.Client(api_key="AIzaSyArWBiWTmryiwTIRaGSHeJSWxJrKIkJNYI")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Answer shortly in 1 sentence: {command}"
    )

    return response.text
 
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://Facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        songs = c.lower().split(" ")[1]
        links = musicLib.music[songs]
        webbrowser.open(links)
    else:
        output = aiProcess(c)
        speak(output)




if __name__ == "__main__":
    speak("Initializing Jarvis ...")

    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source , timeout=3 , phrase_time_limit = 2)
            word = r.recognize_google(audio)
            print("You said:", word)
            if "jarvis" in word.lower():
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
             print("FULL ERROR:", repr(e))
