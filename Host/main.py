#!/usr/bin/env python

import cv2
import sys
import time
import random
import argparse

import config

from board               import Board
from arbitrator          import Arbitrator
from aiConnector         import AIConnector
from userConnector       import UserConnector

from busConnector        import BusConnector

from recognizerConnector import RecognizerConnector
from controllerConnector import ControllerConnector
from outputManager       import OutputManager

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
                config.output.say("The AI won the game")
            else:
                config.output.say("The User won the game")
            sys.exit()
    else:
        config.output.say("Illegal move")

        # Let the user try again
        if player == AI_PLAYER:
           return takeTurn(board, player, arbitrator, ai, user)

    return

def playGame(bus, startai, boardsize):
    config.output.say("Welcome, I am Hansel, I am the host for this game")

    userStarts = raw_input("Do you want to start?\n")

    if (userStarts == 'yes'):
        player = USER_PLAYER
    elif (userStarts == 'no'):
        player = AI_PLAYER
    else:
        config.output.say("Sorry, I dont understand you")
        return

    config.output.say("Starting Board Recognizer ...")
    # TODO start recognition program
    # TODO check if pieces are on the right tiles and move them if neccessary

    config.output.say("Starting Arm Controller ...")
    # TODO start arm control program

    board = Board(boardsize)
    board.setStartBoard()
    board.showBoard()

    arbitrator = Arbitrator()

    config.output.say("Starting AI ...")
    aiConnect = AIConnector(board, player, bus)

    if startai:
        aiConnect.startAI()
    else:
        print aiConnect.getCommand()
        raw_input()

    userConnect = UserConnector(player)

    try:
        # Start the game
        while (True):
            takeTurn(board, player, arbitrator, aiConnect, userConnect)
            board.showBoard()

            if player == USER_PLAYER:
                player = AI_PLAYER
            else:
                player = USER_PLAYER

            c = chr(cv2.waitKey(10) & 255)
            if 'q' == c:
                break
    except Exception as e:
        print "An error occured while playing game"
        print e

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

    parser.add_argument("--withvoice", help="enable voice config.output", action="store_true")

    parser.add_argument("--boardsize", help="set the board size", type=int)

    args = parser.parse_args()

    if not args.boardsize:
        args.boardsize = 10

    return args

def main():
    args = getArgs()

    config.output = OutputManager(args.withvoice)

    bus = startBus()

    try:
        playGame(bus, args.startai, args.boardsize)
    except Exception as e:
        print "An Error occured: %s" % e

    bus.endBus()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
