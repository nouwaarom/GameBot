#ifndef AIPLAYER_H
#define AIPLAYER_H

#include <vector>

#include "GameState.h"
#include "Player.h"
#include "Move.h"

class AIPlayer
{
    private:
        GameState* state;

        Player* selfPlayer;
        Player* opponentPlayer;

        Move selectRandomly(std::vector<Move> v);

    protected:

    public:
        AIPlayer(Board* startBoard, std::vector<pieceType> friendPieces, std::vector<pieceType> enemyPieces);

        Move getMove();
        void setOpponentMove(Move move);
};

#endif
