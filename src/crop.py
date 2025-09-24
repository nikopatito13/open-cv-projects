import os

import cv2

img = cv2.imread(os.path.join('./data', 'ayam.jpg'))

print(img.shape)

cropped_img = img[200:700, 120:1200]

cv2.imshow('img', img)  
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)