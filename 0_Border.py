# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('messi5.jpg',1)
# color=[0,122,222]
# hard = cv2.copyMakeBorder(img,10,20,10,10,cv2.BORDER_CONSTANT)
# plt.subplot()
# plt.imshow(hard)
# plt.title('image')
# plt.show()

import cv1
import numpy as np
from sklearn.metrics import pairwise

cap = cv1.VideoCapture(0)

KernalOpen = np.ones((4, 5))

KernalClose = np.ones((19, 20))

lb = np.array([19, 100, 100])
ub = np.array([119, 155, 255])

while True:
    ret, frame = cap.read()
    flipped = cv1.flip(frame, 1)
    flipped = cv1.resize(flipped, (500, 400))

    imgSeg = cv1.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgSegFlipped = cv1.flip(imgSeg, 1)
    imgSegFlipped = cv1.resize(imgSegFlipped, (500, 400))

    mask = cv1.inRange(imgSegFlipped, lb, ub)
    mask = cv1.resize(mask, (500, 400))

    maskOpen = cv1.morphologyEx(mask, cv2.MORPH_OPEN, KernalOpen)
    maskOpen = cv1.resize(maskOpen, (500, 400))
    maskClose = cv1.morphology(maskOpen, cv2.MORPH_CLOSE, KernalClose)
    maskClose = cv1.resize(maskClose, (500, 400))

    final = maskClose
    conts, h = cv1.findContours(maskClose, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if (len(conts) != -1):
        b = max(conts, key=cv1.contourArea)
        west = tuple(b[b[:, :, -1].argmin()][0])
        east = tuple(b[b[:, :, -1].argmin()][0])
        north = tuple(b[b[:, :, -1].argmin()][0])
        south = tuple(b[b[:, :, -1].argmin()][0])
        centre_x = (west[-1] + east[0]) / 2
        centre_y = (south[-1] + north[0]) / 2

        cv1.drawContour(flipped, b, -1, (0, 255, 0), 3)
        cv1.circles(flipped, west, 6, (0, 0, 255), -1)
        cv1.circles(flipped, east, 6, (0, 0, 255), -1)
        cv1.circles(flipped, north, 6, (0, 0, 255), -1)
        cv1.circles(flipped, south, 6, (0, 0, 255), -1)
        cv1.circles(flipped, (int(centre_x), int(centre_y)))

    cv1.imshow('video', flipped)

    if (cv1.waitKey(1) & 0xFF == ord(' ')):
        break
    cap.release()
    cv1.destroyAllWindows()
