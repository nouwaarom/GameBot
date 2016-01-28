#include "AIPlayer.h"

AIPlayer::AIPlayer(Board* startBoard, std::vector<char> friendPieces, std::vector<char> enemyPieces)
{
    board = new AIBoard(startBoard->getBoardRepresentation(), friendPieces, enemyPieces);
}

Move AIPlayer::getMove()
{
    Move move;
    std::vector<Move> moves = board->getForcedMoves();

    if (!moves.empty())
    {
        move =  board->selectRandomly(moves);
    }
    else {
        moves = board->getMoves();
        move =  board->selectRandomly(moves);
    }

    board->doMove(&move);

    return move;
}

void AIPlayer::setOpponentMove(Move* move)
{
    board->doMove(move);
}
