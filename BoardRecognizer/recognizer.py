import cv2
import numpy as np
import yaml

from boardRecognizer import BoardRecognizer
from pieceRecognizer import PieceRecognizer


class Recognizer:
    def __init__(self, boardsize):
        self.boardsize = boardsize

        self.mask = dict()
        self.config = dict()

        self.boardRecognizer = BoardRecognizer()
        self.pieceRecognizer = PieceRecognizer(self.boardsize)

    def initcapture(self, n):
        cap = cv2.VideoCapture(n)

        # This settings are to always set webcam resolution to maximum
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 2000)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 2000)

        print "Capturing from: {}".format(n)
        print "Frame Size: ", cap.get(3), "x", cap.get(4)

        self.cap = cap
        return cap.isOpened()

    def initrefdata(self, path):
        file = open(path, 'r')
        refdata = yaml.load(file.read())
        self.refBoard = refdata['board']
        print "Ref data:"
        print refdata

    def endcapture(self):
        self.cap.release()

    def setconfig(self, config):
        self.config = config
        self.boardRecognizer.setmask(config['mask'])

    def getconfig(self):
        return self.config

    def getframe(self):
        _, frame = self.cap.read()
        return frame

    def getboardstate(self, frame):
        self.frame = frame

        boardfound, self.board = self.boardRecognizer.processframe(frame)
        if boardfound:
            self.pieceRecognizer.findpiecesonboard(self.board)
            return self.pieceRecognizer.board_representation
