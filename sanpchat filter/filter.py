import cv2
dat = cv2.data.haarcascades
import os
fil = ["haarcascade_frontalface_default.xml", "haarcascade_frontalface_alt.xml"]
for i in fil:
    path = os.path.join(dat, i)
    print(i, "found" if os.path.exists(path) else "not found")