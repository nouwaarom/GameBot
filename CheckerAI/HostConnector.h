#ifndef HOSTCONNECTOR_H
#define HOSTCONNECTOR_H

#include <vector>
#include <zmq.hpp>

#include "AIPlayer.h"
#include "movemessage.pb.h"

class HostConnector
{
private:
    AIPlayer* ai;
    zmq::context_t* context;
    zmq::socket_t* socket;
protected:
    void handleSetMove(aiconnector::MoveMessage& request);
    void handleGetMove(aiconnector::MoveMessage& request);
public:
    HostConnector();

    void setAI(AIPlayer* aiPlayer);

    // Blocks until request arrives, then handles it
    void getRequest();
};

#endif
