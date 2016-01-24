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
