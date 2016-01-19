#ifndef MOVE_H
#define MOVE_H

#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include <boost/foreach.hpp>
#include <exception>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>

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
    Move(std::string json);
    Move(int oldPosition, int newPosition, std::string board);
    Move(Piece newPiece, std::vector<Piece> removedPieces);

    Piece getNewPiece();
    std::vector<Piece> getRemovedPieces();

    std::string getJson();
};

#endif
