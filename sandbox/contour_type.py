import cv2
import numpy as np


img = cv2.imread("../assets/star.png")
print(img.shape)
s = np.zeros((880, 860, 3), dtype="uint8")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
c, h = cv2.findContours(edged, cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_NONE)
print(type(c))
a = c[0]
print(type(a))
print(a.shape)
print(a)
# b = np.squeeze(a)
# print(b.shape)
#print(np.squeeze(a))
cv2.drawContours(s, a, -1, (0, 255, 0), 3)
cv2.imshow('dwnq', s)
q = cv2.waitKey(0)
if q == 'q':
    cv2.destroyAllWindows()


