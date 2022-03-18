#This code is used to capture live video from camera and
#It also captures image from the live video stream....

import cv2

cam= cv2.VideoCapture(0)  #cam is the video recording object and the method captures live videos from the camera

fourcc = cv2.VideoWriter_fourcc(*'XVID')# video codeccs
out=cv2.VideoWriter('VideoOutput.avi',fourcc,20, (640,480))#Video writer Object opname,codecs,framerate,frame size

print(cam.isOpened())#Check for open object


f=0
while(cam.isOpened()):

    ret, frame = cam.read()#read from camera by frames

    if ret:
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        cv2.imshow('frame', frame)

        #cv2.imshow('Gray',gray)



        if cv2.waitKey(1)==ord('c'):
            cv2.imwrite('new.jpg',frame )
            f=1
            break

        if cv2.waitKey(1)==ord('q'):
            f=0
            break
    else:
        break
cam.release()
out.release()
cv2.destroyWindow('frame')
if f==1:
    img= cv2.imread('new.jpg',0) #Capturing Image from Video
    cv2.imshow('Preview',img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
cam= cv2.VideoCapture('VideoOutput.avi')
FrameTime =10
while(cam.isOpened()):

    ret, frame = cam.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(30) ==ord('r'):
        break
cam.release()
cv2.destroyAllWindows()