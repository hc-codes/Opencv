import cv2

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))

cap.set(3,3000)
cap.set(4,3000)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):

    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame,1)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
cv2.release()
cv2.destroyAllWindows()