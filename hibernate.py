import pyttsx3
import speech_recognition as sr
import subprocess
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def Logout():
    say("Hibernating")
    time.sleep(5)
    subprocess.call(["shutdown", "/h"])