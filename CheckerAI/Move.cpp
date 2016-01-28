#include "Move.h"

#include <iostream>

Move::Move()
{
}

Move::Move(const aiconnector::Move& move)
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

// TODO check if there are hits
Move::Move(int newPosition, int oldPosition, std::string board)
{
    //piece goes to new position
    newPiece = {newPosition, board[oldPosition]};

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

        removedPieces.push_back({(5*row)+(col/2), board[(5*row)+(col/2)]});
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

std::vector<Piece> Move::getRemovedPieces()
{
    return removedPieces;
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
