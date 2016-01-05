#ifndef AIBOARD_H
#define AIBOARD_H

#include <string>
#include "Board.h"

class AIBoard : public Board
{
private:
protected:
public:
    AIBoard(std::string representation);

    Move* getMoves();

    void doMove(Move* move);
    void undoMove(Move* move);

    int getUtility();
};

#endif
