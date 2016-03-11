#!/usr/bin/env python

import os
import cv2
import argparse

from boardRecognizer  import BoardRecognizer
from Bus.busConnector import BusConnector

from boardmessage_pb2 import BoardMessage

class Recognizer:

    def __init__(self, boardsize):
        self.boardsize = boardsize

    def test(self):
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)

        recognizer = BoardRecognizer(path + '/tests/test-1.avi')

        while True:
            print recognizer.getBoardState()

            if cv2.waitKey(10) == ord('q'):
                break

    def getBoardState(self):
        recognizer = BoardRecognizer(0)

        try:
            board = recognizer.getBoardState()
            return board
        except Exception as e:
            print "An error occured"
            print e
