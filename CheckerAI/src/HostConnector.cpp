#include "HostConnector.h"

#include <iostream>

HostConnector::HostConnector()
{
    bus = new BusConnector();
}

void HostConnector::setAI(AIPlayer* aiPlayer)
{
    ai = aiPlayer;
}

void HostConnector::handleSetMove(aiconnector::MoveMessage& request)
{
    std::cout << "Set Move" << std::endl;

    //Set the move
    ai->setOpponentMove(createMoveFromProtobuf(request.move()));

    request.set_responsetype(aiconnector::MoveMessage::OK);

    return;
}

void HostConnector::handleGetMove(aiconnector::MoveMessage& request)
{
    std::cout << "Get Move" << std::endl;

    Move move = ai->getMove();

    serializeMoveToProtobuf(move, request.mutable_move());
    request.set_responsetype(aiconnector::MoveMessage::MOVE);

    return;
}

void HostConnector::getRequest()
{
    std::cout << "Waiting for host to ask for move" << std::endl;

    // Wait for a request
    std::string request = bus->getRequest("ai");

    // Unserialize the request
    aiconnector::MoveMessage move_message;
    if (!move_message.ParseFromString(std::string(request)))
    {
        std::cerr << "Failed to parse request." << std::endl;
        move_message.set_responsetype(aiconnector::MoveMessage::ERROR);
    }
    else
    {
        // Process the request
        switch (move_message.requesttype())
        {
            case aiconnector::MoveMessage::GET_MOVE:
                handleGetMove(move_message);
                break;

            case aiconnector::MoveMessage::SET_MOVE:
                handleSetMove(move_message);
                break;

            default:
                std::cout << "Invalid Request" << std::endl;
                move_message.set_responsetype(aiconnector::MoveMessage::ERROR);
                break;
        }
    }

    std::string response;
    move_message.SerializeToString(&response);

    bus->sendResponse("ai", response);

    std::cout << "Acknowledged" << std::endl;

    return;
}

Move HostConnector::createMoveFromProtobuf(const aiconnector::Move& protomove)
{
    Piece newPiece;
    newPiece.position = protomove.newpiece().location();
    newPiece.type     = static_cast<pieceType>(protomove.newpiece().type()[0]);

    std::vector<Piece> removedPieces;
    for (int i = 0; i < protomove.removedpieces_size(); i++)
    {
        Piece removedPiece;
        removedPiece.position = protomove.removedpieces(i).location();
        removedPiece.type     = static_cast<pieceType>(protomove.removedpieces(i).type()[0]);

        removedPieces.push_back(removedPiece);
    }

    return Move(newPiece, removedPieces);
}

void HostConnector::serializeMoveToProtobuf(const Move& move, aiconnector::Move* protomove)
{
    protomove->mutable_newpiece()->set_location(move.getNewPiece().position);

    protomove->mutable_newpiece()->set_type(std::string(1, move.getNewPiece().type));

    for (int i=0; i<move.getRemovedPieces().size(); i++)
    {
        aiconnector::Move::Piece* removedPiece = protomove->add_removedpieces();
        removedPiece->set_location(move.getRemovedPieces()[i].position);
        removedPiece->set_type(std::string(1, move.getRemovedPieces()[i].type));
    }
}
