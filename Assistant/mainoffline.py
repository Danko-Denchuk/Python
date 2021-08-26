import speech_recognition as sr
import webbrowser
import time
import os
import random
from time import ctime
from gtts import gTTS
from playsound import playsound


r = sr.Recognizer()

def speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r= random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + 'mp3'
    tts.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that, try again')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Candance, nice to meet you')

    if 'what time is it' in voice_data:
        speak(time())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        url ='https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('This is what I have found for    ' + search)
    if ('stop listening' or 'stop' or 'exit') in voice_data:
        exit()

speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
