import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
from ecapture import ecapture as ec
import shutil
import subprocess
import random
from pygame import mixer
import platform
import socket
import keyboard
import defineYourself
import goodbye
import LogOff
import Maps
import openchrome
import openYT
import openGMail
import searchWiki
import tellTime
import VsCode
import Music

MusicFlag = 0
print("Waking Up Friday")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
Music_Path = []
def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    ct = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        ct.pause_threshold = 0.5
        audio = ct.listen(source)

    try :
        print("Recognizing...")
        command = ct.recognize_google(audio, language = 'en-in')
        print(f"Command Given: {command}\n")

    except Exception as e:
        say("Pardon Sir")
        print("Pardon sir")
        return "None"

    return command

def changeName():
    say("What should i call you sir")
    newName = takeCommand()
    say("Welcome Mr." + newName)
    columns = shutil.get_terminal_size().columns
    return newName

def greetings(myName):
    timeNow = int(datetime.datetime.now().hour)

    if timeNow >= 0 and timeNow < 12:
        say("Good Morning sir")
        say("Welcome Back")
    
    elif timeNow >=12 and timeNow < 16:
        say("Good Afternoon sir")
        say("Welcome Back")
    
    else:
        say("Good Evening sir")
        say("Welcome Back")
    
    say("How may I help you")

say("Waking up Friday")
myName = changeName()
greetings(str(myName))

if __name__=='__main__':

    while True:
        command = takeCommand().lower()
        if command==0:
            continue

        if "good bye" in command or "bye" in command or "stop" in command:
            say('Good Bye Sir')
            say('Have a nice day')
            print('Good Bye Sir. Have a nice day!!')
            break

        elif 'wikipedia' in command:
            say('Searching Wikipedia...')
            command =command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=5)
            say("According to Wikipedia")
            print(results)
            say(results)

        elif 'open youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            say("Youtube is ready")
            time.sleep(5)

        elif 'open google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            say("Google Chrome is ready")
            time.sleep(5)

        elif 'open gmail' in command:
            webbrowser.open_new_tab("gmail.com")
            say("GMail is ready")
            time.sleep(5)

        elif 'time' in command:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")

        elif 'who are you' in command:
            say("Hello Sir I am Jarvis Your personal AI Assistant I am here to help you sir You may ask me anything")

        elif "camera" in command or "take a photo" in command:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
            time.sleep(5)

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in command or "sleep" in command:
            say("Hibernating")
            subprocess.call(["shutdown / h"])
 
        elif "log off" in command or "sign out" in command:
            say("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        
        elif "where is" in command or "locate" in command:
            command = command.replace("where is", "")
            location = command
            say("You asked to Locate" + location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        
        elif 'open code' in command:
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

        elif 'play music' in command:
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

time.sleep(4)