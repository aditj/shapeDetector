import cv2
import numpy as np
import imutils
import os

path="~/Documents/cod/"
kernel=np.ones((5,5),np.uint8)
image=cv2.imread("45.png")
hsvimage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
def win_col(max_value,min_value,name):
    global image,hsvimage,kernel
    mask = cv2.inRange(hsvimage, min_value, max_value)
    mask=cv2.erode(mask,kernel,iterations=1)
    image1=cv2.bitwise_and(image,image,mask=mask)
    cnts,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cnts = imutils.grab_contours(cnts)
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        if len(approx)==3:
            text="triangle"
        elif len(approx)==4:
            text="quadrilateral"
        elif len(approx)==5:
            text="pentagon"
        else:
            text="circle"
        cv2.drawContours(image1, [c], -1, (0, 255, 0), 2)
        cv2.putText(image1, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imwrite(name+'.jpg', image1)
    cv2.imshow("image",image)
    cv2.imshow(name+ " Coloured Objects",image1)
    input()
win_col(np.array([179,255,255]),np.array([170,0,0]),"Red")
win_col(np.array([86,255,255]),np.array([76,0,0]),"Green")
win_col(np.array([31,255,255]),np.array([23,60,0]),"Yellow")
win_col(np.array([179,255,255]),np.array([170,0,0]),"Blue")
win_col(np.array([15,255,255]),np.array([10,96,0]),"Orange")
