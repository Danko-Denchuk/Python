from gtts import gTTS
from playsound import playsound

tts= gTTS('Hello, I am Candance, you voice assistant, how can I help you')

with open("sounds/presentation.mp3","wb") as archivo:
    tts.write_to_fp(archivo)

# playsound('sounds/presentation.mp3')
