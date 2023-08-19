import cv2
import time
import random
import subprocess

from .movemessage_pb2  import MoveMessage
from Bus.busConnector import BusConnector

class AIConnector:

    PROGRAM_PATH = "CheckerAI/cmake-build-debug/CheckerAI"

    def __init__(self, board, userStarts, bus):
        difficulty = random.randint(0,99)
        self.command = [self.PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board.getBoardRepresentation())]

        self.bus = bus

    def startAI(self):
        self.ai = subprocess.Popen(self.command, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        time.sleep(1)
        self.__printStandardOut()

    def getCommand(self):
        return ' '.join(self.command)

    def terminateAI(self):
        self.__printStandardOut()
        self.ai.kill()

    def getMove(self, board):
        print("Requesting AI move ...")
        move_request = MoveMessage()
        move_request.requesttype = MoveMessage.GET_MOVE

        response = self.bus.sendRequest("ai", move_request.SerializeToString())
        self.__printStandardOut()
        print("Recieved response")

        move_response = MoveMessage()
        move_response.ParseFromString(response)

        print("AI response: ")
        print(move_response)

        if move_response.responsetype == MoveMessage.MOVE:
            return move_response.move
        else:
            print("Shit happened")

    def setMove(self, move):
        print("Sending user move to AI")
        move_request = MoveMessage()
        move_request.requesttype = MoveMessage.SET_MOVE

        move_request.move.CopyFrom(move)

        response = self.bus.sendRequest("ai", move_request.SerializeToString())
        self.__printStandardOut()
        print("Recieved response")

        move_response = MoveMessage()
        move_response.ParseFromString(response)

        if move_response.responsetype == MoveMessage.OK:
            print("AI acknowledged move")
        else:
            print("AI did not acknowledge move")

    def __printStandardOut(self):
        pass
#        while True:
#            line = self.ai.stdout.readline()
#            if line is b'':
#                break;
#            print("AI: {}".format(line.rstrip()))

