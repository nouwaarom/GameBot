#ifndef AIBOARD_H
#define AIBOARD_H

#include <utility>
#include <string>
#include <vector>

#include "Board.h"
#include "Player.h"

class GameState
{
public:
    explicit GameState(Board* startBoard);

    std::vector<Move> getForcedMoves(Player* player);
    std::vector<Move> getUnforcedMoves(Player* player);

    std::vector<Move> getMoves(Player* player);

    void doMove(const Move& move);
    void undoMove(const Move& move);

    Board* getBoard() const;

    // TODO, move to utilities file.
    template <typename T>
    bool vectorContains(std::vector<T> v, T x);

private:

    std::vector<Move> mergeMoves(Move first, std::vector<Move> second);
    static std::vector<Move> appendMoves(std::vector<Move> first, std::vector<Move> second);

    std::vector<Move> getMovesAtPosition(int row, int col, Player* player);
    std::vector<Move> getForcedMovesAtPosition(int row, int col, Player* player);
    std::vector<Move> getSuccessiveForcedMoves(Move move, Player* player);

    void getMovesInDirection(int r, int c, bool up, bool right, bool oneStep, Player* player, std::vector<Move> &moves);

    Board* board;
};

#endif
