#include "AlphaBeta.h"


AlphaBeta::AlphaBeta(GameState* game_state)
{
    m_game_state = game_state;
}


void AlphaBeta::reset_statistics()
{
    m_statistics.number_of_prunes = 0;
    m_statistics.number_of_evaluations = 0;
}

const AlphaBetaStats& AlphaBeta::get_statistics() 
{
    return m_statistics;
}

std::pair<int, Move> AlphaBeta::alphaBeta(int depth, int alpha, int beta, Player* player, Player* maximizingPlayer)
{
    int bestValue;
    Move bestMove;

    std::vector<Move> moves = m_game_state->getMoves(player);

    if (depth == 0 || moves.size() == 0)
    {
        return std::make_pair(getScore(maximizingPlayer), Move());
    }

    if (player == maximizingPlayer)
    {
        bestValue = -581357;

        for (Move move : moves)
        {
            m_statistics.number_of_evaluations++;
            m_game_state->doMove(move);

            std::pair <int, Move> pair = alphaBeta(depth - 1, alpha, beta, player->getOpponent(), maximizingPlayer);

            if (pair.first > bestValue) {
                bestValue = pair.first;
                bestMove = move;

                if (bestValue > alpha) {
                    alpha = bestValue;
                }
            }

            m_game_state->undoMove(move);

            if (beta <= alpha) {
                m_statistics.number_of_prunes++;
                break;
            }
        }
        return std::make_pair(bestValue, bestMove);
    }

    else
    {
        bestValue = 581357;

        for (Move move : moves)
        {
            m_statistics.number_of_evaluations++;
            m_game_state->doMove(move);

            std::pair <int, Move> pair = alphaBeta(depth - 1, alpha, beta, player->getOpponent(), maximizingPlayer);

            if (pair.first < bestValue) {
                bestValue = pair.first;
                bestMove = move;

                if (bestValue < beta) {
                    beta = bestValue;
                }
            }

            m_game_state->undoMove(move);

            if (beta <= alpha) {
                m_statistics.number_of_prunes++;
                break;
            }
        }
        return std::make_pair(bestValue, bestMove);
    }
}


int AlphaBeta::getScore(Player* maximizingPlayer)
{
    int score = 0;
    Board* board = m_game_state->getBoard();

    // TODO, add minimum or maximum score for winning condition.
    int position;
    for (position=0; position<50; position++)
    {
        int row = board->getRow(position);
        int col = board->getCol(position);

        int pieceScore = 0;
        pieceType piece = board->getPiece(position);

        // Piece Count
        if (m_game_state->vectorContains(maximizingPlayer->getPieces(), piece)) {
            pieceScore = 10;
        }
        if (m_game_state->vectorContains(maximizingPlayer->getOpponentPieces(), piece)) {
            pieceScore = -10;
        }

        // King Count
        if ((piece == pieceType::white_crown) || (piece == pieceType::black_crown)) {
            pieceScore *= 3;
        }

        // Weigthing using Grid
        pieceScore *= std::max(abs(row-5), abs(col-5));

        score += pieceScore;
    }

    return score;
}
