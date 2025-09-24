import os
import cv2

img = cv2.imread(os.path.join('./data', 'handwritten.png'))
img_resized = cv2.resize(img, (800,800))

img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
ret, simple_thresh = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY)
adaptive_threshthresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
#print(img.shape)

cv2.imshow('img_resized', img_resized)
cv2.imshow('simple_thresh', simple_thresh)
cv2.imshow('adaptive_threshthresh', adaptive_threshthresh)


cv2.waitKey(0)