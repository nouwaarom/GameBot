from __future__ import division
from movemessage_pb2 import Move

def helperCreateMove(newPiece, removedPieces):
    move = Move()
    move.newpiece.location = newPiece[0]
    move.newpiece.type     = newPiece[1]

    for removedPiece in removedPieces:
        removedpiece  = move.removedpieces.add()
        removedpiece.location = removedPiece[0]
        removedpiece.type     = removedPiece[1]

    return move

def helperCreateMoveFromLocations(newLocation, oldLocation, board):
    move = Move()
    move.newpiece.location = newLocation
    move.newpiece.type     = board.getPiece(oldLocation)

    (oldRow, oldCol) = helperGetRowColumn(oldLocation)
    (newRow, newCol) = helperGetRowColumn(newLocation)

    (row, col) = (newRow, newCol)

    for i in range(0, abs(oldRow-newRow)):
        removedPiece = move.removedpieces.add()

        if oldRow != newRow:
            row += (oldRow-newRow)//abs(oldRow-newRow)
        if oldCol != newCol:
            col += (oldCol-newCol)//abs(oldCol-newCol)

        location = (5*row)+(col//2)
        removedPiece.location = location
        removedPiece.type     = board.getPiece(location)

        print "Removed: %d" % location

    return move

def helperGetOldPiece(newPiece, removedPieces):
    for removedPiece in removedPieces:
        if removedPiece.type == newPiece.type:
            return removedPiece
    print "Could not find old piece, this move smells..."

def helperGetRowColumn(location):
    row = location // 5
    col = 2*(location % 5) + (row % 2)
    return (row, col)
