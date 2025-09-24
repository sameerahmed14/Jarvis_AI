import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests as r
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="YOUR_KEY"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI("YOUR_KEY")

    completion = client.chat.completions.create(
    model="gpt-4o-mini",  # change to a valid available model
    messages=[
       {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
       {"role": "user", "content": command}
    ]
)

    return completion.choices[0].message.content
    

def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkdin" in c.lower():
        speak("opening linkdin")
        webbrowser.open("https://linkdin.com")
    elif c.lower().startswith("play"):
        speak("playing you song as you requested")
        song= c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey= {newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for articles in articles :
                speak(article['title'])

    else:
        #Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)

        



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit = 1 )

            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes boss")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
             print("Error; {0}".format(e))