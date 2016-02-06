import subprocess

import config

class RecognizerConnector:

    PROGRAM_PATH = "../BoardRecognizer/main.py"

    def __init__(self, startRecognizer):

        if startRecognizer:
            self.startBoardRecognizer()
        else:
            print "Execute this command(press any key to continue): "
            print ' '.join(aiCommand)
            raw_input()

    def startBoardRecognizer(self):
        config.output.say("Starting board recognizer")
        aiCommand = [self.PROGRAM_PATH]

        self.ai = subprocess.Popen(aiCommand, shell = False, stdin  = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    def getBoardState(self):
        print "To be implemented"
