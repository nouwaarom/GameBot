#include "Board.h"
#include <stdexcept>
#include <iostream>
#include <sstream>

Board::Board(std::string representation)
{
    int index = 0;
    for (char& c : representation) {
        board[index++] = (static_cast<pieceType>(c));
    }
}

int Board::getNumberOfRows()
{
    return 10;
}

int Board::getNumberOfColumns()
{
    return 10;
}

int Board::getPosition(int row, int col)
{
    return (5*row) + (col/2);
}

pieceType Board::getPiece(int row, int col)
{
    if (row < 0 || row >= 10 || col < 0 || col >= 10) {
        std::stringstream error_message;
        error_message << "Attempt to get piece at invalid board position: (" << row << "," << col << ")";

        throw std::runtime_error(error_message.str());
    }

    if ((col + row) % 2 == 1) {
        return pieceType::empty;
    }
    return getPiece(getPosition(row, col));
}

pieceType Board::getPiece(int position)
{
    return board[position];
}

void Board::setPiece(int position, pieceType type)
{
    board[position] = type;
}

void Board::removePiece(int position, pieceType previous_type)
{
    if (board[position] != previous_type) {
        std::stringstream error_message;
        error_message << "Attempt to remove a '" << previous_type << "' at position" << position << ", but position contains a '" << board[position] << "'";

        throw std::runtime_error(error_message.str());
    }

    board[position] = pieceType::empty;
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

Move Board::createMove(int newRow, int newCol, int oldRow, int oldCol)
{
    Move move;
    // oldPiece goes to new location, gets crowned if it reached the other side
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

    int row_delta = (oldRow-newRow)/abs(oldRow-newRow); // direction to move in (-1 or 1)
    int col_delta = (oldCol-newCol)/abs(oldCol-newCol); // direction to move in (-1 or 1)
    for (int i = 0; i < abs(oldRow-newRow); i++) {
        row += row_delta;
        col += col_delta;
        pieceType piece = getPiece(row, col);
        if (piece == pieceType::empty) {
            continue;
        }

        move.addRemovedPiece({getPosition(row, col), piece});
    }

    return move;
}

void Board::doMove(const Move& move)
{
    Piece newPiece = move.getNewPiece();
    std::vector<Piece> removedPieces = move.getRemovedPieces();

    setPiece(newPiece.position, newPiece.type);

    for (int i = 0; i < removedPieces.size(); i++) {
        Piece toRemove = removedPieces[i];
        removePiece(toRemove.position, toRemove.type);
    }

    return;
}

void Board::undoMove(const Move& move)
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

void Board::debugPrint()
{
    for (int row = 0; row < 10; row++) {
        for (int col = 0; col < 10; col++) {
            pieceType type = getPiece(row, col);
            char c = (type == pieceType::empty) ? ' ' : static_cast<char>(type);
            std::cout << c;
        }
        std::cout << std::endl;
    }
}
