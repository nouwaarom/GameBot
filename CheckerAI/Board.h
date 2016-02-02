#ifndef BOARD_H
#define BOARD_H

#include <string>
#include "Move.h"

/*
 Class that handles the data for the board
 init: creates a board with standard setup
 or a saved setup if specified
*/
class Board
{
private:
    int getPosition(int row, int col);
protected:
    //Board is actually 10 by 10 but half of the tiles are always empty
	std::vector<pieceType> board;

public:
    Board(std::string representation);

    std::vector<pieceType>::iterator getBegin();
    std::vector<pieceType>::iterator getEnd();

    pieceType getPiece(int position);
    pieceType getPiece(int row, int col);

    void setPiece(int position, pieceType type);

    Move createMove(int newPosition, int oldPosition);
    Move createMove(int newRow, int newCol, int oldRow, int oldCol);

    void doMove(Move move);
    void undoMove(Move move);
};

#endif
