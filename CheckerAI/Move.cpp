#include "Move.h"

Move::Move(std::string json)
{
    using boost::property_tree::ptree;

    std::stringstream ss;
    ss << json;

    ptree pt;
    boost::property_tree::read_json(ss, pt);

    BOOST_FOREACH(ptree::value_type &node, pt.get_child("response.move"))
    {
        int  newPosition = node.second.get<char>("newPos");
        char newType     = node.second.get<int>("newType");
        newPiece = {newPosition, newType};

        //Loop over all removed nodes
        BOOST_FOREACH(ptree::value_type &removedNode, node.second.get_child("removed"))
        {
            int  position = removedNode.second.get<char>("pos");
            char type     = removedNode.second.get<int>("type");
            removedPieces.push_back({position, type});
        }
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

std::string Move::getJson()
{
    using boost::property_tree::ptree;

    ptree propertyTree;
    ptree removedPiecesTree;

    propertyTree.put("newPos", newPiece.position);
    propertyTree.put("newType",    newPiece.type);

    //auto
    for (Piece &removedPiece : removedPieces)
    {
        ptree removedPieceTree, removedPosition, removedType;
        removedPosition.put("", removedPiece.position);
        removedType.put("", removedPiece.position);
        removedPieceTree.push_back(std::make_pair("pos", removedPosition));
        removedPieceTree.push_back(std::make_pair("type", removedType));

        removedPiecesTree.push_back(std::make_pair("", removedPieceTree));

    }

    propertyTree.add_child("removed", removedPiecesTree);

    std::stringstream stringStream;
    boost::property_tree::read_json(stringStream, propertyTree);

    std::string json;
    stringStream >> json;

    return json;
}
