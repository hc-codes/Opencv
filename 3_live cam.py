#This code is used to capture live video from camera and
#It also captures image from the live video stream....

import cv2

cam= cv2.VideoCapture(0)  #cam is the video recording object and the method captures live videos from the camera


print(cam.isOpened())#Check for open object

while(cam.isOpened()):

    ret, frame = cam.read()#read from camera by frames boolean,frame

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY) #convert rgb to gray

        print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
       # cv2.imshow('frame', frame)     ##  line 13 ref(ret,frame)

        cv2.imshow('Gray',gray)         ##  line gray=cv2.cvtcolor()

        if cv2.waitKey(1)==ord('q'): #close te window when user press 'q'
            break
    else:
        print("Error")
        break
cam.release()

cv2.destroyWindow('frame')