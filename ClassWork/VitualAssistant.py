# VitualAssistant.py

# pip install pyttsx3 SpeechRecognition pyaudio     -->For install prompt
import speech_recognition as sr
import pyttsx3 

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" 🎤 Listening...")
        recognizer.pause_threshold = 1

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio,language= 'en-in')
            print("🔉 You said: ",command)
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""
        

engine = pyttsx3.init()
def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text)
    engine.runAndWait()


speak("Hello! I'm your virtual assistant. How can I help you?")

while True:
    command = listen()

    if 'google' in command:
        speak("Opening Google")

    elif 'stop' in command:
        speak("Okay!")
        break

    else:
        speak("Sorry! I can't understand.")