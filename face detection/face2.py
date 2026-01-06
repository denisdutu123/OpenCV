import cv2
import numpy as np
import os

casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
fold = "datasets"
print("Put your face in good lighting")
#creating list of images
(imag, lab, nam, id) = ([], [], {}, 0)
for (subdir, maidir, individ) in os.walk(fold):
    for subdir in maidir:
        nam[id] = subdir 
        pat = os.path.join(fold, subdir)
        for i in os.listdir(pat):
            pa = pat + '/' + i
            idnlab = id
            imag.append(cv2.imread(pa, 0))
            lab.append(int(idnlab))
        id+=1
(wid, hei) = (230, 150)
#creating numpy array
(imag, lab) = [np.array(n) for n in [imag, lab]]
#training the model
mod = cv2.face.LBPHFaceRecognizer_create()
mod.train(imag, lab)
capt = cv2.VideoCapture(0)
while True:
    (_,im) = capt.read()
    grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = fold.detectMultiScale(grey, 1.3, 4)
    #looping through detcted faces
    for (x, y, wid, hei) in faces:
        cv2.rectangle(im, (x, y), (x+wid, y+hei), (213, 14, 134), 6)
        singular = grey[y:y+hei, x:x+wid]
        resized = cv2.resize(singular, (wid, hei))
        #trying to recgonise the face
        predi = mod.predict(resized)
        cv2.rectangle(im, (x, y), (x+wid, y+hei), (213, 14, 134), 6)
        if predi[1] < 500:
            cv2.putText(im, '% s - %.0f' %(nam[predi[0]], predi[1]),(x - 10, y - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (123, 233, 9), 7)
        else:
            cv2.putText(im, "not recognised", (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, (245, 34, 187), 6)
        cv2.imshow("face recogniser", im)
        key = cv2.waitKey(10)
        if key == 27:
            break
        
            
            
        
        