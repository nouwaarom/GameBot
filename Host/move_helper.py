from __future__ import division
from .movemessage_pb2 import Move
from .player import PLAYER_BLACK, PLAYER_WHITE

def helperCreateMove(newPiece, removedPieces):
    move = Move()
    move.newpiece.location = newPiece[0]
    move.newpiece.type     = newPiece[1].encode()

    for removedPiece in removedPieces:
        removedpiece  = move.removedpieces.add()
        removedpiece.location = removedPiece[0]
        removedpiece.type     = removedPiece[1].encode()

    return move

def helperCreateMoveFromLocations(newLocation, oldLocation, board):
    move = Move()
    move.newpiece.location = newLocation
    move.newpiece.type     = board.getPiece(oldLocation).encode()

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
        removedPiece.type     = board.getPiece(location).encode()

        print("Removed: %d" % location)

    return move

def helperGetOldPiece(newPiece, removedPieces):
    for removedPiece in removedPieces:
        if helperGetOwnerOfPiece(removedPiece) == helperGetOwnerOfPiece(newPiece):
            return removedPiece
    print("Could not find old piece, this move smells...", newPiece, removedPieces)

def helperGetOwnerOfPiece(piece):
    piece_type = piece.type.decode();
    if piece_type == 'w' or piece_type == 'W':
        return PLAYER_WHITE
    if piece_type == 'b' or piece_type == 'B':
        return PLAYER_BLACK
    raise Exception("No player known for piece: {}".format(piece.type))

def helperGetRowColumn(location):
    row = location // 5
    col = 2*(location % 5) + (row % 2)
    return (row, col)
