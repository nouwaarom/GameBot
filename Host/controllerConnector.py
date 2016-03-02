import subprocess
import time

from boardmessage_pb2 import BoardMessage

class ControllerConnector:

    PROGRAM_PATH = "../ArmController/main.py"

    def __init__(self, bus, boardsize):
        self.command = [self.PROGRAM_PATH]
        self.bus = bus

        self.boardsize = boardsize

    def startArmController(self):
        print("Starting arm controller")
        self.armcontroller = subprocess.Popen(self.command, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        time.sleep(1)

    def getCommand(self):
        return ' '.join(self.command)

    def endArmController(self):
        self.armcontroller.kill()

    def setBoardState(self, boardString):
        message = BoardMessage()
        message.requesttype = BoardMessage.SET_BOARD
        message.board = boardString

        request = message.SerializeToString()
        response = self.bus.sendRequest("recognizer", request)

        message.ParseFromString(response)

        if message.responsetype == BoardMessage.OK:
            return 0
        else:
            return -1
