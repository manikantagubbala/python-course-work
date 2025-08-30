# VitualAssistant.py

# pip install pyttsx3 SpeechRecognition pyaudio     -->For install prompt
import speech_recognition as sr         # it is used to convert the speak to text
import pyttsx3                          # it is used to text to speak
import webbrowser                       # it is used for default browser

def listen():                           # create a func using listen()
    recognizer = sr.Recognizer()        # listen the audio from microphone or file
    with sr.Microphone() as source:     # connects to your default microphone ,   source -->AudioSource
        print(" 🎤 Listening...")   
        recognizer.pause_threshold = 1  # it is like a time taken process

        audio = recognizer.listen(source)   # record the voice and convert the audio to text

        try:
            command = recognizer.recognize_google(audio,language= 'en-in')      # audio lan is taken from english through google
            print("🔉 You said: ",command)
            return command.lower()                          # what we speak the words, it gives the words in text format in lowercase
        except sr.UnknownValueError:
            print("❌ Sorry, I didn't understand.")
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("❌ Speech service error.")
            speak("Sorry, my speech service is down.")
            return ""
        

engine = pyttsx3.init()                         # intialize the python text to speech
def speak(text):                        
    voices = engine.getProperty('voices')       # there are diff voices installed(male, female), it should ask speech engine      
    engine.setProperty('voice', voices[0].id)   # set the voice using index value(0,1)
    engine.say(text)                            # we give the text
    engine.runAndWait()                         # it will run th text, convert text to speech

speak("Hello! I'm your virtual assistant. How can I help you?")

while True:
    command = listen()
    if 'google' in command:
        speak('opening google')
        webbrowser.open('https://www.google.com/')

    elif 'play music' in command:
        speak("You can listen your music")

    elif 'stop' in command:
        speak("Okay!")
        break

    else:
        speak("Sorry! I can't understand.")