#ifndef PLAYER_H
#define PLAYER_H

#include "Board.h"
#include "Move.h"

class Player
{
private:
protected:
public:
    virtual Move* getMove(Board board);
};

#endif
