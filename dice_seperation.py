import cv2 as cv
import numpy as np
import sys



def seperate_image(img):
    img_grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    ret,edges = cv.threshold(img_grey,30,255,cv.THRESH_BINARY)
    kernel = np.ones((5,5),np.uint8)
    edges = cv.erode(edges,kernel,iterations=8)
    edges = cv.dilate(edges,kernel,iterations=6)
    #cv.imwrite("edges.png",edges)
    contours, hierarchy = cv. findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img,contours,-1,(255,0,253),5)
    cv.imwrite("contours.png",img)
    seperate_images = []
    for contour in contours:
        rect = cv.minAreaRect(contour)
        points = cv.boxPoints(rect)
        width_vec = points[0] - points[1]
        height_vec = points[0] - points[3]
        box_width = cv.norm(width_vec)
        box_height = cv.norm(height_vec)
        if box_width < 150 or box_width > 275:
            continue
        if box_height < 150 or box_height > 275:
            continue   
        dest_points = np.array([[0,0],[box_width,0],[box_width,box_height]]).astype(np.float32)
        matrix = cv.getAffineTransform(points[:3],dest_points)
        seperate_images.append(cv.warpAffine(img,matrix,(int(box_width),int(box_height))))
    return seperate_images

if __name__ == "__main__":
    img = cv.imread("img.jpg")
    seperate_images = seperate_image(img)
    count = 0
    for i in seperate_images:
        cv.imwrite(str(count) +".png",i)
        count +=1