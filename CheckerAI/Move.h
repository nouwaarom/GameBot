#ifndef MOVE_H
#define MOVE_H

#include <string>
#include <vector>

#include "movemessage.pb.h"

struct Piece {
    int  position;
    char type;
};

class Move
{
private:
    Piece newPiece;
    std::vector<Piece> removedPieces;
protected:
public:
    Move();
    Move(const aiconnector::MoveMessage::Move& move);

    Move(int oldPosition, int newPosition, std::string board);
    Move(Piece newPiece, std::vector<Piece> removedPieces);

    Piece getNewPiece();
    std::vector<Piece> getRemovedPieces();

    void serialize(aiconnector::MoveMessage::Move* move);
};

#endif
