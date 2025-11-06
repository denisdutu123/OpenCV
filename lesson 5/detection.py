import cv2
import numpy as np

image = cv2.imread("download.jpeg")

#converting to grey scale

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blu = cv2.blur(grey, (3, 3))
cv2.imshow("original", image)
cv2.waitKey(0)
cv2.imshow("grey", grey)
cv2.waitKey(0)
cv2.imshow("blured", blu)
cv2.waitKey(0)

dete = cv2.HoughCircles(blu, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 45)
if dete is not None:
    dete = np.uint16(np.around(dete))
    for i in dete[0, :]:
        x, y, r = i[0], i[1], i[2]
        cv2.circle(image, (x, y), r, (198, 15, 231), 7)
        cv2.circle(image, (x, y), 1, (198, 15, 231), 7)
        cv2.imshow("Circle", image)
        cv2.waitKey(0)
cv2.destroyAllWindows()
