import matplotlib.pyplot as plt
import pygame
import playsound

# With pygame
pygame.mixer.init()
pygame.mixer.music.load("output.wav")
pygame.mixer.music.play()
print("Currently playing with pygame")
pygame.time.wait(5000)
pygame.mixer.music.stop()

# With playsound it gives a warning when playing wav
playsound.playsound("output.wav", False)
print("Currently playing file with playsound")
pygame.time.wait(5000)
