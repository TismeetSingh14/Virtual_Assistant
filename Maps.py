import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def Maps(command):
    command = command.replace("where is", "")
    location = command
    say("You asked to Locate" + location)
    webbrowser.open("https://www.google.nl / maps / place/" + location + "")