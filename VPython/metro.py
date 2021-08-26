from vpython import *
from scipy import interpolate
import time

class station():
    def __init__(self, x0, y0, z0, a, b, c):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.a = a
        self.b = b
        self.c = c

class Locomotive():
    def __init__(self, x0, y0, z0, L, H, W, a, b, c):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.L = L
        self.H = H
        self.W = W
        self.a = a
        self.b = b
        self.c = c

class Wagon():
    def __init__(self, x0, y0, z0, L, H, W, a, b, c):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.L = L
        self.H = H
        self.W = W
        self.a = a
        self.b = b
        self.c = c

# class rails():
#     def __init__(self, x0, y0, z0, a, b, c):
#         self.x0 = x0
#         self.y0 = y0
#         self.z0 = z0
#         self.a = a
#         self.b = b
#         self.c = c

axis_x=arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.red, shaftwidth=1)
axis_y=arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.green, shaftwidth=1)
axis_z=arrow(pos=vec(0,0,0), axis=vec(0,0,10), color=color.blue, shaftwidth=1)

path = curve(vec(0,0,-50),vec(0, 0, 50), color=color.cyan, radius=0.1)
# extreme1 = sphere(pos=path.point(0), radius=1, color=color.cyan)
# extreme2 = sphere(pos=path.point(path.npoints-1), radius=1, color=color.cyan)

# for x in range(5, 10):
#     sol = 3*x
#     path.append(vec(x, 0, -sol))

# links = curve(path[0], path[len(path-1)])

locomotive = Locomotive(0, 1, 0, 5, 1, 1, 0, 0, -1)
wagon = Wagon(0, 1, -200, 5, 1, 1, 0, 0, -1)

BoxLocomotive=box(pos=vec(locomotive.x0, locomotive.y0, locomotive.z0), color=color.orange, length=locomotive.L, height=locomotive.H, width=locomotive.W, axis=vec(locomotive.a, locomotive.b, locomotive.c))
# BoxWagon1=box(pos=vec(wagon.x0, wagon.y0, wagon.z0 + 5.5), color=color.orange, length=wagon.L, height=wagon.H, width=wagon.W, axis=vec(wagon.a, wagon.b, wagon.c))
# BoxWagon2=box(pos=vec(wagon.x0, wagon.y0, wagon.z0 + 11), color=color.orange, length=wagon.L, height=wagon.H, width=wagon.W, axis=vec(wagon.a, wagon.b, wagon.c))

accel=0.1
initial_speed=0
max_speed=100
t=0
#
while 1:
    # for roll in range(-100,100,1):
    #     rate(60)
    #     print("Rolling right")
    #     BoxLocomotive.up=vec(roll/100,1,0)
    #
    # for roll in range(100,-100,-1):
    #     rate(60)
    #     print("Rolling left")
    #     BoxLocomotive.up=vec(roll/100,1,0)
    #
    # BoxLocomotive.up=vec(0,1,0)

    for pitch in range(-100,100,1):
        print("Pitching upwards")
        rate(60)
        BoxLocomotive.up=vec(0,1,pitch/100)

    for pitch in range(100,-100,-1):
        print("Pitching downwards")
        rate(60)
        BoxLocomotive.up=vec(0,1,pitch/100)

    BoxLocomotive.up=vec(0,1,0)


#     t+=1
#     rate(60)
#     speed=initial_speed+accel*t
#     BoxLocomotive.pos.z+=0.01*speed
#     BoxWagon1.pos.z+=0.01*speed
#     BoxWagon2.pos.z+=0.01*speed
#     if t>10000:
#         t=0
#     if speed >= max_speed:
#         initial_speed=speed
#         accel=0
