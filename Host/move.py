

class Move:

    def __init__(self, newPiece, removedPieces):
        self.newPiece = newPiece
        self.removedPieces = removedPieces

    def getNewPiece(self):
        return self.newPiece

    def getRemovedPieces(self):
        return self.removedPieces
