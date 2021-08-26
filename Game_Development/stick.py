import pygame
from pygame.math import Vector2
import numpy as np
import pandas as pd
import sys
import math
import os

# Check/install dependencies
# os.system("pip install pygame numpy pandas")

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

origin = 480, 360
length = 250
length2 = 250
length3 = 250
angle = 0
angle2 = 2.09
angle3 = 4.18

speed = -2
hue = 0

def render():
    pygame.display.update()


def move():
    global length
    global angle
    global length2
    global angle2
    global length3
    global angle3

    global start_ticks
    global origin
    global speed
    global hue
    trails = range(1,5*round(speed*speed))

    current_ticks = pygame.time.get_ticks()
    if current_ticks - start_ticks > 16:
        for trail in trails:
            if hue < 250:
                hue = hue + 5
            else:
                hue = 0
                break
            if speed < 0:
                pygame.draw.line(screen, (255, hue, hue), origin, (origin[0] - length*math.cos(angle-0.01*trail),origin[1] - length*math.sin(angle-0.01*trail)), 3)
                pygame.draw.line(screen, (hue, 255, hue), origin, (origin[0] - length*math.cos(angle2-0.01*trail),origin[1] - length2*math.sin(angle2-0.01*trail)), 3)
                pygame.draw.line(screen, (hue, hue, 255), origin, (origin[0] - length*math.cos(angle3-0.01*trail),origin[1] - length2*math.sin(angle3-0.01*trail)), 3)
            else:
                pygame.draw.line(screen, (255, hue, hue), origin, (origin[0] - length*math.cos(angle+0.01*trail),origin[1] - length*math.sin(angle+0.01*trail)), 3)
                pygame.draw.line(screen, (hue, 255, hue), origin, (origin[0] - length*math.cos(angle2+0.01*trail),origin[1] - length2*math.sin(angle2+0.01*trail)), 3)
                pygame.draw.line(screen, (hue, hue, 255), origin, (origin[0] - length*math.cos(angle3+0.01*trail),origin[1] - length2*math.sin(angle3+0.01*trail)), 3)

        start_ticks = current_ticks
        angle = angle - 0.01*speed
        angle2 = angle2 - 0.01*speed
        angle3 = angle3 - 0.01*speed

        if speed > 0:
            if angle == 0.01:
                angle = 6.28
            if angle2 == 0.01:
                angle2 = 6.28
            if angle3 == 0.01:
                angle3 = 6.28
        else:
            if angle == 6.28:
                angle = 0
            if angle2 == 6.28:
                angle2 = 0
            if angle3 == 6.28:
                angle3 = 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        # Check for key
        if event.key == pygame.K_RIGHT:
            speed = speed - 0.2
        elif event.key == pygame.K_LEFT:
            speed = speed + 0.2

    screen.fill(white)
    move()
    render()
    pygame.time.wait(int(1000/60))
    pygame.display.update()
