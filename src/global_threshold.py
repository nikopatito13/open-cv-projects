import cv2
import os

img = cv2.imread(os.path.join('./data', 'ayam.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, tresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
cv2.blur(tresh, (40,40))
ret, tresh = cv2.threshold(tresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img_gray', img_gray)
cv2.imshow('img', img)
cv2.imshow('tresh', tresh)
cv2.waitKey(0)