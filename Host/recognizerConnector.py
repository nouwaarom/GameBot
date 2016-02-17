import subprocess
import time
import config

from boardmessage_pb2 import BoardMessage

class RecognizerConnector:

    PROGRAM_PATH = "../BoardRecognizer/main.py"

    def __init__(self, bus):
        self.command = [self.PROGRAM_PATH]
        self.bus = bus

    def startBoardRecognizer(self):
        config.output.say("Starting board recognizer")
        self.ai = subprocess.Popen(self.command, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        time.sleep(1)

    def getCommand(self):
        return ' '.join(self.command)

    def endBoardRecognizer(self):
        self.ai.kill()

    def getBoardState(self):
        message = BoardMessage()
        message.requesttype = BoardMessage.GET_BOARD

        request = message.SerializeToString()
        response = self.bus.sendRequest("recognizer", request)

        message.ParseFromString(response)

        if message.responsetype == BoardMessage.BOARD:
            board = message.board
            return board

        else:
            print "Critical error, the board recognizer crashed"
            return -1