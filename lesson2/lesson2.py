import cv2
import numpy as np

#addition of 2 images
im1 = cv2.imread("image1.jpg")
im2 = cv2.imread("image2.jpg")
add = cv2.addWeighted(im1, 0.5, im2, 0.5, 0)
cv2.imshow("merged images", add)
cv2.waitKey(0)

#opposite of adding
i1 = cv2.imread("img1.jpg")
i2 = cv2.imread("img2.jpg")
sub = cv2.subtract(i1, i2)
cv2.imshow("sub images", sub)
cv2.waitKey(0)

#resize image
imag1 = cv2.imread("1bit.png")
imag2 = cv2.imread("2bit.png")
res1 = cv2.resize(imag1, (30, 90))
res2 = cv2.resize(imag2, (600, 800))
cv2.imshow("resized image", res1)
cv2.waitKey(0)
cv2.imshow("resi image", res2)
cv2.waitKey(0)

