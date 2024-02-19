import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pytesseract as tes
import sys

img = cv.imread("test.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh2 = cv.threshold(img,130,255,cv.THRESH_BINARY )
cv.imshow("Threashold", thresh2)
cv.waitKey(0)
edged = cv.Sobel(thresh2,25,50)
cv.imshow("edged", edged)
cv.waitKey(0)
contours, hierarchy = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contour_img = thresh2.copy()
cv.drawContours(contour_img, contours, -1, (0,255,0),5)
cv.imshow("contour", contour_img)
cv.waitKey(0)
rect = cv.minAreaRect(contours[0])
box = cv.boxPoints(rect)
box = np.intp(box)
cv.drawContours(contour_img,[box],0,(0,0,255),2)
cv.imshow("box", contour_img)
cv.waitKey(0)