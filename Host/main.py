#!/usr/bin/env python

import cv2
import random

from board       import Board
from move        import Move
from arbitrator  import Arbitrator
from aiConnector import AIConnector

AI_PLAYER = 0
USER_PLAYER = 1

def getUserMove(board):
    print "You need to make a move"

    potentialMoves = board.getMoves(['w'])

    if len(potentialMoves) > 0:
        return random.choice(potentialMoves)
    else:
        print "User couldnt come up with a move"

def setUserMove(board, move):
    print "They AI made a move"

def takeTurn(board, player, arbitrator, ai):

    if player == AI_PLAYER:
        move = ai.getMove()
        if arbitrator.isMoveLegal(board, move):
            board.doMove(move)
            setUserMove(board, move)
            if arbitrator.didWin(board, player):
                print "The AI won the game"
        else:
            print "The AI did an illegal move"

    else:
        move = getUserMove(board)
        if arbitrator.isMoveLegal(board, move):
            board.doMove(move)
            ai.setMove(move)
            if arbitrator.didWin(board, player):
                print "The user won the game"
        else:
            print "You did an illegal move"


def main():
    print "Welcome, I am Hansel, I am the host for this game"

    #print "Do you want to start? (yes/no) "
    #userStarts = sys.stdin.readline()
    userStarts = raw_input("Do you want to start?\n")

    if (userStarts == 'yes'):
        player = USER_PLAYER
    elif (userStarts == 'no'):
        player = AI_PLAYER
    else:
        print "Sorry, I dont understand you"
        return -1;

    print "Starting Board Recognizer ..."
    # TODO start recognition program
    # TODO check if pieces are on the right tiles and move them if neccessary

    print "Starting Arm Controller ..."
    # TODO start arm control program

    print "Setting up board .."
    #Setup board
    board = Board()
    board.setStartBoard()

    arbitrator = Arbitrator()

    print "Starting AI ..."
    aiConnect = AIConnector(board, player)

    # Start the game
    while(True):
        takeTurn(board, player, arbitrator, aiConnect)

        if player == USER_PLAYER:
            player = AI_PLAYER
        else:
            player = USER_PLAYER

        board.showBoard()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
