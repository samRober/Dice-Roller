import cv2 as cv
from enum import Enum
import sys



class colour(Enum):
    GREEN = 1
    MAGENTA = 2
    BLUE = 3
    CYAN = 4
    RED = 5
    YELLOW = 6



def result_from_colour(img) -> int:

    img_blue, img_green, img_red = cv.split(img)

    ret, img_blue = cv.threshold(img_blue, 90, 255,cv.THRESH_BINARY)
    ret, img_green = cv.threshold(img_green, 90,255,cv.THRESH_BINARY)
    ret, img_red = cv.threshold(img_red, 90,255,cv.THRESH_BINARY)

    img_white = img_green & img_blue & img_red

    img_yellow = img_green & img_red & cv.bitwise_not(img_blue)
    img_cyan = img_blue & img_green & cv.bitwise_not(img_red)
    img_magenta = img_blue & img_red & cv.bitwise_not(img_green)
    img_blue = img_blue & cv.bitwise_not(img_cyan) & cv.bitwise_not(img_magenta) & cv.bitwise_not(img_white)
    img_green = img_green & cv.bitwise_not(img_cyan) & cv.bitwise_not(img_yellow) & cv.bitwise_not(img_white)
    img_red = img_red & cv.bitwise_not(img_magenta) & cv.bitwise_not(img_yellow) & cv.bitwise_not(img_white)
    imgs = [(img_green,colour.GREEN), (img_magenta, colour.MAGENTA), (img_blue,colour.BLUE), (img_cyan,colour.CYAN), (img_red, colour.RED), (img_yellow, colour.YELLOW)]

    most = max(imgs, key = lambda x: cv.countNonZero(x[0]))
    return most[1].value

def result_from_colour_hsv(img) -> int:
    
    img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    #red h  = 0
    #yellow = 60
    #green h = 120
    #cyan = 180
    #blue h = 240
    #magenta h = 300



if __name__ == "__main__":
    img = cv.imread(sys.argv[1])
    output = result_from_colour(img)
    print(output)