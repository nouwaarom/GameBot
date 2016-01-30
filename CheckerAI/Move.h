#ifndef MOVE_H
#define MOVE_H

#include <string>
#include <vector>

#include "movemessage.pb.h"

enum pieceType : char
{
    white = 'w',
    white_crown = 'W',
    black = 'b',
    black_crown = 'B',
    empty = 'x'
};

struct Piece {
    int  position;
    pieceType type;
};

class Move
{
private:
    Piece newPiece;
    std::vector<Piece> removedPieces;
protected:
public:
    Move();
    Move(const aiconnector::Move& move);

    Move(Piece newPiece, std::vector<Piece> removedPieces);

    Piece getNewPiece();
    void setNewPiece(Piece piece);

    std::vector<Piece> getRemovedPieces();
    void setRemovedPieces(std::vector<Piece> pieces);
    void addRemovedPiece(Piece piece);

    void serialize(aiconnector::Move* move);
};

#endif
