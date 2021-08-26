# Code meant to be ran on a LINUX machine with PYTHON

# This is just for compatibility reasons, it uses pip install for now
import os
import socket
import webbrowser
import time
from time import ctime
import random
# The ones above are default python modules, below the needed ones are installed.
try:
    os.system('pip install pyaudio speechrecognition gtts playsound pyaudio')
except:
    print('Nothing to do here or no internet')

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()

# def checkInternetSocket(host='8.8.8.8', port=53, timeout=5):
#     try:
#         socket.setdefaulttimeout(timeout)
#         socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#         return True
#     except socket.error as ex:
#         print(ex)
#         return False

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

            playsound('sounds/error.mp3')

            speak('Sorry, I did not get that')
        except sr.RequestError:

            playsound('sounds/error.mp3')

            speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:

        playsound('sounds/gotit.mp3')

        speak('My name is Candance, nice to meet you')

    if 'what time is it' in voice_data:

        playsound('sounds/gotit.mp3')

        speak(ctime())

    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        time.sleep(2)
        url ='https://google.com/search?q=' + search

        playsound('sounds/gotit.mp3')

        webbrowser.get().open(url)
        speak('This is what I have found for    ' + search)
    if ('stop listening' or 'stop' or 'exit' or 'goodbye') in voice_data:

        speak('Goodbye')

        playsound('sounds/exit.mp3')
        exit()
    if 'secret message' in voice_data:
        
        playsound('sounds/gotit.mp3')
        playsound('sounds/error.mp3')
        playsound('sounds/listening.mp3')
        playsound('sounds/exit.mp3')
        speak('Do you like that bitch')

# speak('How can I help you?')
playsound('sounds/listening.mp3')
while 1:
    voice_data = record_audio()
    respond(voice_data)
