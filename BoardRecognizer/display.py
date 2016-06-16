import cv2

class Display:
    def __init__(self):
        self.windowFrame = 'frame'
        self.windowBoard = 'board'

    def initdisplay(self):
        cv2.namedWindow(self.windowFrame, cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow(self.windowBoard, cv2.WINDOW_AUTOSIZE)

    def enddisplay(self):
        cv2.destroyWindow(self.windowFrame)
        cv2.destroyWindow(self.windowBoard)

    def showframe(self, frame):
        cv2.imshow(self.windowFrame, frame)

    def showboard(self, board):
        cv2.imshow(self.windowBoard, board)