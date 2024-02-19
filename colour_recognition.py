import cv2 as cv
from enum import Enum
import sys

img = cv.imread(sys.argv[1])

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

cv.imwrite("yellow.jpg", img_yellow)
cv.imwrite("cyan.jpg", img_cyan)
cv.imwrite("magenta.jpg", img_magenta)
cv.imwrite("blue.jpg", img_blue)
cv.imwrite("green.jpg", img_green)
cv.imwrite("red.jpg", img_red)


class colour(Enum):
    GREEN = 1
    MAGENTA = 2
    BLUE = 3
    CYAN = 4
    RED = 5
    YELLOW = 6

imgs = [(img_green,colour.GREEN), (img_magenta, colour.MAGENTA), (img_blue,colour.BLUE), (img_cyan,colour.CYAN), (img_red, colour.RED), (img_yellow, colour.YELLOW)]

most = max(imgs, key = lambda x: cv.countNonZero(x[0]))
print(most[1].value)