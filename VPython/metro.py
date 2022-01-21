from vpython import *

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
ruta2=list()
ruta.append(Stretch(0, 0, 0, 30, 0, 30, 60, 0, 60, 120, 35, 90))
ruta2.append(Stretch(0, 0, 0, 30, 0, 30, 60, 0, 60, 240, 35, -190))

def calc_tramo(tramo, visible):
    path = curve(color=color.cyan, radius=0.1, visible=visible)
    aux_path = curve(color=color.red, radius=0.1, visible=0)

    for n in range(len(tramo)):
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

    dt = 1
    integral=0

    for n in range(aux_path.npoints-1):
        if n > 1:
            integral = integral + mag(aux_path.point(n)['pos']-aux_path.point(n-1)['pos'])
        if integral >= dt:
            integral = 0
            path.append(aux_path.point(n)['pos'])

    track1=curve(color=color.cyan, radius=0.1)
    track2=curve(color=color.cyan, radius=0.1)

    for n in range(path.npoints-2):
        normal=norm(cross(path.point(n+1)['pos']-path.point(n)['pos'],vec(0,1,0)))

        track1.append(vec(path.point(n)['pos']+0.33*normal))
        track2.append(vec(path.point(n)['pos']-0.33*normal))

    return path


path=calc_tramo(ruta, 0)
path2=calc_tramo(ruta2,0)

locomotive = Locomotive(0, 1, 0, 5, 1, 1, 0, 0, -1)

def make_train(cabs, line):
    locomotive = Locomotive(0, 1, 0, 5, 1, 1, 0, 0, -1)
    train=list()
    if line==1:
        col=color.cyan
    if line==2:
        col=color.orange

    for n in range(cabs):
        train.append(box(color=col, length=locomotive.L, height=locomotive.H, width=locomotive.W, axis=vec(locomotive.a, locomotive.b, locomotive.c)))
    return train

BoxLocomotive=make_train(6,1)
AnotherLocomotive=make_train(6,2)

is_followed=False
def follow(r):
    global is_followed
    if r.checked:
        scene.camera.follow(BoxLocomotive[0])
        scene.range=10
    else:
        scene.camera.follow(None)


checkbox(bind=follow, text='Follow train')
scene.append_to_caption('\t\t')

def calc_speed(path):
    speed=list()
    for s in range(path.npoints-1):
        speed.append(norm(path.point(s+1)['pos']-path.point(s)['pos']))
    return speed


def move_train(train, path, n, speed, mode):
    if path.npoints-n > 5:
        for t in range(train-1):
            if n-5*t > 0:
                mode[t].up=norm(cross(speed[n-5*t], vec(0,1,0)))
                mode[t].axis=5*speed[n-5*t]
                mode[t].pos.x=path.point(n-5*t)['pos'].x
                mode[t].pos.y=path.point(n-5*t)['pos'].y+1
                mode[t].pos.z=path.point(n-5*t)['pos'].z
    else:
        return 0

t1=clock()*1000
vel=calc_speed(path)
vel2=calc_speed(path2)
n=0
while running:
    if running:
        if ((clock()*1000)-t1)>12:
            line1=move_train(len(BoxLocomotive), path, n, vel, BoxLocomotive)
            line2=move_train(len(AnotherLocomotive), path2,  n, vel2, AnotherLocomotive)
            t1=clock()*1000
            n=n+1
            if line1==0 and line2==0:
                n=0

    else:
        break
