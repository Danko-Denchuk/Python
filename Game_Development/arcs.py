import pygame
from pygame.math import Vector2
import numpy as np
import pandas as pd
import sys
import math

black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
red = 255, 0, 0
blue = 0, 20, 255
cyan = 0, 255, 255
yellow = 255, 255, 0
orange = 255 , 165, 0
lgray = 224, 224, 224

pygame.init()
size = width, height = 960, 720
screen = pygame.display.set_mode(size)
font = pygame.font.Font('freesansbold.ttf', 24)
start_ticks = pygame.time.get_ticks()
frame = 1
hue = 0

def loading():
    global frame
    global start_ticks
    global hue
    sqr=25
    arc_ticks = pygame.time.get_ticks()

    if arc_ticks - start_ticks > 16:
        pygame.draw.arc(screen, (hue, 255, 0), ((mousePos[0]+sqr*np.sqrt(2)/2, mousePos[1]+sqr*np.sqrt(2)/2), (sqr, sqr)), 0, 0.1*frame, 3)
        pygame.draw.arc(screen, (hue, 255, 0), ((mousePos[0]+sqr*np.sqrt(2)/2, mousePos[1]+sqr*np.sqrt(2)/2), (sqr, sqr)), 3.14, 3.14+0.1*frame, 3)
        start_ticks = arc_ticks
        frame = frame + 1
        hue = hue + 8
        if frame >= 30:
            frame = 1
            hue = 0


def render():
    pygame.display.update()


def texting(texto, center, color):
    text = font.render(str(texto), True, color)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text, textRect)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mousex, mousey=pygame.mouse.get_pos()
    mousePos = mousex, mousey
    left, middle, right = pygame.mouse.get_pressed()

    screen.fill(white)
    loading()
    render()

    pygame.time.wait(int(1000/60))
    pygame.display.update()
