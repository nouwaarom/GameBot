from .arbitrator          import Arbitrator
from .boardDisplayService import BoardDisplayService

import sys

class Game:
    def __init__(self, board, boardDisplayService, arbitrator):
        self.board               = board
        self.boardDisplayService = boardDisplayService
        self.arbitrator          = arbitrator

    # Starts the game
    def playGame(self, whitePlayer, blackPlayer):
        isWhiteTurn = True

        self.boardDisplayService.showBoard(self.board)

        while (True):
            if isWhiteTurn:
                print("White's turn")
                self.takeTurn(whitePlayer, blackPlayer)
                isWhiteTurn = False
            else:
                print("Blacks turn")
                self.takeTurn(blackPlayer, whitePlayer)
                isWhiteTurn = True

            self.boardDisplayService.showBoard(self.board)

    def takeTurn(self, activePlayer, passivePlayer):
        move = activePlayer.getMove(self.board)

        # TODO, take into account that the active player can only move their pieces
        if self.arbitrator.isMoveLegal(self.board, move):
            self.board.doMove(move)

            passivePlayer.setMove(move)

            if self.arbitrator.didWin(self.board, activePlayer):
                print("Someone won the game")
                sys.exit()
        else:
            # TODO, notify player.
            print("Illegal move")
            return False

        return True
