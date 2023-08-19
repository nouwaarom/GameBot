from .movemessage_pb2 import Move
from .move_helper import helperCreateMove

class Board:

    def __init__(self, boardsize):
        self.boardsize = boardsize

    def setStartBoard(self):
        self.board = ["x"] * 50
        for i in range(2 * self.boardsize):
            self.board[i] = 'w'
            self.board[i+3*self.boardsize] = 'b'

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

        self.board[newPiece.location] = newPiece.type.decode()

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
