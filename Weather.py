import requests
import json
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
def GetWeather():
    api_key = "b237bbd52a554e65b4b62837202010"
    base_url = "https://api.weatherapi.com/v1/forecast.json"

    say("Please Tell City Name")
    city_name = input()
    complete_url = base_url + "?key=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print("Getting Weather Details about " + x['location']['name'])
    print("The current temperature is " + str(x['current']['temp_c']))
    print("It will be " + x['current']['condition']['text'] + " today")
    print("The sun will rise at " + x['forecast']['forecastday'][0]['astro']['sunrise'] + " and will set at " + x['forecast']['forecastday'][0]['astro']['sunset'])

GetWeather()