from serial import Serial

class Controller():
    def __init__(self):
        print "Welcome to the arm controller"

    def doMove(self, move):
        print("Armcontroller is doing move")

        serial = Serial('/dev/ttyUSB0')
        serial.baudrate = 9600

        try:
            serial.write('x')
        except Exception as e:
            print "An error occured"
            print e
