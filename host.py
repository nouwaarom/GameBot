#!/usr/bin/env python3

import cv2
import sys
import time
import random
import argparse

from Host.host.game                import Game
from Host.host.board               import Board
from Host.host.boardDisplayService import BoardDisplayService
from Host.host.arbitrator          import Arbitrator
from Host.host.userConnector       import UserConnector
from Host.host.aiConnector         import AIConnector

from Bus.busConnector import BusConnector
from Bus.bus          import Bus

def playGame(bus, startai, boardsize):
    print("Welcome, I am Hansel, I am the host for this game")

    userStarts = input("Do you want to start?\n")

    if (userStarts == 'yes'):
        userStarts = 1
    elif (userStarts == 'no'):
        userStarts = 0
    else:
        print("Sorry, I dont understand you")
        return

    print("Starting Board Recognizer ...")
    # TODO start recognition program
    # TODO check if pieces are on the right tiles and move them if necessary

    print("Starting Arm Controller ...")
    # TODO start arm control program

    board = Board(boardsize)
    board.setStartBoard()
    boardDisplayService = BoardDisplayService(boardsize)

    arbitrator = Arbitrator()

    print("Starting communication to AI ...")
    aiConnect = AIConnector(board, userStarts, bus)

    if startai:
        aiConnect.startAI()
    else:
        print("To start the AI, execute: {}".format(aiConnect.getCommand()))
        input()

    userConnect = UserConnector(userStarts)

    game = Game(board, boardDisplayService, arbitrator)

    try:
        if userStarts:
            game.playGame(userConnect, aiConnect)
        else:
            game.playGame(aiConnect, userConnect)
    finally:
        if startai:
            aiConnect.terminateAI()

    return

# Argument parsing is actually quite usefull
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--startai",         help="Start the AI", action="store_true")
    parser.add_argument("--boardsize",       help="set the board size", type=int)
    args = parser.parse_args()

    if not args.boardsize:
        args.boardsize = 10

    return args

def main():
    args = getArgs()

    bus = Bus()
    bus.startBus()

    busCon = BusConnector(5555, 5556)

    try:
        playGame(busCon, args.startai, args.boardsize)
    except (KeyboardInterrupt, SystemExit):
        print("Exiting application")
    finally:
        bus.endBus()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
