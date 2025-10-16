import cv2
import os
#print(cv2.__version__)

read = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", read)
cv2.waitKey(0)
#black and white image read

read1 = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", read1)
cv2.waitKey(0)
#saving changes

path = "/Users/denisdutu/Documents/OpenCV/"
os.chdir(path)
cv2.imwrite("second image.jpg", read1)
print("Image saved")

#splitting image in rgb

read2 = cv2.imread("rgb.jpg", cv2.IMREAD_COLOR)
blue, green, red = cv2.split(read2)
cv2.imshow("image", read2)
cv2.waitKey(0)
cv2.imshow("image", blue)
cv2.waitKey(0)
cv2.imshow("image", green)
cv2.waitKey(0)
cv2.imshow("image", red)
cv2.waitKey(0)