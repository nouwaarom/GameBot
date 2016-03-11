import zmq
import time
import subprocess

class BusConnector:

    def __init__(self, publishPort, subscribePort):
        self.context = zmq.Context()

        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.connect("tcp://127.0.0.1:5555")

        self.subscriber = self.context.socket(zmq.SUB)
        self.subscriber.connect("tcp://127.0.0.1:5556")

    # Send a request and return response
    def sendRequest(self, reciever, message):
        self.subscriber.setsockopt(zmq.SUBSCRIBE, reciever + "_response")

        self.publisher.send_multipart([reciever + "_request ", message])

        [adress, content] = self.subscriber.recv_multipart()
        return content

    # Send a request and return response
    def getRequest(self, reciever):
        self.subscriber.setsockopt(zmq.SUBSCRIBE, reciever + "_request")

        [adress, content] =  self.subscriber.recv_multipart()
        return content

    def sendResponse(self, reciever, message):
        self.publisher.send_multipart([reciever + "_response ", message])
