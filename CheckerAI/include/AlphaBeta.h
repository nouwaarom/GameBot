#ifndef ALPHA_BETA_H
#define ALPHA_BETA_H

#include "Board.h"
#include "Player.h"
#include "GameState.h"


class AlphaBeta {
    public:
        AlphaBeta(GameState* game_state);
        std::pair<int, Move> alphaBeta(int depth, int alpha, int beta, Player* player, Player* maximizingPlayer);
    protected:
        int getScore(Player* maximizingPlayer);
    private:
        GameState* m_game_state;
};


#endif
