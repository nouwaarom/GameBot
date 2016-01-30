#include "Move.h"

#include <iostream>

Move::Move()
{
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

Move::Move(Piece newPiece, std::vector<Piece> removedPieces)
{
    newPiece = newPiece;
    removedPieces = removedPieces;
}

Piece Move::getNewPiece()
{
    return newPiece;
}


void Move::setNewPiece(Piece piece)
{
    newPiece = piece;
}

std::vector<Piece> Move::getRemovedPieces()
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

    std::cout << "newpiece type: " << newPiece.type << std::endl;
    move->mutable_newpiece()->set_type(std::string(1, newPiece.type));

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++)
    {
        aiconnector::Move::Piece* removedPiece = move->add_removedpieces();
        removedPiece->set_location(removedPieces[i].position);
        removedPiece->set_type(std::string(1, removedPieces[i].type));
    }
}
