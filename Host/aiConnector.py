import zmq
import random
import subprocess

from move import Move

class AIConnector:

    PROGRAM_PATH = "../CheckerAI/chess"

    def __init__(self, board, userStarts):
        difficulty = random.randint(0,99)

        aiCommand = [self.PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board.getBoardRepresentation())]
        print aiCommand
        #self.ai = subprocess.Popen(aiCommand, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)


        #if aiError:
        #    print aiError
        #else:
        #    print aiOutput

        # Start the connection to the AI
        context = zmq.Context()
        self.socket = context.socket(zmq.REQ)
        self.socket.connect("tcp://127.0.0.1:5555")

        print "Successfully talking to the AI now"


    def getMove(self):
        print "Please send please"
        self.socket.send(b"Please send please")

        print "waiting for response"
        message = self.socket.recv()

        print ("AI send: %s" % message)

    def setMove(self, move):
        print "User did clever move"
        self.socket.send(b"User did super clever move")

        print "waiting for response"
        message = self.socket.recv()
        print("AI send: %s" % message)

