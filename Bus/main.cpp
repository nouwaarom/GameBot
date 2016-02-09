
#include <iostream>
using namespace std;

#include "zmq.hpp"

#include "publish.hpp"
#include "subscribe.hpp"

int main(int argc, char** argv)
{
	// create context
	zmq::context_t ctx(1);

    cout << "Starting publisher" << endl;
	// build publisher -- connects to subscribers
	zmq::socket_t publish(ctx, ZMQ_XPUB);
    publish.bind("tcp://127.0.0.1:5556");

    cout << "Starting subscriber" << endl;
	// build subscriber -- connects to publishers
    zmq::socket_t subscribe(ctx, ZMQ_XSUB);
    subscribe.bind("tcp://127.0.0.1:5555");
	//subscribe.setsockopt(ZMQ_SUBSCRIBE, "", 0);

    cout << "Starting proxy" << endl;

	// start device
	zmq::proxy(subscribe, publish, NULL);

    cout << "Done" << endl;

	return 0;
}
