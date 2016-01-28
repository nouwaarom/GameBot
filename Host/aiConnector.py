import zmq
import cv2
import random
import subprocess
import movemessage_pb2

class AIConnector:

    PROGRAM_PATH = "../CheckerAI/chess"

    def __init__(self, board, userStarts, execute):
        difficulty = random.randint(0,99)

        aiCommand = [self.PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board.getBoardRepresentation())]

        if execute:
            self.ai = subprocess.Popen(aiCommand, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        else:
            print "Execute this command(press any key to continue): "
            print ' '.join(aiCommand)

            cv2.waitKey(0)

        # Start the connection to the AI
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://127.0.0.1:5555")

        print "Successfully talking to the AI now"

    def terminateAI(self):
        self.ai.kill()

    def getMove(self):
        print "Requesting AI move ..."
        move_request = movemessage_pb2.MoveMessage()
        move_request.requesttype = movemessage_pb2.MoveMessage.GET_MOVE

        self.socket.send(move_request.SerializeToString())

        response = self.socket.recv()
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

        self.socket.send(move_request.SerializeToString())

        response = self.socket.recv()
        print "Recieved response"

        move_response = movemessage_pb2.MoveMessage()
        move_response.ParseFromString(response[0:-1])

        if move_response.responsetype == movemessage_pb2.MoveMessage.OK:
            print "Ai acknowledged move"
