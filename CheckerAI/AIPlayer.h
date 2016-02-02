#ifndef AIPLAYER_H
#define AIPLAYER_H

#include <vector>

#include "GameState.h"
#include "Move.h"

class AIPlayer
{
private:
    GameState* state;

    std::vector<pieceType> myTypes;
    std::vector<pieceType> enemyTypes;

    Move selectRandomly(std::vector<Move> v);
protected:
public:
    AIPlayer(Board* startBoard, std::vector<pieceType> friendPieces, std::vector<pieceType> enemyPieces);

    Move getMove();
    void setOpponentMove(Move move);
};

#endif
