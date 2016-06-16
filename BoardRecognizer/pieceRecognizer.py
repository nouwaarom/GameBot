import numpy as np
import decimal
import cv2

from filter import Filter

class PieceRecognizer:

    def __init__(self, boardsize):
        print "Initializing piece recognizer"
        self.boardsize = boardsize
        self.board_representation = []
        self.means = []
        self.board = None

    def getmeansfromboard(self, board):
        # Split the board into pieces
        mean = [[0 for _ in range(self.boardsize)] for _ in range(self.boardsize)]
        #mean = [[0] * self.boardsize] * self.boardsize

        print mean

        means = []
        for i in range(self.boardsize):
            row = board[(i*50):((i+1)*50)]
            for j in range(self.boardsize):
                tile = row[0:50, (j*50):((j+1)*50)]
                means.append(cv2.mean(tile)[0])
        # flatmean = []
        # for i in range(32):
        #     x = self.getcol(i)
        #     y = self.getrow(i)

        #    flatmean.append(mean[x][y])


        filter = Filter(self.boardsize)
        filter.apply(means)
        return means

    def isWhite(self, index):
        row = index / self.boardsize
        col = index % self.boardsize

        return row % 2 != col % 2

    def findpiecesonboard(self, board):
        mean = self.getmeansfromboard(board)
        # Browns
        mean = list(
            map(lambda (_, x): x,
                filter(lambda (x, _): not self.isWhite(x),
                    enumerate(mean)
                )
            )
        )

        self.board = cv2.cvtColor(board, cv2.COLOR_GRAY2RGB)

        # Determine the type of pieces
        for i in range(32):

            if mean[i] < 80:
                identifier = 'b'
            elif mean[i] > 140:
                identifier = 'w'
            else:
                identifier = 'x'

            self.board_representation.append(identifier)

        self.means = mean

        return True
