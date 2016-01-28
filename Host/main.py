#!/usr/bin/env python

import cv2
import random

from board         import Board
from arbitrator    import Arbitrator
from aiConnector   import AIConnector
from userConnector import UserConnector

AI_PLAYER = 0
USER_PLAYER = 1

def takeTurn(board, player, arbitrator, ai, user):

    if player == AI_PLAYER:
        move = ai.getMove()
    else:
        move = user.getMove(board)

    if arbitrator.isMoveLegal(board, move):
        board.doMove(move)

        if player == AI_PLAYER:
            user.setMove(move)
        else:
            ai.setMove(move)

        if arbitrator.didWin(board, player):
            if player == AI_PLAYER:
                print "The AI won the game"
            else:
                print "The User won the game"
    else:
        print "Illegal move"

    return

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
    board.showBoard()

    arbitrator = Arbitrator()

    print "Starting AI ..."
    aiConnect = AIConnector(board, player, True)

    userConnect = UserConnector(player)

    # Start the game
    while(True):
        takeTurn(board, player, arbitrator, aiConnect, userConnect)
        board.showBoard()

        if player == USER_PLAYER:
            player = AI_PLAYER
        else:
            player = USER_PLAYER

        c = chr(cv2.waitKey(10) & 255)
        if 'q' == c:
            break

    cv2.destroyAllWindows()
    aiConnect.terminateAI()

if __name__ == "__main__":
    main()
