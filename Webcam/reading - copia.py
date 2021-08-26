import cv2
from moviepy.editor import *
import numpy as np

cv2.namedWindow("LA PYTHONA")
cv2.namedWindow("Movement")
vc = cv2.VideoCapture(0)
cam = vc
frames = []
video_count=1

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)


def read():
    rval, frame = vc.read()
    frame = cv2.flip(frame, 1)

    frame2 = cam.read()
    frame2 = diffImg(t_minus, t, t_plus)
    frame2 = cv2.flip(frame2, 1)
    key = cv2.waitKey(20)

key = cv2.waitKey(20)
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
frame2 = diffImg(t_minus, t, t_plus)

while rval:
    # Shows webcam footage on screen
    cv2.imshow("LA PYTHONA", frame)
    cv2.imshow("Movement", frame2)

    # Compares three images in grayscale
    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    read()

    bright_pixels = np.sum(frame2 >= 50)

    if key == 27:
        break

    print(str(bright_pixels))

    # Adjust senstitivity in this number and in the bright pixels threshold
    if bright_pixels > 3:
        # This will save a minute of video footage after detecting movement.
        for i in range(0, 1620, 1):
            read()

            cv2.imwrite("seq/img_" + str(i) + ".png", frame)
            frames.append("seq/img_" + str(i) + ".png")

            clip = ImageSequenceClip(frames, 27)
            clip.write_videofile("vid_" + str(video_count) + ".mp4")


cv2.destroyWindow("LA PYTHONA")
cv2.destroyWindow("Movement")
