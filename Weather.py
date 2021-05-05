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
    city_name = takeCommand()
    complete_url = base_url + "?key=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(x)
    # if x["cod"] != "404":
    #     print(x)
    #     y = x["main"]
    #     current_temperature = y["temp"]
    #     current_pressure = y["pressure"]
    #     current_humidiy = y["humidity"]
    #     z = x["weather"]
    
    #     weather_description = z[0]["description"]
    
    #     print(" Temperature (in kelvin unit) = " +
    #                     str(current_temperature) + 
    #         "\n atmospheric pressure (in hPa unit) = " +
    #                     str(current_pressure) +
    #         "\n humidity (in percentage) = " +
    #                     str(current_humidiy) +
    #         "\n description = " +
    #                     str(weather_description))
    #     say(" Temperature (in kelvin unit) = " +
    #                     str(current_temperature) + 
    #         "\n atmospheric pressure (in hPa unit) = " +
    #                     str(current_pressure) +
    #         "\n humidity (in percentage) = " +
    #                     str(current_humidiy) +
    #         "\n description = " +
    #                     str(weather_description))
    
    # else:
    #     say(" City Not Found ")

GetWeather()