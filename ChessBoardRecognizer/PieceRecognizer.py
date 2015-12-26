#!/usr/bin/env python

import sys
import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

#initialize cap
cap = cv2.VideoCapture(1)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)

cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

print "Frame Size: ", cap.get(3), "x", cap.get(4)

while(True):
    #capture frame by frame
    _, frame = cap.read()

    #Smoothing
    frame = cv2.bilateralFilter(frame, 10, 50, 50)

    #operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mask
    mask = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Section Edge Detection
    #gray = cv2.Canny(gray, 50, 250, apertureSize=3, L2gradient=True)

    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
                                param1=50, param2=20, minRadius=0, maxRadius = 60)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            mask = np.zeros((cap.get(4), cap.get(3), 1), np.uint8)

            cv2.circle(mask,(i[0],i[1]),i[2],255,-1)

            mean = cv2.mean(gray, mask = mask)

            if mean[0] < 60:
                 cv2.putText(frame,'Black',(i[0],i[1]), font, 2, (0,0, 0),2)
            else:
                 cv2.putText(frame,'White',(i[0],i[1]), font, 2, (0,0, 0),2)

            cv2.circle(frame,(i[0],i[1]),i[2],(0,150,0),2)


    #display the resulting frame
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('frame', frame)

    cv2.namedWindow('gray', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) == ord('q'):
        break;

#when everyting is done release the frame
cap.release()
cv2.destroyAllWindows()

