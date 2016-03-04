#!/usr/bin/env python
import yaml
import argparse

from busConnector        import BusConnector

from recognizerConnector import RecognizerConnector
from controllerConnector import ControllerConnector

def testRecognizer(bus, startrecognizer, boardsize):
    print("Testing my eyesight")

    recognizer = RecognizerConnector(bus, boardsize)

    if startrecognizer:
        recognizer.startBoardRecognizer()
    else:
        print recognizer.getCommand()
        raw_input()

    board = recognizer.getBoardState()

    print board
    print "Terminating"

    return

def testController(bus, startcontroller, boardsize):
    print("Testing my arm")

    controller = ControllerConnector(bus, boardsize)

    if startcontroller:
        controller.startArmController()
    else:
        print controller.getCommand()
        raw_input()

    board = "wwwwwxxxxbbbbb"

    controller.setBoardState(board)

    print "Terminating"
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
    parser = argparse.ArgumentParser(description="Gamebot configuring program")
    parser.add_argument("--boardtest", help="run board recognizer only", action="store_true")
    parser.add_argument("--armtest", help="run arm controller only", action="store_true")

    parser.add_argument("--startrecognizer", help="start recognizer program", action="store_true")
    parser.add_argument("--startcontroller", help="start controller program", action="store_true")

    parser.add_argument("--boardsize", help="set the board size", type=int)

    args = parser.parse_args()

    if not args.boardsize:
        args.boardsize = 10

    if (not args.boardtest) and (not args.armtest):
        parser.print_help()
        return

    return args

def main():
    print("This program configures the gamebot setup")

    args = getArgs()

    if not args:
        return

    bus = startBus()

    # Test board recognizer program
    if args.boardtest:
        testRecognizer(bus, args.startrecognizer, args.boardsize)

    # Test arm controller
    elif args.armtest:
        testController(bus, args.startcontroller, args.boardsize)

    bus.endBus()

# TODO remove evil else (output is outputmanager object, see main.py)
if __name__ == "__main__":
    main()
