import cv2 as cv
from enum import Enum
import numpy as np
import sys



class colour(Enum):
    GREEN = 1
    MAGENTA = 2
    BLUE = 3
    CYAN = 4
    RED = 5
    YELLOW = 6

def get_most_colour(img_red,img_green,img_blue,img_cyan,img_yellow,img_magenta):
    imgs = [(img_green,colour.GREEN), (img_magenta, colour.MAGENTA), (img_blue,colour.BLUE), (img_cyan,colour.CYAN), (img_red, colour.RED), (img_yellow, colour.YELLOW)]

    most = max(imgs, key = lambda x: cv.countNonZero(x[0]))
    return most[1].value

def result_from_colour(img) -> int:

    img_blue, img_green, img_red = cv.split(img)

    ret, img_blue = cv.threshold(img_blue, 0, 255,cv.THRESH_BINARY)
    ret, img_green = cv.threshold(img_green, 90,255,cv.THRESH_BINARY)
    ret, img_red = cv.threshold(img_red, 90,255,cv.THRESH_BINARY)

    img_white = img_green & img_blue & img_red

    img_yellow = img_green & img_red & cv.bitwise_not(img_blue)
    img_cyan = img_blue & img_green & cv.bitwise_not(img_red)
    img_magenta = img_blue & img_red & cv.bitwise_not(img_green)
    img_blue = img_blue & cv.bitwise_not(img_cyan) & cv.bitwise_not(img_magenta) & cv.bitwise_not(img_white)
    img_green = img_green & cv.bitwise_not(img_cyan) & cv.bitwise_not(img_yellow) & cv.bitwise_not(img_white)
    img_red = img_red & cv.bitwise_not(img_magenta) & cv.bitwise_not(img_yellow) & cv.bitwise_not(img_white)
    
    return get_most_colour(img_red,img_green,img_blue,img_cyan,img_yellow,img_magenta)

def result_from_colour_hsv(img) -> int:
    
    img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    #red h  = 0
    #yellow = 30
    #green h = 60
    #cyan = 90
    #blue h = 120
    #magenta h = 150
    img_red = get_red_hsv(img_hsv)
    img_green = get_green_hsv(img_hsv)
    img_blue = get_blue_hsv(img_hsv)
    img_yellow = get_yellow_hsv(img_hsv)
    img_cyan = get_cyan_hsv(img_hsv)
    img_magenta = get_magenta_hsv(img_hsv)
    cv.imwrite("img_colour.jpg",img_cyan)
    return get_most_colour(img_red,img_green,img_blue,img_cyan,img_yellow,img_magenta)

def get_red_hsv(img):
    lower_red_1 = np.array([0,175,20])
    higher_red_1 = np.array([10,255,255])

    lower_red_2 = np.array([170,175,20])
    higher_red_2 = np.array([180,255,255])

    red_1 = cv.inRange(img,lower_red_1,higher_red_1)
    red_2 = cv.inRange(img,lower_red_2,higher_red_2)

    return red_1|red_2

def get_green_hsv(img):
    lower = np.array([50,175,20])
    higher = np.array([70,255,255])
    return cv.inRange(img,lower,higher)

def get_blue_hsv(img):
    lower = np.array([110,175,20])
    higher = np.array([130,255,255])
    return cv.inRange(img,lower,higher)

def get_yellow_hsv(img):
    lower = np.array([20,175,20])
    higher = np.array([40,255,255])
    return cv.inRange(img,lower,higher)

def get_cyan_hsv(img):
    lower = np.array([80,175,20])
    higher = np.array([100,255,255])
    return cv.inRange(img,lower,higher)

def get_magenta_hsv(img):
    lower = np.array([140,175,20])
    higher = np.array([169,255,255])
    return cv.inRange(img,lower,higher)

if __name__ == "__main__":
    img = cv.imread("img.jpg")
    output = result_from_colour_hsv(img)
    print(output)