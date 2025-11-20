import cv2
import os
import numpy as np
import time

vid = cv2.VideoCapture(r"/Users/denisdutu/Documents/OpenCV/lesson7/video.mp4")

if not vid.isOpened():
    print("The video could not be opened")
    exit()
time.sleep(1)
fram = 0
back = None

for i in range(60):
    decis, outpu = vid.read()
    if not decis:
        print("skipping frame")
        continue
    back = outpu
if back is None:
    print("no frame could be read")
    exit()
back = np.flip(outpu, axis = 1)

#starting invisibility process

while vid.isOpened():
    decis, outpu = vid.read()
    if not decis:
        break
    fram +=1
    outpu = np.flip(outpu, axis = 1)
    hsv = cv2.cvtColor(outpu, cv2.COLOR_BGR2HSV)
    #lighter red color
    
    lowred  =np.array([0, 150, 50])
    upred  =np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lowred, upred)
    
    #darker red colour
    
    lowred2  =np.array([170, 150, 50])
    upred2  =np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lowred2, upred2)
    combine = mask1 + mask2
    combine = cv2.morphologyEx(combine, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8), iterations = 3)
    combine = cv2.morphologyEx(combine, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8), iterations = 3)
    combine = cv2.dilate(combine, np.ones((5, 5), np.uint8), iterations = 2)
    invermask = cv2.bitwise_not(combine)
    invmask = cv2.bitwise_and(back, back, mask = combine)
    invrrmask = cv2.bitwise_and(outpu, outpu, mask = invermask)
    finout = cv2.addWeighted(invmask, 1, invrrmask, 1, 0)
    cv2.imshow("final video", finout)
    if cv2.waitKey(10)== 27:
        break

vid.release()
cv2.destroyAllWindows()
    
    





