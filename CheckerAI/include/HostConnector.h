#ifndef HOSTCONNECTOR_H
#define HOSTCONNECTOR_H

#include <vector>

#include "AIPlayer.h"
#include "movemessage.pb.h"
#include "BusConnector.h"

class HostConnector
{
public:
    HostConnector();

    void setAI(AIPlayer* aiPlayer);

    // Blocks until request arrives, then handles it
    void getRequest();

protected:
    void handleSetMove(aiconnector::MoveMessage& request);
    void handleGetMove(aiconnector::MoveMessage& request);

private:
    Move createMoveFromProtobuf(const aiconnector::Move& protobuf);
    void serializeMoveToProtobuf(const Move& move, aiconnector::Move* protobuf);

    AIPlayer* ai;
    BusConnector* bus;
};

#endif
