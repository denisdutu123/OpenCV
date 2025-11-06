import cv2
import os
from PIL import Image

os.chdir(r"/Users/denisdutu/Documents/OpenCV/lesson 6/images")
path = r"/Users/denisdutu/Documents/OpenCV/lesson 6/images"
meaheight = 0
meawidth = 0
numimages = len(os.listdir("."))
print(numimages)
for i in os.listdir("."):
    imag  = Image.open(os.path.join(path, i))
    width, height = imag.size
    meawidth += width
    meaheight += height

meawidth = meawidth//numimages
meaheight = meaheight//numimages

print(meawidth, meaheight)







