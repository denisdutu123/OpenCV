import cv2
import numpy as np
clic = False
re = gree = blu = x = y = 0

def mous(even, xx, yy, flags, param):
    global re, gree, blu, x, y, clic
    if even == cv2.EVENT_LBUTTONDOWN:
        clic = True
        x = xx
        y = yy
        blu, gree, re = fra[yy, xx]
        blu = int(blu)
        gree = int(gree)
        re = int(re)

cap = cv2.VideoCapture(0)
cv2.namedWindow('window')
cv2.setMouseCallback('colour detection', mous)
while True :
    ret, fra = cap.read()
    if ret == False:
        break
    if clic == True:
        cv2.rectangle(fra, (20, 20), (650, 91), (blu, gree, re), -1)
        tex = f'R = {re} G={gree} B={blu}'
        texcol = (255, 255, 255) if re + gree + blu < 600 else (0, 0, 0)
        cv2.putText(fra, tex, (150, 200), 2, 0.6, texcol, 7, cv2.LINE_AA)
    cv2.imshow("colour", fra)
    key = cv2.waitKey(10)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
