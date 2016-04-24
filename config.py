#!/usr/bin/env python
import yaml
import cv2
import argparse

from ArmController.controller import Controller
from BoardRecognizer.recognizer import Recognizer


# FIXME this should be a fancy config object
config = dict()


def configurerecognizerwithimage(boardsize, filename):
    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    recognizer.initdisplay()
    img = cv2.imread('BoardRecognizer/tests/' + filename)

    print recognizer.getboardstate(img)

    while True:
        recognizer.showdisplay()
        key = cv2.waitKey(50)

        if key == ord('q'):
            break

    recognizer.enddisplay()


def testrecognizer(boardsize, filename):
    print("Testing my eyesight")

    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    # Load the test movie
    recognizer.initcapture('BoardRecognizer/tests/' + filename)
    recognizer.initdisplay()

    while True:
        frame = recognizer.getframe()
        print recognizer.getboardstate(frame)
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
    parser.add_argument("--boardconfigure", help="configure board recognizer", action="store_true")
    parser.add_argument("--boardtest", help="run board recognizer only", action="store_true")
    parser.add_argument("--armtest", help="run arm controller only", action="store_true")
    parser.add_argument("--file", help="name of test image to load")

    args = parser.parse_args()

    if not args:
        print("Nothing to configure, terminating")
        parser.print_help()
        return

    return args


def main():
    global config
    print("This program configures the gamebot setup")

    args = getargs()

    configfile = open('config.yml', 'r')
    config = yaml.load(configfile.read())

    print(config)

    # Test board recognizer program
    if args.boardtest:
        testrecognizer(config['boardsize'], args.file)

    elif args.boardconfigure:
        configurerecognizerwithimage(config['boardsize'], args.file)

    # Test arm controller
    elif args.armtest:
        testcontroller(config['boardsize'])

if __name__ == "__main__":
    main()
