import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def searching(command):
    say('Searching Wikipedia...')
    command =command.replace("wikipedia", "")
    results = wikipedia.summary(command, sentences=5)
    say("According to Wikipedia")
    print(results)
    say(results)