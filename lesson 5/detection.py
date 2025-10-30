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