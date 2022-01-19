from vpython import *
from scipy import interpolate
import time
import numpy as np
import random

scene.width = 1600
scene.height = 900
scene.range = 100
scene.title = "Train simulation program"

running = True

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

button(text="Pause\n\n", bind=Run)

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




class Stretch():
    def __init__(self, x0, y0, z0, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        self.x0=x0
        self.y0=y0
        self.z0=z0

        self.x1=x1
        self.y1=y1
        self.z1=z1

        self.x2=x2
        self.y2=y2
        self.z2=z2

        self.x3=x3
        self.y3=y3
        self.z3=z3

ruta=list()
via1=list()
via2=list()

ruta.append(Stretch(0, 0, 0,
                     30, 0, 30,
                     60, 0, 60,
                     120, 35, 90))

via1.append(Stretch(1, 0, 0,
                     60, -20, 30,
                     30, 20, 90,
                     121, 0, 121))

via2.append(Stretch(-1, 0, -1,
                     60, -20, 30,
                     30, 20, 90,
                     119, 0, 119))


# tramo.append(Stretch(90, 0, 90,
#                      120, 0, 120,
#                      150, 0, 150,
#                      200, 25, 200))

def calc_tramo(tramo, visible):
    path = curve(color=color.cyan, radius=0.1, visible=visible)
    aux_path = curve(color=color.red, radius=0.1, visible=0)

    for n in range(0, len(tramo)):
        x0=tramo[n].x0
        y0=tramo[n].y0
        z0=tramo[n].z0

        x1=tramo[n].x1
        y1=tramo[n].y1
        z1=tramo[n].z1

        x2=tramo[n].x2
        y2=tramo[n].y2
        z2=tramo[n].z2

        x3=tramo[n].x3
        y3=tramo[n].y3
        z3=tramo[n].z3

        for t in range(0,10000):
            t=t/10000
            aux_path.append(vec(x0, y0, z0)*(1-t)**3+vec(x1, y1, z1)*(3*t*(1-t)**2)+vec(x2, y2, z2)*(3*(t**2)*(1-t))+vec(x3, y3, z3)*(t**3))
    # for t in range(-1000,1000,1):
    #     aux_path.append(vec(t/10, 5*np.sin(t/100)-2.5*np.cos(t/100), 10*np.cos(t/100)))


    dt = 1
    integral=0
    marker = list()

    for n in range(aux_path.npoints-1):
        if n > 1:
            integral = integral + mag(aux_path.point(n)['pos']-aux_path.point(n-1)['pos'])
        if integral >= dt:
            integral = 0
            path.append(aux_path.point(n)['pos'])
            # marker.append(sphere(pos=aux_path.point(n)['pos'], radius = 2, color = color.red))
    return path

path=calc_tramo(ruta, 0)
# track1=calc_tramo(via1, 0)
# track2=calc_tramo(via2, 1)

track1=curve(color=color.cyan, radius=0.1)
track2=curve(color=color.cyan, radius=0.1)

for n in range(path.npoints-2):
    normal=norm(cross(path.point(n+1)['pos']-path.point(n)['pos'],vec(0,1,0)))

    track1.append(vec(path.point(n)['pos']+0.33*normal))
    track2.append(vec(path.point(n)['pos']-0.33*normal))

print("Number of points in path = " + str(path.npoints))

# Decorative stars
stars=list()
for star in range(1,1000):
    stars.append(sphere(pos=vec(random.randrange(-1000, 1000), random.randrange(-1000, 1000), random.randrange(-1000, 1000)), radius=1, color=color.white))

# extreme1 = sphere(pos=path.point(0), radius=1, color=color.cyan)
# extreme2 = sphere(pos=path.point(path.npoints-1), radius=1, color=color.cyan)

# for x in range(5, 10):
#     sol = 3*x
#     path.append(vec(x, 0, -sol))

# links = curve(path[0], path[len(path-1)])

locomotive = Locomotive(0, 1, 0, 5, 1, 1, 0, 0, -1)
wagon = Wagon(0, 1, -200, 5, 1, 1, 0, 0, -1)

BoxLocomotive=box(pos=vec(locomotive.x0, locomotive.y0, locomotive.z0), color=color.orange, length=locomotive.L, height=locomotive.H, width=locomotive.W, axis=vec(locomotive.a, locomotive.b, locomotive.c))
BoxWagon1=box(pos=vec(wagon.x0, wagon.y0, wagon.z0), color=color.orange, length=wagon.L, height=wagon.H, width=wagon.W, axis=vec(wagon.a, wagon.b, wagon.c))
BoxWagon2=box(pos=vec(wagon.x0, wagon.y0, wagon.z0), color=color.orange, length=wagon.L, height=wagon.H, width=wagon.W, axis=vec(wagon.a, wagon.b, wagon.c))
BoxWagon3=box(pos=vec(wagon.x0, wagon.y0, wagon.z0), color=color.orange, length=wagon.L, height=wagon.H, width=wagon.W, axis=vec(wagon.a, wagon.b, wagon.c))

speed_list=list()
acceleration_list=list()

is_followed=False
def follow(r):
    global is_followed
    if r.checked:
        scene.camera.follow(BoxLocomotive)
        scene.range=10
    else:
        scene.camera.follow(None)

is_deck=False
def deck_view(r):
    global is_deck
    if r.checked:
        is_deck=True
    else:
        is_deck=False

checkbox(bind=follow, text='Follow train') # text to right of checkbox
scene.append_to_caption('\t\t')

checkbox(bind=deck_view, text='Deck view') # text to right of checkbox
scene.append_to_caption('\n\n')

velocity=label(yoffset=100, box=False, color=color.orange)
passengers=label(yoffset=20, box=False, color=color.orange)

while True:
    for n in range(path.npoints-2):
        if running:
            speed=norm(path.point(n+1)['pos']-path.point(n)['pos'])
            velocity.text=(str(round(mag(speed), 2))+'<i>m/s<i>')
            velocity.pos=BoxLocomotive.pos
            # speed2=norm(path.point(n+2)['pos']-path.point(n+1)['pos'])
            # accel=speed2-speed
            BoxLocomotive.up=norm(cross(speed, vec(0,1,0)))

            speed_list.append(speed)
            BoxLocomotive.axis=5*norm(speed)
            BoxLocomotive.pos.x=path.point(n)['pos'].x
            BoxLocomotive.pos.y=path.point(n)['pos'].y+1
            BoxLocomotive.pos.z=path.point(n)['pos'].z

            if n > 5:
                BoxWagon1.axis=5*speed_list[n-5]
                BoxWagon1.up=norm(cross(speed_list[n-5],vec(0,1,0)))
                BoxWagon1.pos.x=path.point(n-5)['pos'].x
                BoxWagon1.pos.y=path.point(n-5)['pos'].y+1
                BoxWagon1.pos.z=path.point(n-5)['pos'].z
                passengers.text=(str('<i>15 passengers<i>'))
                passengers.pos=BoxWagon1.pos

            if n > 10:
                BoxWagon2.axis=5*speed_list[n-10]
                BoxWagon2.up=norm(cross(speed_list[n-10],vec(0,1,0)))
                BoxWagon2.pos.x=path.point(n-10)['pos'].x
                BoxWagon2.pos.y=path.point(n-10)['pos'].y+1
                BoxWagon2.pos.z=path.point(n-10)['pos'].z

            if n > 10:
                BoxWagon3.axis=5*speed_list[n-15]
                BoxWagon3.up=norm(cross(speed_list[n-15],vec(0,1,0)))
                BoxWagon3.pos.x=path.point(n-15)['pos'].x
                BoxWagon3.pos.y=path.point(n-15)['pos'].y+1
                BoxWagon3.pos.z=path.point(n-15)['pos'].z

            # scene.camera.pos.x=BoxLocomotive.pos.x
            # scene.camera.pos.y=BoxLocomotive.pos.y+1
            # scene.camera.pos.z=BoxLocomotive.pos.z
            if is_deck:
                # scene.camera.pos.x=BoxLocomotive.pos.x
                # scene.camera.pos.y=BoxLocomotive.pos.y+1
                # scene.camera.pos.z=BoxLocomotive.pos.z
                scene.center.x=BoxLocomotive.pos.x-5*speed.x
                scene.center.y=BoxLocomotive.pos.y+3
                scene.center.z=BoxLocomotive.pos.z-5*speed.z
                scene.camera.axis=speed

            rate(30)
        else:
            break
    speed_list=[]
    acceleration_list=[]
# BoxLocomotive.up=vec(0,1,0)
