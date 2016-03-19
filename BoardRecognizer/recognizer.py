import cv2

from boardRecognizer import BoardRecognizer


class Recognizer:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.mask = dict()
        self.config = dict()

    def initboardrecognizer(self, capture):
        self.recognizer = BoardRecognizer(capture, self.boardsize)

    def runtest(self):
        self.recognizer.initdisplay()

        self.recognizer.setmask(self.config['mask'])
        self.recognizer.inittrackbar()

        while True:
            print self.recognizer.getboardstate()

            if cv2.waitKey(10) == ord('q'):
                break

        self.recognizer.endcapture()
        self.recognizer.enddisplay()

    def getboardstate(self):
        try:
            board = self.recognizer.getboardstate()
            return board
        except Exception as e:
            print "An error occurred while getting board state"
            print e

    def setconfig(self, config):
        self.config = config

    def getconfig(self):
        return self.config
