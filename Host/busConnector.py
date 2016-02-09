import zmq
import time
import subprocess

class BusConnector:

    PROGRAM_PATH = "../Bus/bus"

    def __init__(self, publishPort, subscribePort):
        self.context = zmq.Context()

        self.publishPort = publishPort
        self.subscribePort = subscribePort

        self.command = [self.PROGRAM_PATH, str(self.publishPort), str(self.subscribePort)]

    def startPublisher(self):
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.connect("tcp://127.0.0.1:5555")

    def startSubscriber(self):
        self.subscriber = self.context.socket(zmq.SUB)
        self.subscriber.connect("tcp://127.0.0.1:5556")

    # Send a request and return response
    def sendRequest(self, reciever, message):
        self.subscriber.setsockopt(zmq.SUBSCRIBE, reciever + "_response")

        self.publisher.send_multipart([reciever + "_request ", message])

        [adress, content] = self.subscriber.recv_multipart()
        return content

    # Creates a new thread with a XPUB/XSUB proxy
    def startBus(self):
        self.bus = subprocess.Popen(self.command, shell = False)
        time.sleep(1)

    def getCommand(self):
        return ' '.join(self.command)

    def endBus(self):
        self.bus.kill()
