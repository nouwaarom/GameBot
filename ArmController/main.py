#!/usr/bin/env python

from serial import Serial

from busConnector     import BusConnector
from boardmessage_pb2 import BoardMessage

def main():
    print "Welcome to the arm controller"

    busConnection = BusConnector(5555, 5556)

    serial = Serial('/dev/ttyUSB0')
    serial.baudrate = 9600

    print "Waiting for requests from host"

    while True:
        request = busConnection.getRequest("recognizer");

        message = BoardMessage()
        message.ParseFromString(request)

        if message.requesttype == BoardMessage.SET_BOARD:

            print "setting pieces"
            try:
                serial.write('x')
                print "Success"

                message.responsetype = BoardMessage.OK;
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
