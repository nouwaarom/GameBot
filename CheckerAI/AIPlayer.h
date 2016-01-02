#ifndef AIPLAYER_H
#define AIPLAYER_H

#include "Player.h"

class AIPlayer : public Player
{
private:
    Board* board;
protected:
public:
    AIPlayer(Board* board);

    Move* getMove();
};

#endif
