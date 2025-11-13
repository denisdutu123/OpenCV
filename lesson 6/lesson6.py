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

for i in os.listdir("."):
    if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".avif"):
        imag  = Image.open(os.path.join(path, i))
        width, height = imag.size
        print(width, height)
        resi = imag.resize((meawidth, meaheight), Image.LANCZOS)
        resi.save(i, "JPEG", quality = 95)
        print("image is resized")

#functiong for generating video

def vid():
    namvid = "Formula 1.avi"
    os.chdir(r"/Users/denisdutu/Documents/OpenCV/lesson 6/images")
    filnam = []
    for i in os.listdir("."):
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".avif"):
            filnam.append(i)
    print(filnam)
    lis = cv2.imread(os.path.join(".", filnam[0]))
    hei, wid, lay = lis.shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    vid = cv2.VideoWriter(namvid, fourcc, 1, (wid, hei))
    for n in filnam:
        vid.write(cv2.imread(os.path.join(".", n)))
    cv2.destroyAllWindows()
    vid.release()
    print("video is created", vid)
    

   


vid()
        
    
    
        
    







