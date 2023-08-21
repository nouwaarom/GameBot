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
    ai->setOpponentMove(Move(request.move()));

    request.set_responsetype(aiconnector::MoveMessage::OK);

    return;
}

void HostConnector::handleGetMove(aiconnector::MoveMessage& request)
{
    std::cout << "Get Move" << std::endl;

    Move move = ai->getMove();

    move.serialize(request.mutable_move());
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
