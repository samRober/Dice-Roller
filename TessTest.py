import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pytesseract as tes
import sys

img = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh2 = cv.threshold(img,130,255,cv.THRESH_BINARY_INV )

img_rgb = cv.cvtColor(thresh2, cv.COLOR_BGR2RGB)
titles = ['Original Image','threashold']
images = [img, thresh2]
for i in range(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
print(tes.image_to_string(img_rgb, config = r'--psm 10'))
