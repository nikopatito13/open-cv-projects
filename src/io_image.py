import os
import cv2

#read image
image_path = os.path.join('.', 'data', 'ayam.jpg')

img = cv2.imread(image_path)

#read image
cv2.imwrite(os.path.join('.', 'data', 'ayam_out.jpg'), img)
cv2.imshow('image', img)
cv2.waitKey(0)

