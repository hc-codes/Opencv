import cv2
import datetime

cap = cv2.VideoCapture(0)

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: "+ str(cap.get(3)) + " & Height: "+ str(cap.get(4))
        frame = cv2.putText(frame, text, (10,50), font, 1, (111,11,111), 2, cv2.LINE_AA)

        datet = str(datetime.datetime.now())
        # txt = "Date: "+ str(datetime.datetime.date(2,9,9)) +", Time: "+ str(datetime.datetime.time(1,1,1))
        frame = cv2.putText(frame, datet, (10, 470), font, 1, (11, 121, 111), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cv2.release()
cv2.destroyAllWindows()
