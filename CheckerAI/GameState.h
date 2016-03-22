#ifndef AIBOARD_H
#define AIBOARD_H

#include <utility>
#include <string>
#include <vector>

#include "Board.h"
#include "Player.h"

class GameState
{
    private:
        Board* board;

        std::vector<Move> mergeMoves(Move first, std::vector<Move> second);
        std::vector<Move> appendMoves(std::vector<Move> first, std::vector<Move> second);

        std::vector<Move> getMovesAtPosition(int row, int col, Player* player);
        std::vector<Move> getForcedMovesAtPosition(int row, int col, Player* player);
        std::vector<Move> getSuccessiveForcedMoves(Move move, Player* player);

        void getMovesInDirection(int r, int c, bool up, bool right, bool oneStep, Player* player, std::vector<Move> &moves);

        template <typename T>
        bool vectorContains(std::vector<T> v, T x);

    protected:
        int getScore(Player* maximizingPlayer);

    public:
        GameState(Board* startBoard);

        std::vector<Move> getForcedMoves(Player* player);
        std::vector<Move> getUnforcedMoves(Player* player);

        std::vector<Move> getMoves(Player* player);

        void doMove(Move move);

        std::pair<int, Move> alphaBeta(int depth, int alpha, int beta, Player* player, Player* maximizingPlayer);
};

#endif
