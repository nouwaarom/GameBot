#include "HumanPlayer.h"

#include <iostream>

using namespace std;

Move* HumanPlayer::getMove(Board board)
{
    int oldPosition, newPosition;

    cout << "Player: ";
    cin >> oldPosition;
    cin >> newPosition;

    Move* move = new Move(oldPosition, newPosition);

    return move;
}
