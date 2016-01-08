#ifndef AIBOARD_H
#define AIBOARD_H

#include <string>
#include <vector>
#include "Board.h"

class AIBoard : public Board
{
private:
protected:
public:
    AIBoard(std::string representation);

    std::vector<Move> getForcedMoves();
    std::vector<Move> getMoves();

    void doMove(Move move);
    void undoMove(Move move);

    int getScore();
};

#endif
