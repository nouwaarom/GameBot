#include "AIPlayer.h"

AIPlayer::AIPlayer(Board* startBoard)
{
    board = new AIBoard(startBoard->getBoardRepresentation());
}

Move* AIPlayer::getMove()
{
    return new Move(1,2, board->getBoardRepresentation());
}

void AIPlayer::setOpponentMove(Move* move)
{
    return;
}
