import datetime
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

Month = {
    '01':'January',
    '02':"Feburary",
    '03': 'March',
    '04':'April',
    '05':'May',
    '06':'June',
    '07':"July",
    '08':"August",
    '09':'September',
    '10':'October',
    '11':'November',
    '12':"December"
    }
def DateTime():
    date = str(datetime.date.today()).split('-')
    day = date[-1][-1]
    month = Month[date[1]]
    year = date[0]
    say(day + month + year)