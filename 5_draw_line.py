import numpy as np
import cv2

img = cv2.imread('lena.jpg',1)

print(img.shape)

img = cv2.line(img, (0,0), (255,255), (250,100,0), 5,1)  ##(img, start index, destination, color, thickness)

img = cv2.arrowedLine(img, (0,255), (255,255), (100,0,255), 5, cv2.LINE_4)

img = cv2.rectangle(img, (400,0), (510,100), (100,255,100), 5) ## (x1,y1)Top left,(x2,y2) Bottom right
img = cv2.circle(img,(455,47), 50, (200,100,100), -1)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'OpenCv', (10,400), font, 4, (25,200,250), 10, cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


