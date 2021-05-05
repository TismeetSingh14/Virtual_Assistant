import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def OpenCode():
    home = os.path.expanduser('~')
    home = home.replace("\\",'/')
    path = 'AppData/Local/Programs'
    codePath = home + "/" + path + '/'
    for root,dirs,files in os.walk(codePath):
            for file in files:
                if file.endswith("Code.exe"):
                    k = root + "/" + file
                    os.startfile(k)
                    break