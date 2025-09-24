import os
import cv2

img = cv2.imread(os.path.join('./data', 'ayam.jpg'))
img_resized = cv2.resize(img, (118,300))

print(img.shape)
print(img_resized.shape)
cv2.imshow('img',img)
cv2.imshow('img_resized', img_resized)
cv2.waitKey(0)
