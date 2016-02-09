import zmq

class BusConnector:

    def __init__(self, publishPort, subscribePort):
        context = zmq.Context()

        self.publisher = context.socket(zmq.PUB)
        self.publisher.connect("tcp://127.0.0.1:5555")

        self.subscriber = context.socket(zmq.SUB)
        self.subscriber.connect("tcp://127.0.0.1:5556")

    # Send a request and return response
    def getRequest(self, reciever):
        self.subscriber.setsockopt(zmq.SUBSCRIBE, reciever + "_request")

        [adress, content] =  self.subscriber.recv_multipart()
        return content

    def sendResponse(self, reciever, message):
        self.publisher.send_multipart([reciever + "_response ", message])
