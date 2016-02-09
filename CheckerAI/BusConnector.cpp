#include "BusConnector.h"
#include <iostream>

std::string BusConnector::s_recv(zmq::socket_t* socket)
{
    zmq::message_t message;
    socket->recv(&message);

    return std::string(static_cast<char*>(message.data()), message.size());
}

bool BusConnector::s_send(zmq::socket_t* socket, const std::string& string)
{
    zmq::message_t message(string.size());
    memcpy(message.data(), string.data(), string.size());

    bool rc = socket->send(message);
    return rc;
}

bool BusConnector::s_sendmore(zmq::socket_t* socket, const std::string& string)
{
    zmq::message_t message(string.size());
    memcpy(message.data(), string.data(), string.size());

    bool rc = socket->send(message, ZMQ_SNDMORE);
    return rc;
}

BusConnector::BusConnector()
{
    context = new zmq::context_t(1);

    publisher  = new zmq::socket_t(*context, ZMQ_PUB);
    publisher->connect("tcp://127.0.0.1:5555");

    subscriber = new zmq::socket_t(*context, ZMQ_SUB);
    subscriber->connect("tcp://127.0.0.1:5556");

    std::cout << "I am listening for the host" << std::endl;
}

std::string BusConnector::getRequest(std::string reciever)
{
    std::string topic = reciever + "_request";
    subscriber->setsockopt(ZMQ_SUBSCRIBE, topic.data(), topic.size());

    //  Read envelope with address
    std::string address = s_recv (subscriber);
    //  Read message contents
    std::string contents = s_recv (subscriber);

    return contents;
}

void BusConnector::sendResponse(std::string reciever, std::string message)
{
    s_sendmore(publisher, reciever + "_response");
    s_send(publisher, message);

    return;
}
