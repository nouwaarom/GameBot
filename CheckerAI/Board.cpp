#include "Board.h"

Board::Board(std::string representation)
{
   board = representation;
}

std::string Board::getBoardRepresentation()
{
    return board;
}

void Board::doMove(Move* move)
{

}

bool Board::isEnd()
{
    return true;
}
