#ifndef HUMANPLAYER_H
#define HUMANPLAYER_H

#include "Player.h"

class HumanPlayer : public Player
{
private:
protected:
public:
    Move* getMove(Board board);
};

#endif
