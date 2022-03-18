import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 325:385]
img[270:330, 100:160] = ball
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()