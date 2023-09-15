#ifndef BOARD_H
#define BOARD_H

#include <array>
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
public:
    explicit Board(std::string representation);

    int getNumberOfRows();
    int getNumberOfColumns();

    pieceType getPiece(int position);
    pieceType getPiece(int row, int col);
    void setPiece(int position, pieceType type);
    //! \brief Remove piece at position, if previous type is not correct throw an exception
    void removePiece(int position, pieceType previous_type);

    static int getRow(int position);
    static int getCol(int position);

    Move createMove(int newRow, int newCol, int oldRow, int oldCol);

    void doMove(const Move& move);
    void undoMove(const Move& move);

    //! \brief Print the state of the board.
    void debugPrint();

protected:
    //Board is actually 10 by 10 but half of the tiles are always empty
	board_t board;

private:
    static int getPosition(int row, int col);
};

#endif
