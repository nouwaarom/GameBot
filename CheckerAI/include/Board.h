#ifndef BOARD_H
#define BOARD_H

#include <string>
#include "Move.h"

typedef std::array<pieceType, 100> board_t;

/*
 Class that handles the data for the board
 init: creates a board with standard setup
 or a saved setup if specified
*/
class Board
{
private:
    static int getPosition(int row, int col);
protected:
    //Board is actually 10 by 10 but half of the tiles are always empty
	board_t board;

public:
    explicit Board(std::string representation);

    board_t::iterator getBegin();
    board_t::iterator getEnd();

    pieceType getPiece(int position);
    pieceType getPiece(int row, int col);
    void setPiece(int position, pieceType type);

    int getRow(int position);
    int getCol(int position);

    Move createMove(int newPosition, int oldPosition);
    Move createMove(int newRow, int newCol, int oldRow, int oldCol);

    void doMove(const Move& move);
    void undoMove(const Move& move);
};

#endif
