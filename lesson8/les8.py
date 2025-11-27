import cv2
import numpy as np

print("Welcome to the filter app")
print(" 0 - original\n 1 - Grayscale\n 2 - Sepia\n 3 - Negative\n 4 - cartoon\n 5 - mirror\n q- quit")
cam = cv2.VideoCapture(0)
filtyp = "original"
while True:
    captu, fram = cam.read()
    if not captu:
        break
    if filtyp == "grayscale":
        fram = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
    elif filtyp == "sepia":
        sep = np.array(([[0.35, 0.45, 0.10], [0.40, 0.50, 0.12], [0.45, 0.55, 0.15]  ]))
        sepfram = cv2.transform(fram, sep)
        fram = np.clip(sepfram, 0, 255).astype(np.uint8)
    elif filtyp == "negative":
        fram = cv2.bitwise_not(fram)
    elif filtyp == "cartoon":
        gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edg = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        colo = cv2.bilateralFilter(fram, 9, 300, 300)
        fram = cv2.bitwise_and(colo, colo, mask = edg)
    elif  filtyp == "mirror":
        fram = cv2.flip(fram, 1)

    #showing video output
    cv2.imshow("output of image", fram)
    #key pressing event
    key = cv2.waitKey(1)
    if key == ord("0"):
        filtyp = "original"
    elif key == ord("1"):
        filtyp = "grayscale"
    elif key == ord("2"):
        filtyp = "sepia"
    elif key ==ord("3"):
        filtyp = "negative"
    elif key == ord("4"):
        filtyp = "cartoon"
    elif key == ord("5"):
        filtyp = "mirror"
    elif key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

    