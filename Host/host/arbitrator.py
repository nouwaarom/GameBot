from .movemessage_pb2  import Move
from .board import Board
from .move_helper import helperGetOldPiece, helperGetRowColumn

class Arbitrator:

    def __init__(self):
        print("Arbitrator Initializing")

    def isMoveLegal(self, board, move):
        newPiece = move.newpiece
        removedPieces = move.removedpieces

        # Check if the move is diagonal
        if len(removedPieces) < 3:
            if newPiece is None:
                return False
            newLocation = newPiece.location
            oldPiece = helperGetOldPiece(newPiece, removedPieces)
            if oldPiece is None:
                return False
            oldLocation = oldPiece.location

            try:
                (newRow, newCol) = helperGetRowColumn(newLocation)
                (oldRow, oldCol) = helperGetRowColumn(oldLocation)
            except:
                print("Malformed move!")
                return False
            if newRow == oldRow or newCol == oldCol:
                print("Not a diagonal move!")
                return False

        if board.getPiece(newPiece.location) != 'x':
            print("NewPiece location (%d) is not empty" % newPiece.location)
            return False

        for removedPiece in removedPieces:
            if board.getPiece(removedPiece.location) != removedPiece.type.decode():
                print("RemovedPiece type is not correct")
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
