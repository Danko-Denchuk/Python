from vpython import *
import time

axis_x=arrow(pos=vec(0,0,0), axis=vec(10,0,0), color=color.red, shaftwidth=1)
axis_y=arrow(pos=vec(0,0,0), axis=vec(0,10,0), color=color.green, shaftwidth=1)
axis_z=arrow(pos=vec(0,0,0), axis=vec(0,0,10), color=color.blue, shaftwidth=1)

rocket_core = cylinder(pos=vec(0,0,0), axis=vec(0,10,0),color=color.green, radius=1)
# nose_cone = cone(pos=vec(0,10,0),axis=vec(0,5,0),color=color.green, radius=1)

# cucubumba = compound([core, nose_cone], origin=vec(0,0,0))

v_0 = vec(10, 10, 0)    # m/s
a_0 = vec(0, 0, 0)      # m/s^2
g = -9.82               # m/s^2

# v=v_0+vec(a_0*t)

initial_position=rocket_core.pos # m
inst_pos=vec(0,0,0)
a=vec(0,0,0)
v=vec(0,0,0)

def compute(t):


# Fly
while 1:
    for t in range(1,100,1):
        compute(t/1000)
        rate(24)
        rocket_core.pos = inst_pos
        print(str(inst_pos))
