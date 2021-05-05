import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def openProgram():
    os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    say("Google Chrome is ready")
    time.sleep(5)

