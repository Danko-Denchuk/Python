from os import path
from pydub import AudioSegment

# Files
dst = "output.wav"

def mp3_to_wav(src):
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

working = True

while working:
    print("Write the filename")
    src = input()
    print(src)
    try:
        mp3_to_wav(src)
        print("Converted succesfully")
        working = False
    except:
        print("Error")
