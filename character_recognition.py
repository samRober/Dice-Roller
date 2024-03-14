import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import tesserocr as tes
import sys



def read_image(img) -> int:
    ret,thresh2 = cv.threshold(img,130,255,cv.THRESH_BINARY_INV )

    img_rgb = cv.cvtColor(thresh2, cv.COLOR_BGR2RGB)


    return tes.image_to_string(img_rgb, config = r'--psm 10')

if __name__ == "__main__":
    img = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
    print(read_image(img))