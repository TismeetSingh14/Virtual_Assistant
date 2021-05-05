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

say('Good Bye Sir')
say('Have a nice day')
print('Good Bye Sir. Have a nice day!!')
