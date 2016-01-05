#ifndef AIPLAYER_H
#define AIPLAYER_H

#include "Player.h"
#include "AIBoard.h"

class AIPlayer : public Player
{
private:
    AIBoard* board;
protected:
public:
    AIPlayer(Board* board);

    Move* getMove();
    void setOpponentMove(Move* move);
};

#endif
