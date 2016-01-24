#include "HostConnector.h"

#include <iostream>

HostConnector::HostConnector()
{
    std::cout << "Starting server" << std::endl;

    context = new zmq::context_t(1);
    socket = new zmq::socket_t(*context, ZMQ_REP);

    socket->bind("tcp://127.0.0.1:5555");

    std::cout << "Started server" << std::endl;
}

void HostConnector::setAI(AIPlayer* aiPlayer)
{
    ai = aiPlayer;
}

void HostConnector::handleSetMove(aiconnector::MoveMessage& request)
{
    std::cout << "Set Move" << std::endl;

    //Set the move
    ai->setOpponentMove(new Move(request.move()));

    request.set_responsetype(aiconnector::MoveMessage::OK);

    return;
}

void HostConnector::handleGetMove(aiconnector::MoveMessage& request)
{
    std::cout << "Get Move" << std::endl;

    Move* move = ai->getMove();

    move->serialize(request.mutable_move());
    request.set_responsetype(aiconnector::MoveMessage::MOVE);

    return;
}

void HostConnector::getRequest()
{
    std::cout << "Waiting for host to ask for move" << std::endl;

    // Wait for a request
    zmq::message_t zrequest;
    socket->recv(&zrequest);

    // Unserialize the request
    aiconnector::MoveMessage move_message;
    if (!move_message.ParseFromString(std::string(static_cast<char*>(zrequest.data()), zrequest.size())))
    {
      std::cerr << "Failed to parse request." << std::endl;
      return;
    }

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
            break;
    }


    std::string responseString;
    move_message.SerializeToString(&responseString);

    zmq::message_t response(responseString.length()+1);
    memcpy ((void *) response.data(), responseString.c_str(), responseString.length());
    socket->send(response);

    std::cout << "Acknowledged" << std::endl;

    return;
}
