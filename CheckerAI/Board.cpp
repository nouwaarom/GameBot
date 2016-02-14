#include "Board.h"

Board::Board(std::string representation)
{
    for (char& c : representation) {
        board.push_back(static_cast<pieceType>(c));
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
    if (row >= 0 && row < 10) {
        if (col >= 0 && col < 10) {
            return getPiece(getPosition(row, col));
        }
    }

    return pieceType::invalid;
}

pieceType Board::getPiece(int position)
{
    return board[position];
}

void Board::setPiece(int position, pieceType type)
{
    board[position] = type;
}

int Board::getRow(int position)
{
    return position / 5;
}

int Board::getCol(int position)
{
    int row = position / 5;
    return 2*(position % 5) + (row % 2);
}

Move Board::createMove(int newPosition, int oldPosition)
{
    int oldRow = oldPosition / 5;
    int oldCol = 2*(oldPosition % 5) + (oldRow % 2);

    int newRow = newPosition / 5;
    int newCol = 2*(newPosition % 5) + (newRow % 2);

    return createMove(newRow, newCol, oldRow, oldCol);
}

Move Board::createMove(int newRow, int newCol, int oldRow, int oldCol)
{
    Move move;
    // oldPiece goes to new location, gets crowned if it reached teh other side
    pieceType oldPiece = getPiece(oldRow, oldCol);
    if ((oldPiece == pieceType::white) && newRow == 9) {
        oldPiece = pieceType::white_crown;
    }
    if ((oldPiece == pieceType::black) && newRow == 0) {
        oldPiece = pieceType::black_crown;
    }

    move.setNewPiece({getPosition(newRow, newCol), oldPiece});

    int row = newRow;
    int col = newCol;

    int i;
    for (i=0; i < abs(oldRow-newRow); i++) {

        row += (oldRow-newRow)/abs(oldRow-newRow);
        col += (oldCol-newCol)/abs(oldCol-newCol);

        move.addRemovedPiece({getPosition(row, col), getPiece(row, col)});
    }

    return move;
}

void Board::doMove(Move move)
{
    Piece newPiece = move.getNewPiece();
    std::vector<Piece> removedPieces = move.getRemovedPieces();

    setPiece(newPiece.position, newPiece.type);

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++) {
        setPiece(removedPieces[i].position, pieceType::empty);
    }

    return;
}

void Board::undoMove(Move move)
{
    Piece newPiece = move.getNewPiece();
    std::vector<Piece> removedPieces = move.getRemovedPieces();

    setPiece(newPiece.position, pieceType::empty);

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++)
    {
        setPiece(removedPieces[i].position, removedPieces[i].type);
    }

    return;
}
