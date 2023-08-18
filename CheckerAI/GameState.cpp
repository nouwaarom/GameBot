#include "GameState.h"

#include <algorithm>
#include <utility>

template <typename T>
bool GameState::vectorContains(std::vector<T> v, T x)
{
    return (find(v.begin(), v.end(), x) != v.end());
}

std::vector<Move> GameState::appendMoves(std::vector<Move> first, std::vector<Move> second)
{
    first.insert(first.end(), second.begin(), second.end());

    return first;
}

GameState::GameState(Board* startBoard)
{
    board = startBoard;
}

std::vector<Move> GameState::mergeMoves(Move first, std::vector<Move> second)
{
    std::vector<Move> moves;

    std::vector<int> firstRemovedPositions;
    for (Piece piece : first.getRemovedPieces()) {
        firstRemovedPositions.push_back(piece.position);
    }

    if (!second.empty()) {
        std::vector<Move>::iterator moveIt;
        for (moveIt = second.begin(); moveIt < second.end(); moveIt++)
        {
            //Don't merge moves if they cancel eachother
            if (!vectorContains(firstRemovedPositions, moveIt->getNewPiece().position))
            {
                Move move;
                move.setNewPiece(moveIt->getNewPiece());
                move.setRemovedPieces(first.getRemovedPieces());

                std::vector<Piece> removed = moveIt->getRemovedPieces();

                std::vector<Piece>::iterator removedIt;
                for (removedIt = removed.begin(); removedIt < removed.end(); removedIt++)
                {
                    if (removedIt->position != first.getNewPiece().position)
                    {
                        move.addRemovedPiece(*removedIt);
                    }
                }

                moves.push_back(move);
            }
        }
    }
    else {
        moves.push_back(first);
    }

    return moves;
}

std::vector<Move> GameState::getSuccessiveForcedMoves(Move move, Player* player)
{
    std::vector<Move> moves;

    int position = move.getNewPiece().position;
    int row = position / 5;
    int col = 2*(position % 5) + (row % 2);

    board->doMove(move);
    moves = getForcedMovesAtPosition(row, col, player);

    moves = mergeMoves(move, moves);
    board->undoMove(move);

    return moves;
}

std::vector<Move> GameState::getMovesAtPosition(int row, int col, Player* player)
{
    std::vector<Move> moves;

    pieceType piece = board->getPiece(row,col);

    bool isCrowned = (piece == pieceType::white_crown) || (piece == pieceType::black_crown);
    bool isWhite   = vectorContains(player->getPieces(), pieceType::white);
    bool isBlack   = vectorContains(player->getPieces(), pieceType::black);

    getMovesInDirection(row, col, isWhite, true, !isCrowned, player, moves);
    getMovesInDirection(row, col, isWhite, false, !isCrowned, player, moves);

    return moves;
}

void GameState::getMovesInDirection(int r, int c, bool up, bool right, bool oneStep, Player* player, std::vector<Move> &moves){
    int row = r;
    int col = c;

    while(!oneStep || row == r){
        if(up)  row++;
        else    row--;

        if(right) col++;
        else      col--;
        pieceType type = board->getPiece(row, col);
        if(type != pieceType::empty) break;
        moves.push_back(board->createMove(row, col, r, c));
    }
}

std::vector<Move> GameState::getForcedMovesAtPosition(int row, int col, Player* player)
{
    std::vector<Move> moves;
    Move move;

    std::vector<pieceType> opponentPieces = player->getOpponent()->getPieces();

    pieceType piece = board->getPiece(row,col);

    bool isCrowned = (piece == pieceType::white_crown) || (piece == pieceType::black_crown);

    int i, j;
    //check left down
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row-i,col-i) == pieceType::empty)); i++)
    {
        if (vectorContains(opponentPieces, board->getPiece(row-i-1,col-i-1)))
        {
            for (j=2; (board->getPiece(row-i-j, col-i-j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row-i-2,col-i-2, row, col), player));
            }
        }
    }

    //check right down
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row-i,col+i) == pieceType::empty)); i++)
    {
        if (vectorContains(opponentPieces, board->getPiece(row-i-1,col+i+1)))
        {
            for (j=2; (board->getPiece(row-i-j, col+i+j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row-i-2,col+i+2, row, col), player));
            }
        }
    }

    //check left up
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row+i,col-i) == pieceType::empty)); i++)
    {
        if (vectorContains(opponentPieces, board->getPiece(row+i+1,col-i-1)))
        {
            for (j=2; (board->getPiece(row+i+j, col-i-j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row+i+2,col-i-2, row, col), player));
            }
        }
    }

    //check right
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row+i,col+i) == pieceType::empty)); i++)
    {
        if (vectorContains(opponentPieces, board->getPiece(row+i+1,col+i+1)))
        {
            for (j=2; (board->getPiece(row+i+j, col+i+j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row+i+2,col+i+2, row, col), player));
            }
        }
    }

    return moves;
}

std::vector<Move> GameState::getUnforcedMoves(Player* player)
{
    std::vector<Move> moves;
    std::vector<Move> movesAtPosition;

    std::vector<pieceType> playerPieces = player->getPieces();

    for (auto tile = board->getBegin(); tile < board->getEnd(); tile++)
    {
        int key = std::distance(board->getBegin(), tile);

        int row = board->getRow(key);
        int col = board->getCol(key);

        if (vectorContains(playerPieces, *tile))
        {
            movesAtPosition = getMovesAtPosition(row, col, player);
            moves.insert(moves.end(), movesAtPosition.begin(), movesAtPosition.end());
        }
    }

    return moves;
}

std::vector<Move> GameState::getForcedMoves(Player* player)
{
    std::vector<Move> moves;
    std::vector<Move> movesAtPosition;

    std::vector<pieceType> playerPieces = player->getPieces();

    for (auto tile = board->getBegin(); tile < board->getEnd(); tile++)
    {
        int key = std::distance(board->getBegin(), tile);

        int row = board->getRow(key);
        int col = board->getCol(key);

        if (vectorContains(playerPieces, *tile))
        {
            movesAtPosition = getForcedMovesAtPosition(row, col, player);
            moves.insert(moves.end(), movesAtPosition.begin(), movesAtPosition.end());
        }
    }

    return moves;
}

void GameState::doMove(Move move)
{
    board->doMove(std::move(move));
}

std::vector<Move> GameState::getMoves(Player* player)
{
    std::vector<Move> moves = getForcedMoves(player);

    if (!moves.empty()) {
        return moves;
    }

    return getUnforcedMoves(player);
}

int GameState::getScore(Player* maximizingPlayer)
{
    int score = 0;

    int position;
    for (position=0; position<50; position++)
    {
        int row = board->getRow(position);
        int col = board->getCol(position);

        int pieceScore = 0;
        pieceType piece = board->getPiece(position);

        // Piece Count
        if (vectorContains(maximizingPlayer->getPieces(), piece)) {
            pieceScore = 10;
        }
        if (vectorContains(maximizingPlayer->getOpponentPieces(), piece)) {
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

std::pair<int, Move> GameState::alphaBeta(int depth, int alpha, int beta, Player* player, Player* maximizingPlayer)
{
    int bestValue;
    Move bestMove;

    std::vector<Move> moves = getMoves(player);

    if (depth == 0 || moves.size() == 0)
    {
        return std::make_pair(getScore(maximizingPlayer), Move());
    }

    if (player == maximizingPlayer)
    {
        bestValue = -581357;

        for (Move move : moves)
        {
            board->doMove(move);

            std::pair <int, Move> pair = alphaBeta(depth - 1, alpha, beta, player->getOpponent(), maximizingPlayer);

            if (pair.first > bestValue) {
                bestValue = pair.first;
                bestMove = move;

                if (bestValue > alpha) {
                    alpha = bestValue;
                }
            }

            board->undoMove(move);

            if (beta <= alpha) {
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
            board->doMove(move);

            std::pair <int, Move> pair = alphaBeta(depth - 1, alpha, beta, player->getOpponent(), maximizingPlayer);

            if (pair.first < bestValue) {
                bestValue = pair.first;
                bestMove = move;

                if (bestValue < beta) {
                    beta = bestValue;
                }
            }

            board->undoMove(move);

            if (beta <= alpha) {
                break;
            }
        }
        return std::make_pair(bestValue, bestMove);
    }
}
