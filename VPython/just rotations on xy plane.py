from vpython import *
import time
import numpy as np
import asyncio

axis_x=arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.red, shaftwidth=1)
axis_y=arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.green, shaftwidth=1)
axis_z=arrow(pos=vec(0,0,0), axis=vec(0,0,10), color=color.blue, shaftwidth=1)

class Body():
    def __init__(self, x, y, z, a, b, c, L, H, W):
        self.x=x
        self.y=y
        self.z=z
        self.a=a
        self.b=b
        self.c=c
        self.L=L
        self.H=H
        self.W=W

defBody=Body(1,0,0,10,0,0, 5, 1, 1)

pointer=arrow(pos=vec(defBody.x, defBody.y, defBody.z), axis=vec(defBody.a, defBody.b, defBody.c), shaftwidth=1,color=color.green)

path=curve(radius=0.3)
for z in range(68,1,-1):
    #path.append(vec(20*np.sin(z/10),0,-z))
    path.append(vec(50*np.sin(z/10), 0, 50*cos(z/10)))

pointer_direction=vec(1,0,0)
def movement():
    global pointer_direction
    for point in range(1, path.npoints-1):
        rate(6)
        displacement=path.point(point)['pos']-pointer.pos
        angle=diff_angle(displacement, pointer_direction)

        if displacement.x > 0 and displacement.z > 0:
            pointer.rotate(angle=angle, axis=vec(0, 1, 0))
            pointer_direction.hat=displacement

        elif displacement.x < 0 and displacement.z > 0:
            pointer.rotate(angle=angle, axis=vec(0, 1, 0))
            pointer_direction.hat=displacement

        elif displacement.x < 0 and displacement.z < 0:
            pointer.rotate(angle=angle, axis=vec(0, 1, 0))
            pointer_direction.hat=displacement

        elif displacement.x > 0 and displacement.z < 0:
            pointer.rotate(angle=angle, axis=vec(0, 1, 0))
            pointer_direction.hat=displacement

        elif displacement.x == 0 or displacement.z == 0:
            if displacement.x == 0:
                pointer_direction.hat=vec(0,0,1)
            elif displacement.z == 0:
                pointer_direction.hat=vec(1,0,0)

        label(pos=vec(0,40,0), text=degrees(angle))
        label(pos=vec(0,20,0), text=pointer_direction)

        pointer.pos=path.point(point)['pos']
while 1:
    movement()
