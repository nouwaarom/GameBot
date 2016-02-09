#ifndef HOSTCONNECTOR_H
#define HOSTCONNECTOR_H

#include <vector>

#include "AIPlayer.h"
#include "movemessage.pb.h"
#include "BusConnector.h"

class HostConnector
{
private:
    AIPlayer* ai;
    BusConnector* bus;
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
