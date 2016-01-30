#include "Board.h"

Board::Board(std::string representation)
{
    for (char& c : representation) {
        board.insert(board.begin(), static_cast<pieceType>(c));
    }
}

std::vector<pieceType>::iterator Board::getBegin()
{
    return board.begin();
}

std::vector<pieceType>::iterator Board::getEnd()
{
    return board.end();
}

int Board::getPosition(int row, int col)
{
    return ((5*row) + (col/2));
}

pieceType Board::getPiece(int row, int col)
{
    return board[getPosition(row, col)];
}

pieceType Board::getPiece(int position)
{
    return board[position];
}

void Board::setPiece(int position, pieceType type)
{
    board[position] = type;
}

Move Board::createMove(int newPosition, int oldPosition)
{
    Move move;
    //piece goes to new position
    move.setNewPiece({newPosition, board[oldPosition]});

    int oldRow = oldPosition / 5;
    int oldCol = 2*(oldPosition % 5) + (oldRow % 2);

    int newRow = newPosition / 5;
    int newCol = 2*(newPosition % 5) + (newRow % 2);

    int row = newRow;
    int col = newCol;

    int i;
    for (i=0; i < abs(oldRow-newRow); i++) {

        row += (oldRow-newRow)/abs(oldRow-newRow);
        col += newCol + (oldCol-newCol)/abs(oldCol-newCol);

        move.addRemovedPiece({(5*row)+(col/2), board[(5*row)+(col/2)]});
    }

    return move;
}

Move Board::createMove(int newRow, int newCol, int oldRow, int oldCol)
{
    Move move;
    //piece goes to new position
    move.setNewPiece({getPosition(newRow, newCol), getPiece(oldRow, oldCol)});

    int row = newRow;
    int col = newCol;

    int i;
    for (i=0; i < abs(oldRow-newRow); i++) {

        row += (oldRow-newRow)/abs(oldRow-newRow);
        col += newCol + (oldCol-newCol)/abs(oldCol-newCol);

        move.addRemovedPiece({getPosition(row, col), getPiece(row, col)});
    }

    return move;
}

void Board::doMove(Move* move)
{

}
