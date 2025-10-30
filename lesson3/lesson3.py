import cv2
import numpy as np

#erosion
ima = cv2.imread("image.jpg")
kernel = np.ones((5, 5), np.uint8)
eros = cv2.erode(ima, kernel)

cv2.imshow("original", ima)
cv2.waitKey(0)
cv2.imshow("erosion", eros)
cv2.waitKey(0)
cv2.destroyAllWindows()
#bordering

ima1 = cv2.imread("image.jpg")
#solid border
bord = cv2.copyMakeBorder(ima1, 12, 12, 12, 12, cv2.BORDER_CONSTANT, value = (123, 45, 245))
cv2.imshow("border", bord)
cv2.waitKey(0)
#reflective border
ima1 = cv2.imread("image.jpg")
ref = cv2.copyMakeBorder(ima1, 20, 20, 20, 20, cv2.BORDER_REFLECT, value = 1)
cv2.imshow("reflect", ref)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blurring
image1 = cv2.imread("image.jpg")
#median blur
low = cv2.medianBlur(image1, 5)
cv2.imshow("image1", low)
cv2.waitKey(0)
#bilateral filter
bila = cv2.bilateralFilter(image1, 8, 78, 68)
cv2.imshow("filter", bila)
cv2.waitKey(0)


#GaussianBlur
gaus = cv2.GaussianBlur(ima, (7, 7), 0)
cv2.imshow("GaussianBlur", gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
