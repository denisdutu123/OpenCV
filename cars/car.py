import cv2
ca = cv2.VideoCapture('cars.mp4')
ca1 = cv2.CascadeClassifier('cars.xml')

while True:
    #reading single frame, ret = true when fra is read otherwise false
    ret, fra = ca.read()
    if ret == False:
        break
    gre = cv2.cvtColor(fra, cv2.COLOR_BGR2GRAY)
    caa = ca1.detectMultiScale(gre, scaleFactor= 1.1, minNeighbors= 1)
    for (x, y, w, h) in caa:
        cv2.rectangle(fra, (x, y), (x + w, y + h), (123, 213, 69), 5)
    cv2.imshow('cars', fra)
    if cv2.waitKey(10) == 27:
        break
ca.release()
cv2.destroyAllWindows()