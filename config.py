#!/usr/bin/env python2
import yaml
import cv2
import argparse

from ArmController.controller import Controller
from BoardRecognizer.recognizer import Recognizer
from BoardRecognizer.display import Display


# FIXME this should be a fancy config object
config = dict()

# FIXME this is very hacky
boardsize = 8


def getrow(position):
    return 2 * (position % (boardsize / 2)) + getcol(position) % 2


def getcol(position):
    return position / (boardsize / 2)


def annotateboard(board, means, pieces):
    for i in range(32):
        x = getcol(i)
        y = getrow(i)
        cv2.putText(board, str(round(means[i], 1)) + ' ' + pieces[i],
                    (y * 50 + 25, x * 50 + 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))

def configurerecognizerwithimage(boardsize, filename):
    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    display = Display()

    display.initdisplay()
    img = cv2.imread('BoardRecognizer/tests/' + filename + '.png')
    recognizer.initrefdata('BoardRecognizer/tests/' + filename + '.yml')

    pieces = recognizer.getboardstate(img)
    print ''.join(pieces)
    checkPieces = []
    for row in recognizer.refBoard:
        for tile in row:
            checkPieces.append(tile)
    for i in range(32):
        if pieces[i] == checkPieces[i]:
            checkPieces[i] = ' '

    print 'Recognized:' + ' '.join(pieces)
    print 'Reference: ' + ' '.join(checkPieces)

    while True:
        display.showframe(img)
        annotateboard(recognizer.board, recognizer.pieceRecognizer.means, pieces)
        display.showboard(recognizer.board)
        key = cv2.waitKey(0)

        if key > 0:
            break

    display.enddisplay()

def iswhite(index, boardsize):
    row = index / boardsize
    col = index % boardsize

    return row % 2 != col % 2

def getthresholdsfromimg(boardsize, filename):
    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    recognizer.initdisplay()
    img = cv2.imread('BoardRecognizer/tests/' + filename + '.png')
    recognizer.initrefdata('BoardRecognizer/tests/' + filename + '.yml')

    checkPieces = []
    for row in recognizer.refBoard:
        for tile in row:
            checkPieces.append(tile)
    _, board = recognizer.boardRecognizer.processframe(img)
    means = recognizer.pieceRecognizer.getmeansfromboard(board)
    # Browns
    means = list(
        map(lambda (_, x): x,
            filter(lambda (x, _): not iswhite(x, boardsize),
                   enumerate(means)
                   )
        )
    )

    blackthres = 0
    whitethres = 255
    minempty = 255
    maxempty = 0
    for i in range(32):
        print checkPieces[i] + ": " + str(means[i])
        piece = checkPieces[i]
        if piece == 'w':
            whitethres = means[i] if means[i] < whitethres else whitethres
        elif piece == 'b':
            blackthres = means[i] if means[i] > blackthres else blackthres
        else:
            minempty = means[i] if means[i] < minempty else minempty
            maxempty = means[i] if means[i] > maxempty else maxempty
    print 'blackThres: '+str(blackthres)
    print 'whiteThres: '+str(whitethres)
    print 'Empty: '+str(minempty)+' - '+str(maxempty)




def testrecognizer(boardsize, filename):
    print("Testing my eyesight")

    recognizer = Recognizer(boardsize)
    recognizer.setconfig(config['recognizer'])

    display = Display()

    # Load the test movie
    recognizer.initcapture('BoardRecognizer/tests/' + filename + '.avi')
    display.initdisplay()

    while True:
        frame = recognizer.getframe()
        print recognizer.getboardstate(frame)
        display.showframe(frame)


    recognizer.endcapture()
    display.enddisplay()

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
    parser.add_argument('--thresholds', help="calculate thresholds for recognition", action="store_true")
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

    elif args.thresholds:
        getthresholdsfromimg(config['boardsize'], args.file)

    # Test arm controller
    elif args.armtest:
        testcontroller(config['boardsize'])

if __name__ == "__main__":
    main()
