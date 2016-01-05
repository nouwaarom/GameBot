#ifndef PLAYER_H
#define PLAYER_H

#include "Move.h"

class Player
{
private:
protected:
public:
    virtual Move* getMove();
    virtual void setOpponentMove(Move* move);
};

#endif
