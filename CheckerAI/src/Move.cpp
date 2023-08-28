#include "Move.h"

#include <iostream>

Move::Move()
{
    newPiece.position = 0;
    newPiece.type = pieceType::invalid;
}

Move::Move(const aiconnector::Move& move)
{
    newPiece.position = move.newpiece().location();
    newPiece.type     = static_cast<pieceType>(move.newpiece().type()[0]);

    int i;
    for (i=0; i<move.removedpieces_size(); i++)
    {
        Piece removedPiece;
        removedPiece.position = move.removedpieces(i).location();
        removedPiece.type     = static_cast<pieceType>(move.removedpieces(i).type()[0]);

        removedPieces.push_back(removedPiece);
    }
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

void Move::serialize(aiconnector::Move* move)
{
    move->mutable_newpiece()->set_location(newPiece.position);

    move->mutable_newpiece()->set_type(std::string(1, newPiece.type));

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++)
    {
        aiconnector::Move::Piece* removedPiece = move->add_removedpieces();
        removedPiece->set_location(removedPieces[i].position);
        removedPiece->set_type(std::string(1, removedPieces[i].type));
    }
}
