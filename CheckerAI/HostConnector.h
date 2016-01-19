#ifndef HOSTCONNECTOR_H
#define HOSTCONNECTOR_H

#include <vector>
#include <zmq.hpp>

#include "AIPlayer.h"

class HostConnector
{
private:
    AIPlayer* ai;
    zmq::context_t* context;
    zmq::socket_t* socket;
protected:
public:
    HostConnector();

    void setAI(AIPlayer* aiPlayer);

    void getRequest();
};

#endif
