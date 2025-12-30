import cv2
import numpy as np
import os

casca = "haarcascade_frontalface_default.xml"
data = "datasets"
subfold = "denis"
path = os.path.join(data, subfold)
if not os.path.isdir(path):
    os.mkdir(path)
#setting standerds size for face images
(widt, heig) = (230, 150)

fol = cv2.CascadeClassifier(casca)
camer = cv2.VideoCapture(0)
capt = 0
while capt < 30:
    (_,im) = camer.read()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = fol.detectMultiScale(grey, 1.12, 4)
    #looping through detcted faces
    for (x, y, wid, hei) in faces:
        cv2.rectangle(im, (x, y), (x+wid, y+hei), (213, 14, 134), 6)
        singular = grey[y:y+hei, x:x+wid]
        resized = cv2.resize(singular, (widt, heig))
        cv2.imwrite('%s/%s.png'(path, capt), resized)
        
    
    
    