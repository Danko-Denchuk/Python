from  pygame.math import Vector2

import sys, pygame
import random

pygame.init()

size = width, height = 960, 720
screen = pygame.display.set_mode(size)

# a= Vector2(200, -100)
# b= Vector2(200,100)
# c= a-b
# alpha=a.angle_to(b)

points = list()
for i in range(1,16):
    points.append(Vector2(random.randrange(30,50)*i, 100))

target = Vector2(450, 300)

rel_points = []
angles = []

for i in range(1, len(points)):
    rel_points.append(points[i] - points[i-1])
    angles.append(0)

def solve_ik(i, endpoint, target):
    if i < len(points) - 2:
        endpoint = solve_ik(i+1, endpoint, target)
    current_point = points[i]

    angle = (endpoint-current_point).angle_to(target-current_point)
    angles[i] += min(max(-3, angle),3)

    return current_point + (endpoint-current_point).rotate(angle)

def render():
    black = 0, 0, 0
    white = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    blue = 0, 0, 255
    cyan = 0, 255, 255

    screen.fill(white)
    for i in range(1, len(points)):
        prev = points[i-1]
        cur = points[i]
        pygame.draw.line(screen, cyan, prev, cur, 8)
    for point in points:
        pygame.draw.circle(screen, cyan, (int(point[0]), int(point[1])), 10)
        pygame.draw.circle(screen, white, (int(point[0]), int(point[1])), 7)
    pygame.draw.circle(screen, black, (int(target[0]), int(target[1])), 8)
    pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mousex, mousey=pygame.mouse.get_pos()
    target = Vector2(mousex, mousey)
    solve_ik(0, points[-1], target)

    angle = 0
    for i in range(1, len(points)):
        angle += angles[i-1]
        points[i] = points[i-1] + rel_points[i-1].rotate(angle)

    render()
    pygame.time.wait(int(1000/60))
