#ifndef BUSCONNECTOR_H
#define BUSCONNECTOR_H

#include <zmq.hpp>

class BusConnector
{
    private:
        zmq::context_t* context;
        zmq::socket_t*  publisher;
        zmq::socket_t*  subscriber;

        std::string s_recv(zmq::socket_t* socket);
        bool s_send(zmq::socket_t* socket, const std::string & string);
        bool s_sendmore(zmq::socket_t* socket, const std::string & string);

    protected:

    public:
        BusConnector();

        std::string getRequest(std::string reciever);

        void sendResponse(std::string reciever, std::string message);
};

#endif
