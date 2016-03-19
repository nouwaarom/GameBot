import numpy as np
import cv2

from pieceRecognizer import PieceRecognizer


class BoardRecognizer:

    def __init__(self, capture, boardsize):
        print "Initializing board recognizer"

        self.cap = cv2.VideoCapture()
        self.boardsize = boardsize
        self.windowAvailable = True
        self.piecerecognizer = PieceRecognizer()

        self.windowMask = 'mask'
        self.windowFrame = 'frame'

        # Mask for filtering the board edges
        self.mask = dict()

        self.initcapture(capture)

    def initcapture(self, n):
        # initialize cap
        cap = cv2.VideoCapture(n)

        cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

        print "Using Camera{}".format(n)
        print "Frame Size: ", cap.get(3), "x", cap.get(4)

        self.cap = cap
        return cap.isOpened()

    def initdisplay(self):
        self.windowAvailable = True
        cv2.namedWindow(self.windowFrame, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.windowMask, cv2.WINDOW_AUTOSIZE)

    def inittrackbar(self):
        cv2.createTrackbar('H', self.windowMask, 0, 255, self.ontrackbarchange)
        cv2.createTrackbar('S', self.windowMask, 0, 255, self.ontrackbarchange)
        cv2.createTrackbar('V', self.windowMask, 0, 255, self.ontrackbarchange)

        # Set the trackbar to the right starting values
        cv2.setTrackbarPos('H', self.windowMask, self.mask['H'])
        cv2.setTrackbarPos('S', self.windowMask, self.mask['S'])
        cv2.setTrackbarPos('V', self.windowMask, self.mask['V'])

    def ontrackbarchange(self, _):
        self.mask['H'] = cv2.getTrackbarPos('H', self.windowMask)
        self.mask['S'] = cv2.getTrackbarPos('S', self.windowMask)
        self.mask['v'] = cv2.getTrackbarPos('V', self.windowMask)

    def endcapture(self):
        # when everything is done release the frame
        self.cap.release()

    def enddisplay(self):
        cv2.destroyWindow(self.windowFrame)
        cv2.destroyWindow(self.windowMask)

    def getmask(self):
        return self.mask

    def setmask(self, mask):
        self.mask = mask

    def getboardstate(self):
        pieces = "!"

        cap = self.cap

        # capture frame by frame
        _, frame = cap.read()

        # Smoothing
        frame = cv2.bilateralFilter(frame, 12, 50, 50)

        # Color space conversions
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Color filtering
        # was approximately 50 50 50
        lower_green = np.array([self.mask['H'], self.mask['S'], self.mask['V']])
        upper_green = np.array([85, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        # copy the mask because findContours destroys the image
        thresh = mask.copy()
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Board vertexes
        points = []

        # Contour filter
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                m = cv2.moments(contour)
                cx = int(m['m10']/m['m00'])
                cy = int(m['m01']/m['m00'])

                points.append((cx, cy))

        # If the board is found we can try and recognize the pieces
        if len(points) == 4:
            gray = frame[:, :, 2]

            points1 = np.float32(points)
            points2 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
            m = cv2.getPerspectiveTransform(points1, points2)
            board = cv2.warpPerspective(gray, m, (400, 400))

            pieces = self.piecerecognizer.findPiecesOnBoard(board)

        # display the resulting frame
        if self.windowAvailable:
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)

        return pieces
