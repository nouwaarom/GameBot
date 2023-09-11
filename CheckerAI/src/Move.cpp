#include "Move.h"

#include <iostream>

Move::Move()
{
    newPiece.position = 0;
    newPiece.type = pieceType::invalid;
}


Move::Move(Piece _newPiece, std::vector<Piece> _removedPieces)
{
    newPiece = _newPiece;
    removedPieces = _removedPieces;
}

Piece Move::getNewPiece() const
{
    return newPiece;
}


void Move::setNewPiece(Piece piece)
{
    newPiece = piece;
}

std::vector<Piece> Move::getRemovedPieces() const
{
    return removedPieces;
}

void Move::setRemovedPieces(std::vector<Piece> pieces)
{
    removedPieces = pieces;
}

void Move::addRemovedPiece(Piece piece)
{
    removedPieces.push_back(piece);
}

