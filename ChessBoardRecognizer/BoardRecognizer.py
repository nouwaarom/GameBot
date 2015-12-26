#!/usr/bin/env python

import sys
import numpy as np
import cv2

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
    frame = cv2.bilateralFilter(frame, 12, 50, 50)

    #operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Section Edge Detection
    gray = cv2.Canny(gray, 50, 250, apertureSize=3, L2gradient=True)

    # Section Line Detection
    #minLineLength = 100
    #maxLineGap = 30
    #lines = cv2.HoughLinesP(gray,1,np.pi/180,100,minLineLength,maxLineGap)
    #for x1,y1,x2,y2 in lines[0]:
    #    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    # Section Contour Detection
    # Waterfall threshold
    #ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # Adaptive threshold
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 13, 2)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Contour filter
    for i in contours:
        area = cv2.contourArea(i)
        if area > 400:

            hull = cv2.convexHull(i, returnPoints = False)
            defects = cv2.convexityDefects(i, hull)

            if defects is not None:
                goodHull = True

                for j in range(defects.shape[0]):
                    s,e,f,d = defects[j,0]

                    if d > 1000:
                        goodHull = False

                if goodHull:
                    cv2.drawContours(frame, [i], 0, (200,100,0), 2)

    # Section Corner Detection
    #corners = cv2.goodFeaturesToTrack(gray, 64 + 4, 0.01, 10)
    #corners = np.int0(corners)
    #for i in corners:
    #    x, y = i.ravel()
    #    cv2.circle(frame, (x,y), 3, 255, -1)

    #display the resulting frame
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('frame', frame)

    #and the gray
    cv2.namedWindow('gray', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) == ord('q'):
        break;

#when everyting is done release the frame
cap.release()
cv2.destroyAllWindows()
