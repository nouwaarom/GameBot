import cv2
import numpy as np

from boardRecognizer import BoardRecognizer
from pieceRecognizer import PieceRecognizer


class Recognizer:
    def __init__(self, boardsize):
        self.boardsize = boardsize

        self.mask = dict()
        self.config = dict()

        self.windowFrame = 'frame'
        self.windowBoard = 'board'

        self.boardRecognizer = BoardRecognizer()
        self.pieceRecognizer = PieceRecognizer(self.boardsize)

    def initcapture(self, n):
        cap = cv2.VideoCapture(n)

        # This settings are to always set webcam resolution to maximum
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

        print "Using Camera{}".format(n)
        print "Frame Size: ", cap.get(3), "x", cap.get(4)

        self.cap = cap
        return cap.isOpened()

    def initdisplay(self):
        cv2.namedWindow(self.windowFrame, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.windowBoard, cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback(self.windowFrame, self.setmasktoposition)

    def setmasktoposition(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            mask = self.config["mask"]

            # Convert RGB value to HSV
            pixel = np.array(self.frame[y][x], ndmin=3)
            hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)
            hsv = hsv[0][0]

            mask['H'] = hsv[0]
            mask['S'] = hsv[1]
            mask['V'] = hsv[2]

            self.config["mask"] = mask
            self.boardRecognizer.setmask(mask)

    def endcapture(self):
        self.cap.release()

    def enddisplay(self):
        cv2.destroyWindow(self.windowFrame)
        cv2.destroyWindow(self.windowMask)

    def showdisplay(self):
        cv2.imshow(self.windowFrame, self.frame)
        cv2.imshow(self.windowBoard, self.board)
        cv2.waitKey(20)

    def setconfig(self, config):
        self.config = config
        self.boardRecognizer.setmask(config['mask'])

    def getconfig(self):
        return self.config

    def getframe(self):
        _,frame = self.cap.read()
        return frame

    def getboardstate(self, frame):
        self.frame = frame

        boardfound, self.board = self.boardRecognizer.processframe(frame)
        if boardfound:
            pieces = self.pieceRecognizer.findpiecesonboard(self.board)
            return pieces
