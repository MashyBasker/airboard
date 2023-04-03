import cv2
import numpy as np
import sys


class Tracker:

    def __init__(self):
        pass
    
    # create a box around a red area which will act as the airboard pen
    def make_box(self, frame) -> tuple:
        """
        @params:    None
        @return:    Tuple containing coordinates for the colour box 
        """

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        contour, _ = cv2.findContours(mask.copy(),
                                    cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)

        if len(contour) > 0:
            red_area = max(contour, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(red_area)
                
        return (x, y, w, h)

    def get_box_mid(self, bbox) -> tuple:
        """
        @params:    4 tuple containing information for the box coordinates
        @return:    2 tuple containing coodinates for the box mid point
        """

        tlx, tly = bbox[0], bbox[1]     # top left x and y coordinates
        brx, bry = tlx + bbox[2], tly + bbox[3] # bottom right x and y coordinates
        mid_x = (tlx + brx) // 2        # getting the mid x coordinate
        mid_y = (tly + bry) // 2        # getting themid y coordinate

        return (mid_x, mid_y)           # return as tuple


    # tracks the boxed area in the video
    def track_object(self, check, frm, tracker, __contours):
        """
        @params:    video object, tracker instance
        @return:    None 
        """
        if not check:
            sys.exit()

        print(__contours)
        ok, bbox = tracker.update(frm)      # box area around tracking object
        mid_point = self.get_box_mid(bbox)  # get the midpoint of that box
        print(mid_point)

        if ok:
            a = [int(mid_point[0]), int(mid_point[1])]
            k = []
            k.append(a)
            __contours.append(k.copy())
            __contours = np.array(__contours)
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frm, p1, p2, (255,0,0), 2)
            print(type(__contours))
            print(__contours.shape)
            cv2.drawContours(frm, __contours, -1, (0, 255, 0), 3)
        else:
            cv2.putText(frm, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        cv2.imshow("Airboard", frm)
        if cv2.waitKey(1) == 'q':
            cv2.destroyAllWindows()



        


