#ifndef AIBOARD_H
#define AIBOARD_H

#include <string>
#include <vector>
#include "Board.h"

class GameState
{
private:
    Board* board;

    std::vector<pieceType> friendPieces;
    std::vector<pieceType> enemyPieces;

    std::vector<Move> mergeMoves(Move first, std::vector<Move> second);
    std::vector<Move> appendMoves(std::vector<Move> first, std::vector<Move> second);

    std::vector<Move> getSuccessiveMoves(Move move);

    std::vector<Move> getMovesAtPosition(int position);
    std::vector<Move> getForcedMovesAtPosition(int position);

    template <typename T>
    bool vectorContains(std::vector<T> v, T x);

protected:
public:
    GameState(Board* startBoard, std::vector<pieceType> _friendPieces, std::vector<pieceType> _enemyPieces);

    std::vector<Move> getForcedMoves();
    std::vector<Move> getMoves();

    void doMove(Move move);

    int getScore();
};

#endif
