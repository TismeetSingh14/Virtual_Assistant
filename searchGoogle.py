import pyttsx3
import speech_recognition as sr
import webbrowser
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def searchQuery(command):
    command = command.replace("search", "")
    webbrowser.open_new_tab(command)
    time.sleep(5)