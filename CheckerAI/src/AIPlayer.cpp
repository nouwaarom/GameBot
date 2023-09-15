#include "AIPlayer.h"

#include <random>
#include <utility>
#include <algorithm>
#include <iostream>

AIPlayer::AIPlayer(Board* startBoard, std::vector<pieceType> friendPieces, std::vector<pieceType> enemyPieces)
{
    state = new GameState(startBoard);
    alpha_beta = new AlphaBeta(state);

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
    std::pair<int, Move> valuemove = alpha_beta->alphaBeta(8, -581357, 581357, selfPlayer, selfPlayer);

    Move move = valuemove.second;

    state->doMove(move);

    // TODO, set based on debug flag.
    state->getBoard()->debugPrint();

    return move;
}

void AIPlayer::setOpponentMove(Move move)
{
    state->doMove(move);

    // TODO, set based on debug flag.
    state->getBoard()->debugPrint();
}
