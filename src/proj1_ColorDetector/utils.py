import numpy as np
import cv2

def get_limits(color):

    c = np.uint8([color]) #BGR color to convert to HSV
    hsvC= cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = np.array(lower_limit, dtype=np.uint8)
    upper_limit = np.array(upper_limit, dtype=np.uint8)

    return upper_limit, lower_limit