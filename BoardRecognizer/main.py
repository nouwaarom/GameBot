#!/usr/bin/env python

from boardRecognizer import BoardRecognizer
from busConnector    import BusConnector

from boardmessage_pb2 import BoardMessage

def main():
    print "Starting board recognizer"

    recognizer = BoardRecognizer(0)

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
                print e
                message.responsetype = BoardMessage.ERROR;

            print "Sending message"

            response = message.SerializeToString()
            busConnection.sendResponse("recognizer", response)

    return

if __name__ == "__main__":
    main()
