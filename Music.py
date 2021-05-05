import keyboard
from pygame import mixer
import os
import pyttsx3
import speech_recognition as sr
import random
import pyttsx3
import speech_recognition as sr
import string

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

MusicFlag = 0
Music_Path = []

def say(text):
    engine.say(text)
    engine.runAndWait()
    
def PlayMusic():
    mixer.init()
    if os.path.exists("Music_Path.txt")==False or os.stat("Music_Path.txt").st_size == 0:
        Music_Path = []
        say("Finding Music Files on your System. First Time takes a few moments")
        allPaths = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        for path in allPaths:
            path = path + "/"
            for root,dirs,files in os.walk(path):
                for file in files:
                    path = ""
                    if file.endswith(".mp3"):
                        path+=(root+ '/' + str(file))
                        print(path)
                        Music_Path.append(path)
            with open("Music_Path.txt","w+") as f:
                for path in Music_Path:
                    f.write(path+"\n")
    Music_Path = []
    with open("Music_Path.txt","r") as f:
        Music_Path = (f.readlines())
    Clean_Music_Path = []
    for ele in Music_Path:
        Clean_Music_Path.append(ele.strip())
    num = int(random.randint(0,len(Clean_Music_Path)))
    print(num)
    mixer.music.load(Clean_Music_Path[num])
    Music_name = (str(Music_Path[num])).split("/")[-1]
    print("Playing "+ Music_name)
    say("Playing "+ Music_name)
    mixer.music.play()
    while mixer.music.get_busy():
        if keyboard.is_pressed('s'):
            mixer.music.stop()
            break
        if keyboard.is_pressed('p'):
            mixer.music.pause()