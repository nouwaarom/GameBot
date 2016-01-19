#ifndef AIPLAYER_H
#define AIPLAYER_H

#include <vector>

#include "Player.h"
#include "AIBoard.h"

class AIPlayer : public Player
{
private:
    AIBoard* board;
protected:
public:
    AIPlayer(Board* startBoard, std::vector<char> pieces, std::vector<char> enemyPieces);

    Move* getMove();
    void setOpponentMove(Move* move);
};

#endif
