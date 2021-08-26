import pygame
from pygame.math import Vector2
import numpy as np
import pandas as pd
import sys
import math
import os
import matplotlib.pyplot as plt

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
angle = 0
speed = 2
movement = 0

dt=12
kP=0.01
kI=0
kD=0.01

It=0
perror=0

Proportional=list()
Integral=list()
Differential=list()
Angulos=list()

def render():
    pygame.display.update()


def move(angle_goal):
    global length
    global angle
    global movement
    global start_ticks
    global origin
    global speed
    global dt
    global kP
    global kI
    global It
    global kD
    global perror
    global Proportional
    global Integral
    global Differential
    global Angulos

    current_ticks = pygame.time.get_ticks()

    if current_ticks - start_ticks > dt:
        pygame.draw.line(screen, (255, 0, 0), origin, (origin[0] - length*math.cos(angle),origin[1] - length*math.sin(angle)), 3)
        start_ticks = current_ticks

        error = abs(angle - angle_goal)

        # Proportional
        P=kP*error

        Proportional.append(P)

        # Integral
        I=kI*error*dt
        if It<0.5:
            It=It+I
        else:
            It=0

        Integral.append(It)

        # Differential
        D=kD*(error-perror)/dt

        Differential.append(D)

        speed=P+It+D
        # print("P:   " + str(P) + "  I: " + str(I) + " D: " + str(D) + "    PID:    " + str(speed))

        if error > 0.1:
            if angle <= angle_goal:
                angle = angle + speed
            elif angle > angle_goal:
                angle = angle - speed
        else:
            if movement == 0:
                movement = 1
            elif movement == 1:
                movement = 2
        # Previus error
        perror=error

        Angulos.append(angle)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        # Check for key
        if event.key == pygame.K_RIGHT:
            print("left")
        elif event.key == pygame.K_LEFT:
            print("right")

    screen.fill((25, 25, 25))

    if movement == 0:
        move(3.14)
    elif movement == 1:
        move(0)

    if movement == 2:
        fig, ax = plt.subplots(4,1)

        ax[0].plot(Proportional, 'r')
        ax[0].set_title("Proportional")
        ax[0].set_ylabel("Response")
        ax[0].set_xlabel("Iteration")

        ax[1].plot(Integral, 'g')
        ax[1].set_title("Integral")
        ax[1].set_ylabel("Response")
        ax[1].set_xlabel("Iteration")

        ax[2].plot(Differential, 'b')
        ax[2].set_title("Differential")
        ax[2].set_ylabel("Response")
        ax[2].set_xlabel("Iteration")

        ax[3].plot(Angulos, 'k')
        ax[3].set_title("Pos")
        ax[3].set_ylabel("Angle")
        ax[3].set_xlabel("Iteration")

        plt.tight_layout()
        plt.show()

    render()

    pygame.time.wait(int(1000/60))
    pygame.display.update()
