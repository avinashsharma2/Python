import pyttsx3, webbrowser, library, requests, os
import speech_recognition as sr
from sys import exit
from openai import OpenAI
from gtts import gTTS
# from pygame import mixer, time
# mixer.init()
# This function is speaking using gtts
# def speak_test(text):
#     tts = gTTS(text)
#     audio_file = "temp.mp3"
#     tts.save(audio_file)
#     mixer.music.load(audio_file)
#     mixer.music.play()   
#     while mixer.music.get_busy():
#         time.Clock().tick()
#     if not mixer.music.get_busy():
#         mixer.music.unload()
#         os.remove(audio_file)

engine = pyttsx3.init()
r = sr.Recognizer()
# Please create and enter before running the program
newsapi = "<your newsapi key"  
gptapi = "<your openai api key>"
country = "us" # Using us because no news of India

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 300)
    engine.say(text)
    engine.runAndWait()

    
def Ai(chat):
    client = OpenAI(
        api_key=gptapi,
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google. Please give short replies"
            },
            {
                "role": "user",
                "content": chat,
            }
        ]
    )
    return completion.choices[0].message.content
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split()[1]
        try:
            link = library.music[song]
            webbrowser.open(link)
        except Exception:
            print("The music is not found")
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={newsapi}")
        if response.status_code == 200:
            data = response.json()  # Parse the response as JSON
            articles = data.get('articles', [])  # Get the list of articles

            # speak only the news headline
            for article in articles:
                speak(article['title'])
        else:
            print(f"Failed to fetch news: {response.status_code} - {response.reason}")
    elif "exit" in c.lower():  
        speak("Bye bye")
        exit()
    else:
        reply = Ai(c)
        speak(reply)
    
if __name__ == "__main__":
    speak("Jarvis initialized")
    
    while True:
            
        # Recognize
        try:
            # Listen for wake word Jarvis
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            print("Recognizing....")
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("ya")
                # Listen for command
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("Jarvis activated.....")
                            audio = r.listen(source, timeout=2, phrase_time_limit=3)
                        print("Recognizing....")
                        command = r.recognize_google(audio)
                        processCommand(command)
                        break
                    except Exception as e:
                        speak("I couldn't hear you")
                        print(f"Error; {e}")
        except Exception as e:
            print(f"Error; {e}")
              
engine.stop() # Stop pyttsx engine