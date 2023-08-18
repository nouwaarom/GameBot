import cv2
import numpy as np

from board import Board

class BoardDisplayService:
    blue = (255 ,80 ,80)
    white = (255,255,255)

    def __init__(self, boardsize):
        # Create new window for the board
        cv2.namedWindow('boardClass', cv2.WINDOW_AUTOSIZE)

        self.boardsize = boardsize

        self.frame = np.zeros((50*boardsize, 50*boardsize, 3), np.uint8)

        for i in range(self.boardsize):
            for j in range(self.boardsize):
                cv2.rectangle(self.frame, (i*50,j*50),((i+1)*50-1,(j+1)*50-1), self.white, 1)

    def showBoard(self, board):
        # Copy the board
        board = board.getBoardRepresentation()

        for j in range(self.boardsize):
            for i in range(self.boardsize):
                if ((i+j) % 2 == 0):
                    if board:
                        char = board.pop()

                        cv2.putText(self.frame, str(len(board)), (50*i+15, 50*j+35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, self.white, 1)

                        if (char == 'b'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, self.blue, 2)

                        elif (char == 'w'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, self.white, 2)

                        elif (char == 'B'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, self.blue, 5)

                        elif (char == 'W'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, self.white, 5)

                        else:
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (0,0,0), 5)

        cv2.imshow('boardClass', self.frame)
        cv2.waitKey(20)

