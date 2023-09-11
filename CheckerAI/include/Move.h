#ifndef MOVE_H
#define MOVE_H

#include <string>
#include <vector>

enum pieceType : char
{
    white = 'w',
    white_crown = 'W',
    black = 'b',
    black_crown = 'B',
    empty = 'x',
    invalid = '!',
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

        Move(Piece newPiece, std::vector<Piece> removedPieces);

        Piece getNewPiece() const;
        void setNewPiece(Piece piece);

        std::vector<Piece> getRemovedPieces() const;
        void setRemovedPieces(std::vector<Piece> pieces);
        void addRemovedPiece(Piece piece);
};

#endif
