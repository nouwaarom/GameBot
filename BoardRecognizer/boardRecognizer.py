#!/usr/bin/env python

import numpy as np
import cv2

class BoardRecognizer:

    def __init__(self, n):
        print "Initializing board recognizer"

        self.initCapture(n)

    def findPiecesOnBoard(self, image, points):

        points1 = np.float32(points)
        points2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

        M = cv2.getPerspectiveTransform(points1,points2)

        board = cv2.warpPerspective(image, M, (400,400))

        #board = cv2.adaptiveThreshold(board, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #board = cv2.Canny(board, 90, 270)

        # Split the board into pieces
        for i in range(8):
            row = board[(i*50):((i+1)*50)]

            for j in range(8):
                tile = row[0:50,(j*50):((j+1)*50)]

                mean = cv2.mean(tile)
                if mean[0] < 100:
                    print "Black piece on: {},{}".format(chr(i+ord('a')),j+1)
                    #cv2.putText(frame,'Black',(i[0],i[1]), font, 2, (0,0, 0),2)
                #else:
                #    print "White piece on: {},{}".format(chr(i+ord('a')),j)
                    #cv2.putText(frame,'White',(i[0],i[1]), font, 2, (0,0, 0),2)


        cv2.namedWindow('board', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('board', board)

    def initCapture(self, n):
        #initialize cap
        cap = cv2.VideoCapture(n)

        cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

        print "Using Camera{}".format(n)
        print "Frame Size: ", cap.get(3), "x", cap.get(4)

        self.cap = cap

    def endProgram(self):
        #when everyting is done release the frame
        self.cap.release()
        cv2.destroyAllWindows()


    def getBoardState(self):
        pieces = "!"

        cap = self.cap

        #capture frame by frame
        _, frame = cap.read()

        # Smoothing
        frame = cv2.bilateralFilter(frame, 12, 50, 50)

        # Color space conversions
        hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Color filtering
        # 50 50 50
        lower_green = np.array([30, 30, 20])
        upper_green = np.array([85, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        #copy the mask because findContours destroys the image
        thresh = mask.copy()
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #Board vertexes
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
            gray = frame[:,:,2]
            pieces = findPiecesOnBoard(gray, points)

        #display the resulting frame
        cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('frame', frame)

        #and the mask
        cv2.namedWindow('mask', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('mask', mask)

        return pieces
