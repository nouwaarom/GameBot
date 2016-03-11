import zmq
import threading

class Bus:
    def __init__(self):
        print("Bus object created")

    def startBus(self):
        self.context = zmq.Context()

        self.thread = threading.Thread(target=self.busThreadFunction)
        self.thread.start()

    def busThreadFunction(self):
        print("Bus thread created")

        publish = self.context.socket(zmq.XPUB)
        publish.bind("tcp://127.0.0.1:5556")

        subscribe = self.context.socket(zmq.XSUB)
        subscribe.bind("tcp://127.0.0.1:5555")

        # Start proxy
        try:
            zmq.proxy(subscribe, publish);
        except Exception as e:
            print("Bus terminated")

    def endBus(self):
        print("Terminating Bus")
        self.context.destroy()
        self.thread.join()

