#include "Move.h"

Move::Move()
{
}

Move::Move(const aiconnector::MoveMessage::Move& move)
{
    newPiece.position = move.newpiece().location();
    newPiece.type     = move.newpiece().type()[0];

    int i;
    for (i=0; i<move.removedpieces_size(); i++)
    {
        Piece removedPiece;
        removedPiece.position = move.removedpieces(i).location();
        removedPiece.type     = move.removedpieces(i).type()[0];

        removedPieces.push_back(removedPiece);
    }
}

Move::Move(int oldPosition, int newPosition, std::string board)
{
    //piece goes to new position
    newPiece = {newPosition, board[oldPosition]};

    //remove the piece at the oldLocation
    removedPieces.push_back({oldPosition, board[oldPosition]});
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

std::vector<Piece> Move::getRemovedPieces()
{
    return removedPieces;
}

void Move::serialize(aiconnector::MoveMessage::Move* move)
{
    move->mutable_newpiece()->set_location(newPiece.position);
    std::string pieceType = std::string(newPiece.type, 1);
    move->mutable_newpiece()->set_type(pieceType);

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++)
    {
        aiconnector::MoveMessage::Piece* removedPiece = move->add_removedpieces();
        removedPiece->set_location(removedPieces[i].position);
        std::string pieceType = std::string(removedPieces[i].type, 1);
        removedPiece->set_type(pieceType);

    }
}
