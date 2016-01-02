#include "Board.h"

int Board::removePiece(int location)
{
    if (location>=0 && location<50)
    {
        board[location] = 'x';
        return 1;
    }

    return -1;
}

int Board::setPiece(int location, char piece)
{
    if (location>=0 && location<50)
    {
        if (board[location] == 'x')
        {
            board[location] = piece;
            return 1;
        }
    }

    return -1;
}

char Board::getPieceAtLocation(int location)
{
    if (location>=0 && location<50)
    {
        return board[location];
    }

    return -1;
}

Board::Board()
{
    // Create string of x's of length 50
    std::string board(50, 'x');

    // Set the white and black pieces
    int i;
    for (i=0; i<20; i++) {
        board[i] = WHITE;
    }

    for (i=30; i<50; i++) {
        board[i] = BLACK;
    }
}

Board::Board(std::string representation)
{
   board = representation;
}
