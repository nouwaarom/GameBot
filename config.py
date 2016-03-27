#!/usr/bin/env python
import yaml
import argparse

from ArmController.controller import Controller
from BoardRecognizer.recognizer import Recognizer


# FIXME this should be a fancy config object
config = dict()


def testrecognizer(boardsize):
    print("Testing my eyesight")

    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    # Load the test movie
    recognizer.initcapture('BoardRecognizer/tests/test-1.avi')
    recognizer.initdisplay()

    while True:
        print recognizer.getboardstate()
        recognizer.showdisplay()

    recognizer.endcapture()
    recognizer.enddisplay()

    config['recognizer'] = recognizer.getconfig()


def testcontroller(boardsize):
    print("Testing my arm")
    print(boardsize)

    controller = Controller()
    controller.doMove("dummy")

    print("Terminating")


def getargs():
    # Argument parsing is actually quite useful
    parser = argparse.ArgumentParser(description="Gamebot configuring program")
    parser.add_argument("--boardtest", help="run board recognizer only", action="store_true")
    parser.add_argument("--armtest", help="run arm controller only", action="store_true")

    args = parser.parse_args()

    if (not args.boardtest) and (not args.armtest):
        parser.print_help()
        return

    return args


def main():
    global config
    print("This program configures the gamebot setup")

    args = getargs()

    if not args:
        print("Nothing to configure, terminating")
        return

    configfile = open('config.yml', 'r')
    config = yaml.load(configfile.read())

    print(config)

    # Test board recognizer program
    if args.boardtest:
        testrecognizer(config['boardsize'])

    # Test arm controller
    elif args.armtest:
        testcontroller(config['boardsize'])

if __name__ == "__main__":
    main()
