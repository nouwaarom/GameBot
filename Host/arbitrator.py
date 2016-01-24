from move  import Move
from board import Board

class Arbitrator:

    def __init__(self):
        print "Arbitrator Initializing"

    def isMoveLegal(self, board, move):
        newPiece = move.newpiece
        removedPieces = move.removedpieces

        if board.getPiece(newPiece.location) != 'x':
            return False

        for removedPiece in removedPieces:

            if board.getPiece(removedPiece.location) != removedPiece.type:
                return False

        return True


    def didWin(self, board, player):
        #user
        if player:
            enemyPieces = ['w', 'W']
        #ai
        else:
            enemyPieces = ['b', 'B']

        boardList = board.getBoardRepresentation()
        for enemyPiece in enemyPieces:
            if boardList.count(enemyPiece) != 0:
                return False

        return True

