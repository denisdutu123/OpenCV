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
    x = random.randint(0, 500)
    y = random.randint(0, 500)
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
        if not ball["popped"]:
            cv2.circle(cfram, (ball["x"], ball["y"]), ball["r"], (255, 0, 0), -1)
    


