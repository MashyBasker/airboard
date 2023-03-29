import cv2
import numpy as np


class Tracker:

    def __init__(self):
        pass

    def detect_object(first_frame):
        hsv = cv2.cvtColor(first_frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])
        