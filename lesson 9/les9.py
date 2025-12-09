import cv2
import numpy as np
import random

cam = cv2.VideoCapture(0)
cap, fram1 = cam.read()
cap, fram2 = cam.read()
ball = []
total = 10
score = 0
font = cv2.FONT_HERSHEY_SIMPLEX

for i in range(total):
    x = random.randint(0, 1500)
    y = random.randint(0, 1500)
    size = random.randint(18, 40)
    ball.append({'x':x, 'y':y, 'r':size, 'popped': False})
    
while True:   
    diff = cv2.absdiff(fram1, fram2)
    grscal = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blu = cv2.GaussianBlur(grscal, (5, 5), 0)
    _, thresh = cv2.threshold(blu, 20, 255, cv2.THRESH_BINARY)
    dilat = cv2.dilate(thresh, None, iterations = 3)
    contours, _ = cv2.findContours(dilat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cfram = fram1.copy()
    for i in ball:
        if not i["popped"]:
            cv2.circle(cfram, (i["x"], i["y"]), i["r"], (255, 0, 0), -1)

    #motion overlap
    for a in contours:
        if cv2.contourArea(a) < 1500:
            continue
        x, y, wid, hei = cv2.boundingRect(a)
        #centre of motion
        centmot = (x + wid // 2, y +hei // 2)
        cv2.rectangle(cfram, (x, y), (x + wid, y + hei), (89, 233, 12), 7)
        for q in ball:
            if not q["popped"]:
                dist = np.linalg.norm(np.array(centmot) - np.array((q["x"], q["y"])))
                if dist < q["r"] + 10:
                    q["popped"]  = True
                    score +=1
                    
    #showing frame with balloons
    cv2.putText(cfram, "Popped balloons:" + str(score), (100, 1000), font, 1, (123, 56, 234), 4)
    cv2.imshow("balloon", cfram)
    fram1 = fram2
    cap, fram2 = cam.read()
    key = cv2.waitKey(30)
    if key == 27:
        break


cam.release()
cv2.destroyAllWindows()
