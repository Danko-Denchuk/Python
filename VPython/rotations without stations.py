from vpython import *
import time
import numpy as np
import asyncio

# Axis arrow for orientation
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

# Max number of carts and shape definition
Vagones_Max=6
defBody=Body(0,1,0,10,0,0, 5, 1, 1)

pointer=list()
direction_pointer=list()
trenes=1

for vagon in range(0,Vagones_Max):
    pointer.append(box(pos=vec(defBody.x, defBody.y, defBody.z), axis=vec(defBody.a, defBody.b, defBody.c), length=defBody.L, height=defBody.H, width=defBody.W, color=color.green))
    direction_pointer.append(np.pi/2)


# x0,y0,z0 is the center of the station, a,b,c is the axis, r is the radius, w is the width of the cut
class Station():
    def __init__(self, x0, y0 ,z0,  a, b, c, r, w, h):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.w = w
        self.h = h


estaciones=list()
estaciones.append(Station(54,0,26,1,2.5,1,10,24.5,1))
estaciones.append(Station(162,0,26,1,2.5,1,10,24.5,1))

def get_estaciones():
    for i in range(0,len(estaciones)):
        ## Directional object
        estacion=extrusion(pos=vec(estaciones[i].x0, estaciones[i].y0, estaciones[i].z0-20) , path=paths.arc(radius=12.5, angle1=0, angle2=pi), shape=[shapes.rectangle(pos=[0,0], width=estaciones[i].w, height=estaciones[i].h)], color=color.orange)
        estacion=extrusion(pos=vec(estaciones[i].x0, estaciones[i].y0, estaciones[i].z0+20) , path=paths.arc(radius=12.5, angle1=pi, angle2=2*pi), shape=[shapes.rectangle(pos=[0,0], width=estaciones[i].w, height=estaciones[i].h)], color=color.orange)


# x1,y1 and x2,y2 are control points. x0,y0 and x3,y3 are the ends of the curve.
class Stretch():
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3):
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3


path=curve(radius=0.3)
tramo=list()
tramo.append(Stretch(0, 0, 30, 0, 30, 0, 30, 30))
tramo.append(Stretch(30, 30, 30, 30, 30, 80, 30, 80))

def get_tramo():
    for n in range(0, len(tramo)):
        x0=tramo[n].x0
        y0=tramo[n].y0
        x1=tramo[n].x1
        y1=tramo[n].y1
        x2=tramo[n].x2
        y2=tramo[n].y2
        x3=tramo[n].x3
        y3=tramo[n].y3

        for t in range(0,100):
            t=t/100
            path.append( vec((1-t)*( (1-t)*( (1-t)*y0 +t*y1  )+t* ( (1-t)*y1 +t*y2  ))+t*( (1-t)*( (1-t)*y1 +t*y2  )+t*( (1-t)*y2 +t*y3 )), 0,(1-t)*( (1-t)*( (1-t)*x0 +t*x1  )+t*( (1-t)*x1 +t*x2  ))+t*( (1-t)*( (1-t)* x1 +t*x2  )+t*( (1-t)*x2+t*x3  )) ) )


def movement():
    global direction_pointer

    for point in range(1, path.npoints-1):
        rate(24)
        displacement=path.point(point)['pos']-pointer[0].pos
        # Side to side movement
        if displacement.z != 0:
            if displacement.z > 0 and displacement.x > 0:
                goal_angle=np.arctan(displacement.x/displacement.z)
                error=goal_angle-direction_pointer[0]
                if error > 0:
                    pointer[0].rotate(angle=error, axis=vec(0,1,0))
                    direction_pointer[0]+=error
                else:
                    pointer[0].rotate(angle=abs(error), axis=vec(0,-1,0))
                    direction_pointer[0]-=abs(error)

            elif displacement.z < 0 and displacement.x > 0:
                goal_angle=np.pi-np.arctan(abs(displacement.x/displacement.z))
                error=goal_angle-direction_pointer[0]
                if error > 0:
                    pointer[0].rotate(angle=error, axis=vec(0,1,0))
                    direction_pointer[0]+=error
                else:
                    pointer[0].rotate(angle=abs(error), axis=vec(0,-1,0))
                    direction_pointer[0]-=abs(error)

            elif displacement.z < 0 and displacement.x < 0:
                goal_angle=np.pi+np.arctan(abs(displacement.x/displacement.z))
                error=goal_angle-direction_pointer[0]
                if error > 0:
                    pointer[0].rotate(angle=error, axis=vec(0,1,0))
                    direction_pointer[0]+=error
                else:
                    pointer[0].rotate(angle=abs(error), axis=vec(0,-1,0))
                    direction_pointer[0]-=abs(error)

            elif displacement.z > 0 and displacement.x < 0:
                goal_angle=2*np.pi-np.arctan(abs(displacement.x/displacement.z))
                error=goal_angle-direction_pointer[0]
                if error > 0:
                    pointer[0].rotate(angle=abs(error), axis=vec(0,1,0))
                    direction_pointer[0]+=error
                else:
                    pointer[0].rotate(angle=error, axis=vec(0,1,0))
                    direction_pointer[0]-=abs(error)

        pointer[0].pos.x=path.point(point)['pos'].x
        pointer[0].pos.y=path.point(point)['pos'].y+1
        pointer[0].pos.z=path.point(point)['pos'].z


get_tramo()
get_estaciones()
while 1:
    movement()
