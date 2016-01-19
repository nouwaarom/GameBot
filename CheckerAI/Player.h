#ifndef PLAYER_H
#define PLAYER_H

#include <vector>
#include "Move.h"

class Player
{
private:
   std::vector<char> myTypes;
   std::vector<char> enemyTypes;
protected:
public:
    virtual Move* getMove();
    virtual void setOpponentMove(Move* move);
};

#endif
