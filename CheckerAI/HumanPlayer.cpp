#include "HumanPlayer.h"

#include <iostream>

Move* HumanPlayer::getMove()
{
    std::cout << "{\"request\": \"player-move\"}";

    std::string json;
    std::cin >> json;

    return new Move(json);
}

void HumanPlayer::setOpponentMove(Move* move)
{
    std::cout << move->getJson();

    return;
}
