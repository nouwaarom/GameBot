import cv2

from boardRecognizer import BoardRecognizer


class Recognizer:
    def __init__(self, boardsize):
        self.boardsize = boardsize
        self.mask = dict()
        self.config = dict()

        self.windowMask = 'mask'
        self.windowFrame = 'frame'
        self.windowBoard = 'board'

        self.boardRecognizer = BoardRecognizer(capture, self.boardsize)

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
        cv2.namedWindow(self.windowFrame, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.windowMask, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.windowBoard, cv2.WINDOW_AUTOSIZE)

    def inittrackbar(self):
        cv2.createTrackbar('H', self.windowMask, 0, 179, self.ontrackbarchange)
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

    def showdisplay(self):
        cv2.imshow(self.windowFrame, self.frame)
        cv2.imshow(self.windowMask,  self.mask)
        cv2.imshow(self.windowBoard, self.board)

    def getframe(self):
        _, frame = self.cap.read()
        return frame

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
            frame = self.getframe()
            self.boardRecognizer.processframe(frame)
            if self.boardRecognizer.boardfound():
                board = self.boardRecognizer.getboard()
                pieces = self.pieceRecognizer.findpiecesonboard(board)
                return pieces

        except Exception as e:
            print "An error occurred while getting board state"
            print e

    def setconfig(self, config):
        self.config = config

    def getconfig(self):
        return self.config
