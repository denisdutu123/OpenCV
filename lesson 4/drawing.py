import cv2

imag = cv2.imread("image.jpg")

#draw line
first = (200, 40)
second = (650, 450)
colo = (234, 90, 189)
thick = 6
ima = cv2.line(imag, first, second, colo, thick)
cv2.imshow("drawn line", ima)
cv2.waitKey(0)
cv2.destroyAllWindows()

#drawing rectangl                              #change the thickness to -1 to fill in the shape
image = cv2.imread("image.jpg")
fir = (200, 100)
secon = (500, 30)
col = (120, 254, 56)
thic = 10
im = cv2.rectangle(image, fir, second, col, thic)
cv2.imshow("rectangel", im)
cv2.waitKey(0)

# drawing circle

imagg = cv2.imread("image.jpg")
fi = (350, 200)
colou = (167, 23, 199)
thi = 9
radius = 50
i = cv2.circle(imagg, fi, radius, colou, thi )
cv2.imshow("circle", i)
cv2.waitKey()

#drawing text

imaggg = cv2.imread("image.jpg")
fontsty = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
fontsca = 3
c = (230, 11, 210)
firr = (120, 300)
th = 12
imm = cv2.putText(imaggg, "It's Thursday", firr, fontsty, fontsca, c, th, cv2.LINE_AA)
cv2.imshow("text", imm)
cv2.waitKey(0)