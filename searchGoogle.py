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
    say("Searching Google...")
    command = command.replace("search", "")
    url = "https://www.google.com.tr/search?q={}".format(command)
    webbrowser.open_new_tab(url)
    time.sleep(5)