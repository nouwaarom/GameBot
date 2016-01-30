#ifndef AIBOARD_H
#define AIBOARD_H

#include <string>
#include <vector>
#include "Board.h"

class GameState
{
private:
    std::vector<pieceType> friendPieces;
    std::vector<pieceType> enemyPieces;

    Board* board;

    // Some ugly templates because std library doesnt have them
    template<typename T>
    bool vectorContains(std::vector<T> v, T x);

protected:
public:
    GameState(Board* startBoard, std::vector<pieceType> _friendPieces, std::vector<pieceType> _enemyPieces);

    std::vector<Move> getForcedMoves();
    std::vector<Move> getMoves();

    void doMove(Move* move);
    void undoMove(Move move);

    int getScore();
};

#endif
