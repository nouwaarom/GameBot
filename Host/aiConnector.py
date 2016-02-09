import cv2
import time
import random
import subprocess

from movemessage_pb2 import MoveMessage
from busConnector    import BusConnector

class AIConnector:

    PROGRAM_PATH = "../CheckerAI/ai"

    def __init__(self, board, userStarts, bus):
        difficulty = random.randint(0,99)
        self.command = [self.PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board.getBoardRepresentation())]

        self.bus = bus

    def startAI(self):
        self.ai = subprocess.Popen(self.command, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        time.sleep(1)

    def getCommand(self):
        return ' '.join(self.command)

    def terminateAI(self):
        self.ai.kill()

    def getMove(self):
        print "Requesting AI move ..."
        move_request = MoveMessage()
        move_request.requesttype = MoveMessage.GET_MOVE

        response = self.bus.sendRequest("ai", move_request.SerializeToString())
        print "Recieved response"

        move_response = MoveMessage()
        # Only drop last character if message is from c program
        # Dunno if that's true, but this should work
        move_response.ParseFromString(response)

        print "AI response: "
        print move_response

        if move_response.responsetype == MoveMessage.MOVE:
            return move_response.move
        else:
            print("Shit happened")

    def setMove(self, move):
        print "User did clever move"
        move_request = MoveMessage()
        move_request.requesttype = MoveMessage.SET_MOVE

        move_request.move.CopyFrom(move)

        response = self.bus.sendRequest("ai", move_request.SerializeToString())
        print "Recieved response"

        move_response = MoveMessage()
        move_response.ParseFromString(response)

        if move_response.responsetype == MoveMessage.OK:
            print "Ai acknowledged move"
