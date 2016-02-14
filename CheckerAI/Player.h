#ifndef PLAYER_H
#define PLAYER_H

#include <vector>

#include "Move.h"

class Player
{
    private:
        std::vector<pieceType> _pieces;
        std::vector<pieceType> _opponentPieces;

        Player* _opponent;

    protected:

    public:
        Player(std::vector<pieceType> pieces, std::vector<pieceType> opponentPieces);

        void setOpponent(Player* opponent);

        std::vector<pieceType> getPieces();
        std::vector<pieceType> getOpponentPieces();

        Player* getOpponent();
};

#endif
