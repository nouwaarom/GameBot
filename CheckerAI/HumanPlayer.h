#ifndef HUMANPLAYER_H
#define HUMANPLAYER_H

#include "Player.h"
#include <zmq.hpp>

class HumanPlayer : public Player
{
private:
    zmq::socket_t* socket;
protected:
public:
    HumanPlayer(int port);
    Move* getMove();
    void setOpponentMove(Move* move);
};

#endif
