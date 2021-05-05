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
    
def defineYou():
    say("Hello Sir I am Friday")
    say("Your personal AI Assistant")
    say("I am here to help you sir")
    say("You may ask me anything")