#!/usr/bin/env python

import zmq

def main():
    print("Starting bus shizzle")

    context = zmq.Context()

    publish = context.socket(zmq.XPUB)
    publish.bind("tcp://127.0.0.1:5556")

    subscribe = context.socket(zmq.XSUB)
    subscribe.bind("tcp://127.0.0.1:5555")

    # Start proxy
    zmq.proxy(subscribe, publish);

if __name__ == "__main__":
    main()
