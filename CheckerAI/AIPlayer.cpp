#include "AIPlayer.h"

AIPlayer::AIPlayer(Board* startBoard)
{
    board = startBoard;
}

Move* AIPlayer::getMove()
{
    return new Move(1,2);
}
