import cv2
import numpy as np
fil = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
load = cv2.imread("galsses.png")
hei, wid = load.shape[:2]
ratio = wid/hei
#function for putting glasses on face
def glass(back, overlay, x, y):
    backh, backw = back.shape[:2]
    heig, widt = overlay.shape[:2]
    if x < 0 or y < 0 or x + widt > backw or y + heig > backh:
        return back
    if overlay.shape[2] == 4:
        
        transpar = overlay[:, :, 3]/255.0
    else:
        transpar = np.ones((overlay.shape[0], overlay.shape[1]))
        
    #mixing glasses pixels and camera pixels
    for n in range(3):
        back[y: y + heig, x: x + widt, n] = ((1 - transpar)*back[y: y + heig, x: x + widt, n] + transpar*overlay[:, :, n])
    return back
#turning on camera
cam = cv2.VideoCapture(0)
print("press q to quit")

while True:
    cap, fra = cam.read()
    if cap == False:
        break
    grey = cv2.cvtColor(fra, cv2.COLOR_BGR2GRAY)
    #detecting faces
    fac = fil.detectMultiScale(grey, scaleFactor = 1.1, minNeighbors = 5, minSize = (80, 80))
    for (x, y, widt, heig) in fac:
        glasses_widt = widt
        glasses_heig = int(glasses_widt / ratio)
        resize = cv2.resize(load, (glasses_widt, glasses_heig))
        eylev = y + int(heig * 0.35)
        fra= glass(fra, resize, x, eylev)
    cv2.imshow("glasses filter", fra)
    if cv2.waitKey(1) == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()