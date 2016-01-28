import random

from board       import Board
from move_helper import helperCreateMoveFromLocations

class UserConnector:

    def __init__(self, userStarts):
        if userStarts:
            self.userPieces = ['w', 'W']
            self.opponentPieces = ['b', 'B']
        else:
            self.userPieces = ['b', 'B']
            self.opponentPieces = ['w', 'W']

    def getMove(self, board):
        print "You need to make a move"

        oldLocation = int(raw_input("Old location: "))
        newLocation = int(raw_input("New location: "))

        return helperCreateMoveFromLocations(newLocation, oldLocation, board)

    def setMove(self, move):
        return
