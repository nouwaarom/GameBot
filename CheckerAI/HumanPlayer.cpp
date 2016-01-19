#include "HumanPlayer.h"

#include <string>
#include <iostream>

HumanPlayer::HumanPlayer(int port)
{
}

Move* HumanPlayer::getMove()
{
    /*
    std::string json;
    std::cin >> json;

    std::cout << "INPUT: " << json;

    */
    return new Move();
}

void HumanPlayer::setOpponentMove(Move* move)
{
    std::cout << "Waiting for host to set move" << std::endl;
    zmq::message_t request;
    socket->recv(&request);

    std::string moveMessage = move->getJson();
    zmq::message_t response(moveMessage.length()+1);
    memcpy ((void *) response.data(), moveMessage.c_str(), moveMessage.length());
    socket->send(response);

    std::cout << "Acknowledged" << std::endl;

    return;
}
