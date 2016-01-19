#include "HostConnector.h"

HostConnector::HostConnector()
{
    std::cout << "Starting server" << std::endl;

    context = new zmq::context_t(1);
    socket = new zmq::socket_t(*context, ZMQ_REP);

    socket->bind("tcp://127.0.0.1:5555");

    std::cout << "Started server" << std::endl;
}

void HostConnector::setAI(AIPlayer* aiPlayer)
{
    ai = aiPlayer;
}

void HostConnector::getRequest()
{
    std::cout << "Waiting for host to ask for move" << std::endl;
    std::cout.flush();

    zmq::message_t request;
    socket->recv(&request);

    std::string responseString = "{\"response\": \"player-move\"}";
    zmq::message_t response(responseString.length()+1);
    memcpy ((void *) response.data(), responseString.c_str(), responseString.length());
    socket->send(response);

    std::cout << "Acknowledged" << std::endl;

    return;
}
