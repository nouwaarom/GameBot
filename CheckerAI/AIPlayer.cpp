#include "AIPlayer.h"

#include <algorithm>

AIPlayer::AIPlayer(Board* startBoard, std::vector<pieceType> friendPieces, std::vector<pieceType> enemyPieces)
{
    state = new GameState(startBoard, friendPieces, enemyPieces);

    myTypes    = friendPieces;
    enemyTypes = enemyPieces;
}

Move AIPlayer::selectRandomly(std::vector<Move> v)
{
    static std::random_device rd;
    static std::mt19937 gen(rd());

    std::vector<Move>::iterator start = v.begin();
    std::vector<Move>::iterator end   = v.end();

    std::uniform_int_distribution<> dis(0, std::distance(start, end) - 1);
    std::advance(start, dis(gen));

    return *start;
}

Move AIPlayer::getMove()
{
    Move move;
    std::vector<Move> moves = state->getForcedMoves();

    if (!moves.empty())
    {
        move = selectRandomly(moves);
    }
    else {
        moves = state->getMoves();
        move =  selectRandomly(moves);
    }

    state->doMove(&move);

    return move;
}

void AIPlayer::setOpponentMove(Move* move)
{
    state->doMove(move);
}
