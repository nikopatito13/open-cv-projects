import cv2
from utils import get_limits

cap= cv2.VideoCapture(1)

yellow = [0,255, 255] # yellow in BGR
while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtcolor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=yellow)
    
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

    cv2.destroyAllWindows()

    

