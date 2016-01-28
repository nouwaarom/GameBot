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

    oldRow = oldLocation // 5
    oldCol = 2*(oldLocation % 5) + (oldRow % 2)

    newRow = newLocation // 5
    newCol = 2*(newLocation % 5) + (newRow % 2)

    row = newRow
    col = newCol

    for i in range(0, abs(oldRow-newRow)):
        removedPiece = move.removedpieces.add()

        row += (oldRow-newRow)//abs(oldRow-newRow)
        col += (oldCol-newCol)//abs(oldCol-newCol)

        location = (5*row)+(col//2)
        removedPiece.location = location
        removedPiece.type     = board.getPiece(location)

        print "Removed: %d" % location

    return move
