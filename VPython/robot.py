from vpython import *
from scipy import interpolate
import time

class segment:
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


class servo:
    def __init__(self, x0, y0, z0, a, b, c, r):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.a = a
        self.b = b
        self.c = c
        self.r = r


arm1 = segment(0, 5, 0, 10, 1, 1, 0, 1, 0)
arm2 = segment(5, 10, 0, 10, 1, 1, 1, 0, 0)
arm3 = segment(14, 14, 0, 10, 1, 1, 1, 1, 0)

servo1 = servo(0, 0, -1.5, 0, 0, 3, 1)
servo2 = servo(0, 10, -1.5, 0, 0, 3, 1)
servo3 = servo(10, 10, -1.5, 0, 0, 3, 1)
servo4 = servo(17, 17, -1.5, 0, 0, 3, 1)

arm_1=box(pos=vec(arm1.x0, arm1.y0, arm1.z0),axis=vec(arm1.a,arm1.b,arm1.c), color=color.orange, length=arm1.L, height=arm1.H, width=arm1.W)
arm_2=box(pos=vec(arm2.x0, arm2.y0, arm2.z0),axis=vec(arm2.a,arm2.b,arm2.c), color=color.orange, length=arm2.L, height=arm2.H, width=arm2.W)
# arm_3=box(pos=vec(arm3.x0, arm3.y0, arm3.z0),axis=vec(arm3.a,arm3.b,arm3.c), color=color.orange, length=arm3.L, height=arm3.H, width=arm3.W)

servo_1=cylinder(pos=vec(servo2.x0, servo2.y0, servo2.z0), axis=vec(servo2.a, servo2.b, servo2.c), color=color.green, radius=servo2.r)
servo_2=cylinder(pos=vec(servo1.x0, servo1.y0, servo1.z0), axis=vec(servo1.a, servo1.b, servo1.c), color=color.green, radius=servo1.r)
servo_3=cylinder(pos=vec(servo3.x0, servo3.y0, servo3.z0), axis=vec(servo3.a, servo3.b, servo3.c), color=color.green, radius=servo3.r)
# servo_4=cylinder(pos=vec(servo4.x0, servo4.y0, servo4.z0), axis=vec(servo4.a, servo4.b, servo4.c), color=color.green, radius=servo4.r)

base = cylinder(pos=vec(0, -2, 0), axis=vec(0, 2, 0), color=color.orange, radius=5)

# extrusion(path=paths.arc(pos=vec(18.5, 18, 1.5)), axis=vec(0, 0, -1), angle1=1.57, angle2=2.35, shape=shapes.circle(radius=0.5), up=vec(1,0,0), radius=4, color=color.cyan)

def slider1(s):
    arm_1.rotate(angle==0.1, axis(0,-1,0), origin(0,0,0))
slider( bind=slider1 )
scene.append_to_caption('Th1 \n\n')


while 1:
    rate(20)
    # robot.rotate(angle=0.1, axis=vec(0, -1, 0), origin=vec(0, 0, 0))
    # arm_1.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(0, 0, 0))
    # arm_2.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(0, 10, 0))
    # arm_3.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(10, 10, 0))
    #
    # servo_2.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(0, 0, 0))
    # # servo_3.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(0, 10, 0))
    # servo_4.rotate(angle=0.1, axis=vec(0, 0, 1), origin=vec(10, 10, 0))
