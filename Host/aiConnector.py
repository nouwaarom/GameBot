import cv2
import time
import random
import subprocess
import movemessage_pb2

from busConnector import BusConnector

class AIConnector:

    PROGRAM_PATH = "../CheckerAI/ai"

    def __init__(self, board, userStarts, execute, bus):
        difficulty = random.randint(0,99)
        self.aiCommand = [self.PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board.getBoardRepresentation())]

        self.bus = bus

    def startAI(self):
        if execute:
            self.ai = subprocess.Popen(self.aiCommand, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            time.sleep(1)
        else:
            print "Execute this command(press any key to continue): "
            print ' '.join(aiCommand)

            cv2.waitKey(0)

    def terminateAI(self):
        self.ai.kill()

    def getMove(self):
        print "Requesting AI move ..."
        move_request = movemessage_pb2.MoveMessage()
        move_request.requesttype = movemessage_pb2.MoveMessage.GET_MOVE

        response = self.bus.sendRequest(move_request.SerializeToString())
        print "Recieved response"

        move_response = movemessage_pb2.MoveMessage()
        move_response.ParseFromString(response[0:-1])

        print "AI response: "
        print move_response

        if move_response.responsetype == movemessage_pb2.MoveMessage.MOVE:
            return move_response.move
        else:
            print("Shit happened")

    def setMove(self, move):
        print "User did clever move"
        move_request = movemessage_pb2.MoveMessage()
        move_request.requesttype = movemessage_pb2.MoveMessage.SET_MOVE

        move_request.move.CopyFrom(move)

        response = self.bus.sendRequest(move_request.SerializeToString())
        print "Recieved response"

        move_response = movemessage_pb2.MoveMessage()
        move_response.ParseFromString(response[0:-1])

        if move_response.responsetype == movemessage_pb2.MoveMessage.OK:
            print "Ai acknowledged move"
