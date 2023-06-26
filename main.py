import cv2
print(cv2.__version__)
img = cv2.imread('digital-neon.jpg')

cv2.imshow('Display Image', img)
cv2.waitKey(0)
