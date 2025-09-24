import os
import cv2

img = cv2.imread(os.path.join('./data', 'whiteboard.png'))

#line
cv2.line(img, (100,150), (300, 450), (0,255,0), 3)

#rectangle
cv2.rectangle(img, (200,350), (450, 600), (0, 0, 255), 5)

#circle , 3rd param s radius
cv2.circle(img, (500, 550), 50, (255,0,0), 5)

#text
cv2.putText(img, 'Hey you !', (600,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0), 10)

cv2.imshow('img', img)
cv2.waitKey(0)