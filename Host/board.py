import cv2
import numpy as np

from movemessage_pb2 import Move
from move_helper import helperCreateMove

class Board:

    def __init__(self, boardsize):
        # Create new window for the board
        cv2.startWindowThread()
        cv2.namedWindow('boardClass', cv2.WINDOW_AUTOSIZE)

        self.boardsize = boardsize
        self.frame = np.zeros((50*boardsize, 50*boardsize, 3), np.uint8)

        for i in range(self.boardsize):
            for j in range(self.boardsize):
                cv2.rectangle(self.frame, (i*50,j*50),((i+1)*50-1,(j+1)*50-1), (255,255,255), 1)

    def setStartBoard(self):
        self.board = ["x"] * 50
        for i in range(2 * self.boardsize):
            self.board[i] = 'w'
            self.board[i+3*self.boardsize] = 'b'

    def showBoard(self):
        # Copy the board
        board = list(self.board)

        for j in range(self.boardsize):
            for i in range(self.boardsize):
                if ((i+j) % 2 == 0):
                    if board:
                        char = board.pop()

                        cv2.putText(self.frame, str(len(board)), (50*i+15, 50*j+35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

                        if (char == 'b'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (255,0,0), 2)

                        elif (char == 'w'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (255,255,255), 2)

                        elif (char == 'B'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (255,0,0), 5)

                        elif (char == 'W'):
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (255,255,255), 5)

                        else:
                            cv2.circle(self.frame, (50*i+25, 50*j+25), 20, (0,0,0), 5)

        cv2.imshow('boardClass', self.frame)


    def saveBoard(self, name):
        print "Saving board to file"

    def loadBoard(self, name):
        print "Loading board from file"

    def getPiece(self, location):
        return self.board[location]

    def getSize(self):
        return self.boardsize;

    #return a copy of the board representation
    def getBoardRepresentation(self):
        return list(self.board)

    def doMove(self, move):
        newPiece = move.newpiece
        removedPieces = move.removedpieces

        self.board[newPiece.location] = newPiece.type

        for removedPiece in removedPieces:
            self.board[removedPiece.location] = 'x'

    def getMoves(self, colors):
        moves = []
        board = list(self.board)

        for key, tile in enumerate(board):
            if tile in colors:
                #check down
                if key > 5:
                    #check left
                    if (key % 5) != 0:
                        if board[key-6] == 'x':
                            moves.append(helperCreateMove((key-6, tile), [(key, tile)]))

                    #check right
                    if ((key+1) % 5) != 0:
                        if board[key-4] == 'x':
                            moves.append(helperCreateMove((key-4, tile), [(key, tile)]))

                #check up
                if key < 45:
                    #check left
                    if (key % 5) != 0:
                        if board[key+4] == 'x':
                            moves.append(helperCreateMove((key+4, tile), [(key, tile)]))

                    #check right
                    if ((key+1) % 5) != 0:
                        if board[key+6] == 'x':
                            moves.append(helperCreateMove((key+6, tile), [(key, tile)]))

        return moves

    def getForcedMoves(self, colors, enemy):
        moves = []
        board = self.board

        for key, tile in enumerate(self.board):
            if tile in colors:
                #check down
                if key > 10:
                    #check left
                    if ((key-1) % 5) != 0:
                        if board[key-6] in enemy:
                            if board[key-11] == 'x':
                                moves.append(helperCreateMove((key-11, tile), [(key, tile), (key-6, board[key-6])]))

                    #check right
                    if ((key+2) % 5) != 0:
                        if board[key-4] in enemy:
                            if board[key-9] == 'x':
                                moves.append(helperCreateMove((key-9, tile), [(key, tile), (key-4, board[key-4])]))

                #check up
                if key < 40:
                    #check left
                    if ((key-1) % 5) != 0:
                        if board[key+4] in enemy:
                            if board[key+9] == 'x':
                                moves.append(helperCreateMove((key+9, tile), [(key, tile), (key+4, board[key+4])]))

                    #check right
                    if ((key+2) % 5) != 0:
                        if board[key+6] in enemy:
                            if board[key+11] == 'x':
                                moves.append(helperCreateMove((key+11, tile), [(key, tile), (key+6, board[key+6])]))

        return move
