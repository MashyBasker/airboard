import numpy as np
import cv2

img = np.zeros((512, 512, 1), dtype="uint8")
x = range(200)
y = range(200)

a = []
for i in range(200):
    s = [x[i], y[i]]
    k = []
    k.append(s)
    a.append(k.copy())
a = np.array(a)
print(a.shape)
print(type(a))
cv2.drawContours(img, a, -1, (0, 255, 0), 2)
cv2.imshow("hd", img)
k = cv2.waitKey(0)
if k == "q":
    cv2.destroyAllWindows()



