import numpy as np
import cv2

from pieceRecognizer import PieceRecognizer

class BoardRecognizer:

    def __init__(self, n):
        print "Initializing board recognizer"

        self.initCapture(n)

        self.piecerecognizer = PieceRecognizer()

    def initCapture(self, n):
        #initialize cap
        cap = cv2.VideoCapture(n)

        cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

        print "Using Camera{}".format(n)
        print "Frame Size: ", cap.get(3), "x", cap.get(4)

        self.cap = cap

        return cap.isOpened()

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

        #If the board is found we can try and recognize the pieces
        if len(points) == 4:
            gray = frame[:,:,2]

            points1 = np.float32(points)
            points2 = np.float32([[0,0],[400,0],[0,400],[400,400]])
            M = cv2.getPerspectiveTransform(points1,points2)
            board = cv2.warpPerspective(gray, M, (400,400))

            pieces = self.piecerecognizer.findPiecesOnBoard(board)

        #display the resulting frame
        cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('frame', frame)

        #and the mask
        cv2.namedWindow('mask', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('mask', mask)

        return pieces
