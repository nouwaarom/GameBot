import numpy as np
import cv2


class PieceRecognizer:

    def __init__(self, boardsize):
        print "Initializing piece recognizer"
        self.boardsize = boardsize

    def getrow(self, position):
        return 2*(position % (self.boardsize/2)) + self.getcol(position) % 2

    def getcol(self, position):
        return position / (self.boardsize/2)

    def findpiecesonboard(self, board):
        # Split the board into pieces
        board_representation = []
        mean_black = 0
        mean = [[0 for _ in range(self.boardsize)] for _ in range(self.boardsize)]

        for i in range(self.boardsize):
            row = board[(i*50):((i+1)*50)]
            for j in range(self.boardsize):
                tile = row[0:50, (j*50):((j+1)*50)]
                mean[i][j] = cv2.mean(tile)

                if ((i+j) % 2) == 1:
                    mean_black += mean[i][j][0]

        mean_black /= (4 * 8)

        # Determine the type of pieces
        for i in range(32):
            x = self.getcol(i)
            y = self.getrow(i)

            if mean[x][y][0] < mean_black - 50:
                board_representation.append('b')
            elif mean[x][y][0] > mean_black + 50:
                board_representation.append('w')
            else:
                board_representation.append(' ')

        cv2.imshow('board', board)

        return ''.join(board_representation)
