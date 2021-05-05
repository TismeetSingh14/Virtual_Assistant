import pyttsx3
import speech_recognition as sr
import webbrowser
import time
from youtube_search import YoutubeSearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

def say(text):
    engine.say(text)
    engine.runAndWait()

def searchingVideo(command):
    say('Searching YouTube...')
    command = command.replace("search", "")
    results = YoutubeSearch(command, max_results=10).to_dict()
    watch_id = results[0]['url_suffix']
    url = "https://youtube.com" + watch_id
    webbrowser.open_new_tab(url)
    time.sleep(5)