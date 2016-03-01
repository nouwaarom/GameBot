#!/usr/bin/env python

import os
import cv2
import argparse

from boardRecognizer import BoardRecognizer
from busConnector    import BusConnector

from boardmessage_pb2 import BoardMessage


def getArgs():
    # Argument parsing is actually quite usefull
    parser = argparse.ArgumentParser()
    parser.add_argument("--continuous", help="run recognizer in loop", action="store_true")
    parser.add_argument("--boardsize", help="set the board size", type=int)

    args = parser.parse_args()

    if not args.boardsize:
        args.boardsize = 10

    return args


def main():
    print "Starting board recognizer"

    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)

    args = getArgs()

    recognizer = BoardRecognizer(path + '/tests/test-1.avi')

    if args.continuous:
        while True:
            print recognizer.getBoardState()

            if cv2.waitKey(10) == ord('q'):
                break

    else:
        busConnection = BusConnector(5555, 5556)
        print "Waiting for requests from host"

        while True:
            request = busConnection.getRequest("recognizer");

            message = BoardMessage()
            message.ParseFromString(request)

            if message.requesttype == BoardMessage.GET_BOARD:
                print "getting boardState"

                try:
                    board = recognizer.getBoardState()
                    message.responsetype = BoardMessage.BOARD;
                    message.board = board
                except Exception as e:
                    print "An error occured"
                    print e
                    message.responsetype = BoardMessage.ERROR;

                print "Sending message"

                response = message.SerializeToString()
                busConnection.sendResponse("recognizer", response)

    return

if __name__ == "__main__":
    main()
