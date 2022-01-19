from vpython import *
import time
import numpy as np
import asyncio

axis_x=arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.red, shaftwidth=1)
axis_y=arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.green, shaftwidth=1)
axis_z=arrow(pos=vec(0,0,0), axis=vec(0,0,10), color=color.blue, shaftwidth=1)

# Green rectangle as vagon shape definition
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

Vagones_Max=6
defBody=Body(0,1,0,10,0,0, 5, 1, 1)

pointer=list()
direction_pointer=list()
pointer_progress=list()

for vagon in range(0, Vagones_Max):
    pointer.append(box(pos=vec(defBody.x, defBody.y, defBody.z), axis=vec(defBody.a, defBody.b, defBody.c), length=defBody.L, height=defBody.H, width=defBody.W, color=color.green))
    direction_pointer.append(np.pi/2)
    pointer_progress.append(0)

# x0,y0,z0 is the center of the station, a,b,c is the axis, r is the radius, w is the width of the station
class Station():
    def __init__(self, x0, y0 ,z0, a, b, c, r, w, h):
        # Center of the station
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        # Axis of the station
        self.a = a
        self.b = b
        self.c = c
        # Radius and shape
        self.r = r
        self.w = w
        self.h = h

        # Direction of the station
        self.direction=diff_angle(vec(self.a,0,self.c).hat, vec(0,0,1))
        print(degrees(self.direction))
        # Entry and exit points
        self.in1=vec(self.x0+24, self.y0, self.z0-4)
        self.in2=vec(self.x0-24, self.y0, self.z0+4)
        self.out1=vec(self.x0+24, self.y0, self.z0+4)
        self.out2=vec(self.x0-24, self.y0, self.z0-4)


estaciones=list()
# x,y,z of the station, axis,
estaciones.append(Station(54,0,26, 1,2.5,.5, 10,24.5,1))
estaciones.append(Station(0,50,150, -.5,2.5,-1, 10,24.5,1))

# print("Direction:   " + str(estaciones[0].direction) + "      in1:   " + str(estaciones[0].in1) + "      in2:   " + str(estaciones[0].in2))


def get_estaciones():
    etiqueta_estaciones=list()
    for i in range(0,len(estaciones)):
        ## Directional object
        etiqueta_estaciones.append([i])
        etiqueta_estaciones[i]=label(pos=vec(estaciones[i].x0, estaciones[i].y0, estaciones[i].z0), text=str(i), xoffset=0, yoffset=60, space=10, height= 20, border=1, color=color.orange, visible=False)
        estacion=extrusion(pos=vec(estaciones[i].x0, estaciones[i].y0, estaciones[i].z0-20) , path=paths.arc(radius=12.5, angle1=0, angle2=pi), shape=[shapes.rectangle(pos=[0,0], width=estaciones[i].w, height=estaciones[i].h)], color=color.orange)
        estacion.rotate(angle=diff_angle(vec(0,0,1),vec(estaciones[i].a, 0, estaciones[i].c)), axis=vec(0,1,0), origin=vec(estaciones[i].x0,estaciones[i].y0, estaciones[i].z0))
        estacion=extrusion(pos=vec(estaciones[i].x0, estaciones[i].y0, estaciones[i].z0+20) , path=paths.arc(radius=12.5, angle1=pi, angle2=2*pi), shape=[shapes.rectangle(pos=[0,0], width=estaciones[i].w, height=estaciones[i].h)], color=color.orange)
        estacion.rotate(angle=diff_angle(vec(0,0,1),vec(estaciones[i].a, 0, estaciones[i].c)), axis=vec(0,1,0), origin=vec(estaciones[i].x0,estaciones[i].y0, estaciones[i].z0))

        estaciones[i].in1=vec(estaciones[i].in1.x-12*np.sin(estaciones[i].direction/2), estaciones[i].in1.y, estaciones[i].in1.z-np.cos(estaciones[i].direction/2))
        estaciones[i].in2=vec(estaciones[i].in2.x-12*np.sin(estaciones[i].direction/2), estaciones[i].in2.y, estaciones[i].in2.z-np.cos(estaciones[i].direction/2))
        estaciones[i].out1=vec(estaciones[i].out1.x-12*np.sin(estaciones[i].direction/2), estaciones[i].out1.y, estaciones[i].out1.z-np.cos(estaciones[i].direction/2))
        estaciones[i].out2=vec(estaciones[i].out2.x-12*np.sin(estaciones[i].direction/2), estaciones[i].out2.y, estaciones[i].out2.z-np.cos(estaciones[i].direction/2))


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

# Shape of ends and connections markers, spheres.
class Marker():
    def __init__(self, x, y, z):
            self.x=x
            self.y=y
            self.z=z


path=curve(radius=0.3)
tramo=list()


for station in range(0, len(estaciones)-1):
    tramo.append(Stretch(estaciones[station].in2.z, estaciones[station].in2.x, estaciones[station].in2.z, estaciones[station].in2.x, estaciones[station].out1.z, estaciones[station].out1.x, estaciones[station].out1.z, estaciones[station].out1.x))
    tramo.append(Stretch(estaciones[station].out1.z, estaciones[station].out1.x, estaciones[station].out1.z, estaciones[station].out1.x+100, estaciones[station+1].in2.z, estaciones[station+1].in2.x-100, estaciones[station+1].in2.z, estaciones[station+1].in2.x))
    tramo.append(Stretch(estaciones[station+1].in2.z, estaciones[station+1].in2.x, estaciones[station+1].in2.z, estaciones[station+1].in2.x, estaciones[station+1].out1.z, estaciones[station+1].out1.x, estaciones[station+1].out1.z, estaciones[station+1].out1.x))
    tramo.append(Stretch(estaciones[station+1].out1.z, estaciones[station+1].out1.x, estaciones[station+1].out1.z, estaciones[station+1].out1.x+100, estaciones[station].in1.z, estaciones[station].in1.x+100, estaciones[station].in1.z, estaciones[station].in1.x))
    tramo.append(Stretch(estaciones[station].in1.z, estaciones[station].in1.x, estaciones[station].in1.z, estaciones[station].in1.x, estaciones[station].out2.z, estaciones[station].out2.x, estaciones[station].out2.z, estaciones[station].out2.x))
    tramo.append(Stretch(estaciones[station].out2.z, estaciones[station].out2.x, estaciones[station].out2.z, estaciones[station].out2.x-20, estaciones[station].in2.z, estaciones[station].in2.x-20, estaciones[station].in2.z, estaciones[station].in2.x))

joints=list()
dots=list()

for station in range(0, len(estaciones)):
    joints.append(Marker(estaciones[station].in1.x, estaciones[station].in1.y, estaciones[station].in1.z))
    joints.append(Marker(estaciones[station].out1.x, estaciones[station].out1.y, estaciones[station].out1.z))
    joints.append(Marker(estaciones[station].in2.x, estaciones[station].in2.y, estaciones[station].in2.z))
    joints.append(Marker(estaciones[station].out2.x, estaciones[station].out2.y, estaciones[station].out2.z))

for points in range(0, 4*len(estaciones), 4):
    dots.append(sphere(pos=vec(joints[points].x, joints[points].y, joints[points].z), radius=1, color=color.green))
    dots.append(sphere(pos=vec(joints[points+1].x, joints[points+1].y, joints[points+1].z), radius=1, color=color.orange))
    dots.append(sphere(pos=vec(joints[points+2].x, joints[points+2].y, joints[points+2].z), radius=1, color=color.green))
    dots.append(sphere(pos=vec(joints[points+3].x, joints[points+3].y, joints[points+3].z), radius=1, color=color.orange))


def get_tramo():
    etiqueta_tramo=list()
    for n in range(0, len(tramo)):
        x0=tramo[n].x0
        y0=tramo[n].y0
        x1=tramo[n].x1
        y1=tramo[n].y1
        x2=tramo[n].x2
        y2=tramo[n].y2
        x3=tramo[n].x3
        y3=tramo[n].y3

        etiqueta_tramo.append([n])
        etiqueta_tramo[n]=label(pos=vec(y1, 0, x1), text=str(n), xoffset=30, yoffset=30, space=10, height= 20, border=1, visible=False)

        for t in range(0,400):
            t=t/400
            path.append( vec((1-t)*( (1-t)*( (1-t)*y0 +t*y1  )+t* ( (1-t)*y1 +t*y2  ))+t*( (1-t)*( (1-t)*y1 +t*y2  )+t*( (1-t)*y2 +t*y3 )), 0,(1-t)*( (1-t)*( (1-t)*x0 +t*x1  )+t*( (1-t)*x1 +t*x2  ))+t*( (1-t)*( (1-t)* x1 +t*x2  )+t*( (1-t)*x2+t*x3  )) ) )


def toggle_estaciones():
    for i in range(0,len(estaciones)):
        if etiqueta_estaciones[i].visible==True:
            etiqueta_estaciones[i].visible=False
        elif etiqueta_estaciones[i].visible==False:
            etiqueta_estaciones[i].visible=True


def toggle_tramos():
    for n in range(0, len(tramo)):
        if etiqueta_tramo[n].visible==True:
            etiqueta_tramo[n].visible=False
        elif etiqueta_tramo[n].visible==False:
            etiqueta_tramo[n].visible=True


def toggle_vagons():
    for vagon in range(0,Vagones_Max):
        if etiqueta_vagones[vagon].visible==True:
            etiqueta_vagones[vagon].visible=False
        elif etiqueta_vagones[vagon].visible==False:
            etiqueta_vagones[vagon].visible=True


def movement(pointer, vagon, point):
    global direction_pointer
    speed=path.point(point)['pos']-pointer.pos

    pointer.up=vec(cross(speed, vec(-speed.x, speed.y, speed.z)))

    # Side to side movement
    if speed.z != 0:
        if speed.z > 0 and speed.x > 0:
            goal_angle=np.arctan(speed.x/speed.z)
            error=goal_angle-direction_pointer[vagon]
            if error > 0:
                pointer.rotate(angle=error, axis=vec(0,1,0))
                direction_pointer[vagon]+=error
            else:
                pointer.rotate(angle=abs(error), axis=vec(0,-1,0))
                direction_pointer[vagon]-=abs(error)

        elif speed.z < 0 and speed.x > 0:
            goal_angle=np.pi-np.arctan(abs(speed.x/speed.z))
            error=goal_angle-direction_pointer[vagon]
            if error > 0:
                pointer.rotate(angle=error, axis=vec(0,1,0))
                direction_pointer[vagon]+=error
            else:
                pointer.rotate(angle=abs(error), axis=vec(0,-1,0))
                direction_pointer[vagon]-=abs(error)

        elif speed.z < 0 and speed.x < 0:
            goal_angle=np.pi+np.arctan(abs(speed.x/speed.z))
            error=goal_angle-direction_pointer[vagon]
            if error > 0:
                pointer.rotate(angle=error, axis=vec(0,1,0))
                direction_pointer[vagon]+=error
            else:
                pointer.rotate(angle=abs(error), axis=vec(0,-1,0))
                direction_pointer[vagon]-=abs(error)

        elif speed.z > 0 and speed.x < 0:
            goal_angle=2*np.pi-np.arctan(abs(speed.x/speed.z))
            error=goal_angle-direction_pointer[vagon]
            if error > 0:
                pointer.rotate(angle=abs(error), axis=vec(0,1,0))
                direction_pointer[vagon]+=error
            else:
                pointer.rotate(angle=error, axis=vec(0,1,0))
                direction_pointer[vagon]-=abs(error)

    pointer.pos.x=path.point(point)['pos'].x
    pointer.pos.y=path.point(point)['pos'].y+1
    pointer.pos.z=path.point(point)['pos'].z


get_tramo()
get_estaciones()

etiqueta_vagones=list()
for vagon in range(0,Vagones_Max):
        etiqueta_vagones.append([vagon])
        etiqueta_vagones[vagon]=label(pos=vec(0,0,0), text=str(vagon), xoffset=0, yoffset=30, space=10, height= 20, border=1, color=color.green, visible=False)

distance_between_vagons=0

while 1:
    for blob in range(0, path.npoints):
        rate(240)
        for vagon in range(1,Vagones_Max):
            if pointer_progress[0]<path.npoints-1 and pointer_progress[vagon]<path.npoints-1:
                distance_between_vagons=mag(pointer[vagon].pos-pointer[vagon-1].pos)
                if distance_between_vagons>7:
                    pointer_progress[0]-=2
                    pointer_progress[vagon]+=2
                    movement(pointer[vagon], vagon, pointer_progress[vagon])

                elif distance_between_vagons>5.6 and distance_between_vagons<7:
                    pointer_progress[0]-=1
                    pointer_progress[vagon]+=1
                    movement(pointer[vagon], vagon, pointer_progress[vagon])

                pointer_progress[0]+=1
                movement(pointer[0], 0, pointer_progress[0])
                etiqueta_vagones[0].pos=pointer[0].pos
                etiqueta_vagones[vagon].pos=pointer[vagon].pos
            else:
                for vagon in range(0, Vagones_Max):
                    pointer_progress[vagon]=0
