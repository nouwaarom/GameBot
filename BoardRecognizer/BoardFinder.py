#!/usr/bin/env python

import sys
import numpy as np
import cv2

def intersection (L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False


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
    frame = cv2.bilateralFilter(frame, 12, 75, 75)

    #operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Section Edge Detection
    gray = cv2.Canny(gray, 50, 250, apertureSize=3, L2gradient=True)

    # Section line Detection
    lines = cv2.HoughLines(gray,1,np.pi/180, 170)

    # Section line Intersection
    for (rho1,theta1),(rho2,theta2) in zip(lines[0],lines[0,1:]):
        a1 = np.cos(theta1)
        b1 = np.sin(theta1)

        a2 = np.cos(theta2)
        b2 = np.sin(theta2)

        R = intersection((a1,b1,rho1), (a2,b2,rho2))
        if R:
            cv2.circle(frame, R, 3, (0,255,0),-1)

        #cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)

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

