#!/usr/bin/env python

import cv2
import sys
import time
import random
import argparse

from game                import Game
from board               import Board
from arbitrator          import Arbitrator
from aiConnector         import AIConnector
from userConnector       import UserConnector

from boardDisplayService import BoardDisplayService

from busConnector        import BusConnector

from recognizerConnector import RecognizerConnector
from controllerConnector import ControllerConnector

def playGame(bus, startai, boardsize):
    print("Welcome, I am Hansel, I am the host for this game")

    userStarts = raw_input("Do you want to start?\n")

    if (userStarts == 'yes'):
        userStarts = 1
    elif (userStarts == 'no'):
        userStarts = 0
    else:
        print("Sorry, I dont understand you")
        return

    print("Starting Board Recognizer ...")
    # TODO start recognition program
    # TODO check if pieces are on the right tiles and move them if neccessary

    print("Starting Arm Controller ...")
    # TODO start arm control program

    board = Board(boardsize)
    board.setStartBoard()
    boardDisplayService = BoardDisplayService(boardsize)

    arbitrator = Arbitrator()

    print("Starting AI ...")
    aiConnect = AIConnector(board, userStarts, bus)

    if startai:
        aiConnect.startAI()
    else:
        print aiConnect.getCommand()
        raw_input()

    userConnect = UserConnector(userStarts)

    game = Game(board, boardDisplayService, arbitrator)

    if userStarts:
        game.playGame(userConnect, aiConnect)
    else:
        game.playGame(aiConnect, userConnect)

    if startai:
        aiConnect.terminateAI()

    return

def startBus():
    bus = BusConnector(5555, 5556)
    bus.startBus()

    # Start publisher and subscriber
    bus.startPublisher()
    bus.startSubscriber()

    return bus

def getArgs():
    # Argument parsing is actually quite usefull
    parser = argparse.ArgumentParser()

    parser.add_argument("--startrecognizer", help="start recognizer program", action="store_true")
    parser.add_argument("--startcontroller", help="start controller program", action="store_true")
    parser.add_argument("--startai", help="run board recognizer only", action="store_true")

    #parser.add_argument("--withvoice", help="enable voice config.output", action="store_true")

    parser.add_argument("--boardsize", help="set the board size", type=int)

    args = parser.parse_args()

    if not args.boardsize:
        args.boardsize = 10

    return args

def main():
    args = getArgs()

    bus = startBus()

    #try:
    playGame(bus, args.startai, args.boardsize)
    #except Exception as e:
    #    print "An Error occured: %s" % e

    bus.endBus()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
