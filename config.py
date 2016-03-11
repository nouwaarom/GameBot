#!/usr/bin/env python
import yaml
import argparse

from Bus.busConnector import BusConnector
from Bus.bus          import Bus

from ArmController.controller   import Controller
from BoardRecognizer.recognizer import Recognizer

def testRecognizer(bus, boardsize):
    print("Testing my eyesight")

    recognizer = Recognizer(boardsize)

    board = recognizer.getBoardState()

    print board
    print "Terminating"

    return

def testController(bus, boardsize):
    print("Testing my arm")

    controller = Controller()
    controller.doMove("dummy")

    print "Terminating"
    return

def getArgs():
    # Argument parsing is actually quite usefull
    parser = argparse.ArgumentParser(description="Gamebot configuring program")
    parser.add_argument("--boardtest", help="run board recognizer only", action="store_true")
    parser.add_argument("--armtest", help="run arm controller only", action="store_true")

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

    bus = Bus()
    bus.startBus()

    # Start publisher and subscriber
    busCon = BusConnector(5555, 5556)

    # Test board recognizer program
    if args.boardtest:
        testRecognizer(busCon, args.boardsize)

    # Test arm controller
    elif args.armtest:
        testController(busCon, args.boardsize)

    bus.endBus()

if __name__ == "__main__":
    main()
