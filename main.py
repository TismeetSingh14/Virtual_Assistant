import pyttsx3
import speech_recognition as sr
import datetime
import os
import time
from ecapture import ecapture as ec
import shutil
import random
from pygame import mixer
import keyboard
import defineYourself
import goodbye
import LogOff
import Maps
import openChrome
import openYT
import openGMail
import searchWiki
import tellTime
import VsCode
import Music
import ytSearch
import searchGoogle
import restart
import hibernate
import openExcel
import openPowerpoint
import openOneNote
import openWord
import openSettings
import openGoogle
import Weather
import shutdown
import Date

print("Waking Up Friday")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
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
    
    elif timeNow >=12 and timeNow < 16:
        say("Good Afternoon sir")
    
    else:
        say("Good Evening sir")
    
    say("How may I help you")

say("Waking up Friday")
myName = changeName()
greetings(str(myName))

if __name__=='__main__':

    while True:
        command = takeCommand().lower()
        if command==0:
            continue

        if "good bye" in command or "bye" in command or "stop" in command or "exit" in command:
            goodbye.sayBye()
            break
        
        elif "date" in command:
            Date.DateTime()

        elif 'wikipedia' in command:
            searchWiki.searching(command)
        
        elif 'search' in command:
            searchGoogle.searchQuery(command)

        elif 'open youtube' in command:
            openYT.openSiteYT()
        
        elif 'open chrome' in command:
            openChrome.openProgram()

        elif 'open google' in command:
            openGoogle.openSiteChrome()

        elif 'open gmail' in command:
            openGMail.openSiteGMail()

        elif 'time' in command:
            tellTime.sayTime()

        elif 'who are you' in command:
            defineYourself.defineYou()

        elif "camera" in command or "take a photo" in command:
            ec.capture(0,"robo camera","img.jpg")
        
        elif 'on youtube' in command or 'from youtube' in command:
            ytSearch.searchingVideo(command)
        
        elif 'weather' in command:
            Weather.GetWeather()

        elif "restart" in command:
            restart.Logout()
             
        elif "hibernate" in command or "sleep" in command:
            hibernate.Logout()
 
        elif "log off" in command or "sign out" in command:
            LogOff.Logout()
        
        elif "where is" in command or "locate" in command:
            Maps.Maps(command)
        
        elif 'shutdown' in command or 'power off' in command:
            shutdown.Logout()
        
        elif 'excel' in command:
            openExcel.openProgram()
        
        elif 'powerpoint' in command:
            openPowerpoint.openProgram()
        
        elif 'word' in command:
            openWord.openProgram()
        
        elif 'one note' in command:
            openOneNote.openProgram()
        
        elif 'settings' in command:
            openSettings.openProgram()

        elif 'V S Code' in command or "code" in command:
            VsCode.OpenCode()

        elif 'play music' in command or "music" in command:
            Music.PlayMusic()

time.sleep(4)