#ifndef AIBOARD_H
#define AIBOARD_H

#include <string>
#include <vector>
#include "Board.h"

class AIBoard : public Board
{
private:
    std::vector<char> friendPieces;
    std::vector<char> enemyPieces;

    inline int getIndex(int row, int col);

    // Some ugly templates because std library doesnt have them
    template<typename T>
    bool vectorContains(std::vector<T> v, T x);

protected:
public:
    // This function is not in the right class
    Move selectRandomly(std::vector<Move> v);

    AIBoard(std::string representation, std::vector<char> _friendPieces, std::vector<char> _enemyPieces);

    std::vector<Move> getForcedMoves();
    std::vector<Move> getMoves();

    void doMove(Move* move);
    void undoMove(Move move);

    int getScore();
};

#endif
