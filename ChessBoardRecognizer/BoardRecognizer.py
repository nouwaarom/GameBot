#!/usr/bin/env python

from __future__ import division
import sys
import numpy as np
import cv2

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

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

def parallel (L1, L2, p1):
    A = (L1[0]+L2[0]) / 2
    B = (L1[1]+L2[1]) / 2
    C = A*p1[1] + B*p1[2]
    return A, B, C

def divideAndConquer(points):

    points1 = np.float32(points)
    points2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

    M = cv2.getPerspectiveTransform(points1,points2)

    destination = cv2.warpPerspective(frame, M, (500,500))

    # Normalized
    cv2.namedWindow('norm', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('norm', destination)

    #diagonal lines
    #cv2.line(frame, points[0], points[2], (255,0,0), 1)
    #cv2.line(frame, points[1], points[3], (255,0,0), 1)

    # Calculate the point of intersection
    #middle = intersection(line(points[0], points[2]), line(points[1], points[3]))

    #if middle is not None:
    #    cv2.circle(frame, (int(middle[0]), int(middle[1])), 5, (0,0,200), -1)

    #horizontal lines
    #cv2.line(frame, points[0], points[3], (0,0,255), 2)
    #cv2.line(frame, points[1], points[2], (0,0,255), 2)

    #vertical lines
    #cv2.line(frame, points[0], points[1], (0,0,255), 2)
    #cv2.line(frame, points[2], points[3], (0,0,255), 2)

#initialize cap
cap = cv2.VideoCapture(1)

cap.set(cv2.cv.CV_CAP_PROP_FPS, 2)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

print "Frame Size: ", cap.get(3), "x", cap.get(4)


while(True):
    #capture frame by frame
    _, frame = cap.read()

    # Smoothing
    frame = cv2.bilateralFilter(frame, 12, 50, 50)

    # Color space conversions
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color filtering
    lower_green = np.array([50, 70, 70])
    upper_green = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    #mask = cv2.dilate(mask, np.ones((5,5), np.uint8), iterations = 4)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5,5), np.uint8));

    # Section Edge Detection
    #mask = cv2.Canny(mask, 50, 250, apertureSize=3, L2gradient=True)

    # Section Line Detection
    #minLineLength = 100
    #maxLineGap = 30
    #lines = cv2.HoughLinesP(mask,1,np.pi/180,100,minLineLength,maxLineGap)
    #for x1,y1,x2,y2 in lines[0]:
    #    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)

    # Section Contour Detection
    # Waterfall threshold
    #ret, thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # Adaptive threshold
    #thresh = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 13, 2)

    thresh = mask.copy()
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    points = []

    # Contour filter
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            M = cv2.moments(contour)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            points.append((cx, cy))

    if len(points) == 4:
        divideAndConquer(points)


    # Section Corner Detection
    #corners = cv2.goodFeaturesToTrack(mask, 4, 0.05, 10)
    #corners = np.int0(corners)
    #for i in corners:
    #    x, y = i.ravel()
    #    cv2.circle(frame, (x,y), 3, 255, -1)

    #display the resulting frame
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('frame', frame)

    #and the gray
    #cv2.namedWindow('gray', cv2.WINDOW_AUTOSIZE)
    #cv2.imshow('gray', gray)

    #and hsv
    cv2.namedWindow('mask', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break;

#when everyting is done release the frame
cap.release()
cv2.destroyAllWindows()
