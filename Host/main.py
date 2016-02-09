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
from outputManager       import OutputManager

AI_PLAYER = 0
USER_PLAYER = 1

def takeTurn(board, player, arbitrator, ai, user):

    if player == AI_PLAYER:
        # NOTE might want to remove this sometime
        time.sleep(random.randint(1, 3))
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

    return

def main():
    # Argument parsing is actually quite usefull
    parser = argparse.ArgumentParser()
    parser.add_argument("--boardtest", help="run board recognizer only", action="store_true")
    parser.add_argument("--startrecognizer", help="run board recognizer only", action="store_true")
    parser.add_argument("--startai", help="run board recognizer only", action="store_true")
    parser.add_argument("--withvoice", help="enable voice config.output", action="store_true")

    args = parser.parse_args()

    config.output = OutputManager(args.withvoice)

    # Setup bus
    bus = BusConnector(5555, 5556)

    bus.startBus()

    # Start publisher and subscriber
    bus.startPublisher()
    bus.startSubscriber()

    if args.boardtest:
        config.output.say("Testing my eyesight")

        recognizer = RecognizerConnector(bus)

        if args.startrecognizer:
            recognizer.startBoardRecognizer()
        else:
            print recognizer.getCommand()
            raw_input()

        board = recognizer.getBoardState()

        print board

        bus.endBus()

        print "Terminating"

        return

    config.output.say("Welcome, I am Hansel, I am the host for this game")

    #config.output.say "Do you want to start? (yes/no) "
    #userStarts = sys.stdin.readline()
    userStarts = raw_input("Do you want to start?\n")

    if (userStarts == 'yes'):
        player = USER_PLAYER
    elif (userStarts == 'no'):
        player = AI_PLAYER
    else:
        config.output.say("Sorry, I dont understand you")
        return -1;

    config.output.say("Starting Board Recognizer ...")
    # TODO start recognition program
    # TODO check if pieces are on the right tiles and move them if neccessary

    config.output.say("Starting Arm Controller ...")
    # TODO start arm control program

    config.output.say("Setting up board ..")
    #Setup board
    board = Board()
    board.setStartBoard()
    board.showBoard()

    arbitrator = Arbitrator()

    config.output.say("Starting AI ...")
    aiConnect = AIConnector(board, player, args.startai, bus)

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
