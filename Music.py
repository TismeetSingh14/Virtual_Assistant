import keyboard
from pygame import mixer
import os
import pyttsx3
import speech_recognition as sr
import random
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
    
MusicFlag = 0
Music_Path = []

def PlayMusic():
    mixer.init()
    if MusicFlag==0:
        say("Finding Music Files on your System. First Time takes a few moments")
        for root,dirs,files in os.walk("C:/"):
            for file in files:
                path = ""
                if file.endswith(".mp3"):
                    path+=(root+ '/' + str(file))
                    print(path)
                    Music_Path.append(path)
        MusicFlag=1
    num = int(random.randint(0,len(Music_Path)))
    print(num)
    mixer.music.load(Music_Path[num])
    print("Playing {Music_Path[num]}")
    mixer.music.play()
    while mixer.music.get_busy():
        if keyboard.is_pressed('n'):
            mixer.music.stop()
            break
        if keyboard.is_pressed('p'):
            mixer.music.pause()