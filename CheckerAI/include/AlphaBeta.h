#ifndef ALPHA_BETA_H
#define ALPHA_BETA_H

#include "Board.h"
#include "Player.h"
#include "GameState.h"

struct AlphaBetaStats {
    int number_of_evaluations;
    int number_of_prunes;
};

class AlphaBeta {
public:
    AlphaBeta(GameState* game_state);

    //! \brief Reset internally kept algorithm performance statistics.
    void reset_statistics();

    //! \brief Get a reference to the internally kept algorithm performance statistics.
    const AlphaBetaStats& get_statistics(); 

    //! \brief Perform alpha beta pruning, return a move and the score of this
    std::pair<int, Move> alphaBeta(int depth, int alpha, int beta, Player* player, Player* maximizingPlayer);
protected:
    //! \brief Calculate a heuristic for the "quality" of the current board for the maximingPlayer
    int getScore(Player* maximizingPlayer);
private:
    GameState* m_game_state;
    //! \brief Keeps track of statistics for the current run.
    AlphaBetaStats m_statistics;
};


#endif
