#include "AIPlayer.h"

#include <utility>
#include <algorithm>
#include <iostream>

AIPlayer::AIPlayer(Board* startBoard, std::vector<pieceType> friendPieces, std::vector<pieceType> enemyPieces)
{
    state = new GameState(startBoard);

    selfPlayer = new Player(friendPieces, enemyPieces);
    opponentPlayer = new Player(enemyPieces, friendPieces);
    selfPlayer->setOpponent(opponentPlayer);
    opponentPlayer->setOpponent(selfPlayer);

    return;
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
    std::pair<int, Move> valuemove = state->alphaBeta(8, -581357, 581357, selfPlayer, selfPlayer);

    Move move = valuemove.second;
    /*
    std::vector<move> moves = state->getforcedmoves(selfplayer);

    if (!moves.empty())
    {
        move = selectRandomly(moves);
    }
    else {
        moves = state->getMoves(selfPlayer);

        if (!moves.empty())
        {
            move =  selectRandomly(moves);
        }
        else {
            std::cout << "I am Unable to make a move" << std::endl;
        }
    }
    */

    state->doMove(move);

    return move;
}

void AIPlayer::setOpponentMove(Move move)
{
    state->doMove(move);
}
