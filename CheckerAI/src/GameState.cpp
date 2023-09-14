#include "GameState.h"

#include <algorithm>
#include <utility>

template <typename T>
bool GameState::vectorContains(std::vector<T> v, T x)
{
    return (find(v.begin(), v.end(), x) != v.end());
}

bool GameState::isValidRow(int row) {
    return (row >= 0 && row < 10);
}

bool GameState::isValidColumn(int column) {
    return (column >= 0 && column < 10);
}

std::vector<Move> GameState::appendMoves(std::vector<Move> first, const std::vector<Move>& second)
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
    int row = board->getRow(position);
    int col = board->getCol(position);

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
    //bool isBlack   = vectorContains(player->getPieces(), pieceType::black);

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
        if (!isValidRow(row) || !isValidColumn(col)) {
            break;
        }
        pieceType type = board->getPiece(row, col);
        if(type != pieceType::empty) {
            break;
        }
        moves.push_back(board->createMove(row, col, r, c));
    }
}

std::vector<Move> GameState::getForcedMovesAtPosition(int row, int col, Player* player)
{
    std::vector<Move> moves;
    Move move;

    std::vector<pieceType> opponentPieces = player->getOpponent()->getPieces();

    pieceType piece = board->getPiece(row, col);

    bool isCrowned = (piece == pieceType::white_crown) || (piece == pieceType::black_crown);

    getForcedMovesInDirection(row, col, true, true, player, isCrowned, opponentPieces, moves);
    getForcedMovesInDirection(row, col, false, true, player, isCrowned, opponentPieces, moves);
    getForcedMovesInDirection(row, col, true, false, player, isCrowned, opponentPieces, moves);
    getForcedMovesInDirection(row, col, false, false, player, isCrowned, opponentPieces, moves);

    return moves;
}

void GameState::getForcedMovesInDirection(
        int row,
        int col,
        bool up,
        bool right,
        Player* player,
        bool isCrowned,
        std::vector<pieceType> opponentPieces,
        std::vector<Move>& moves)
{
    int row_delta = up ? 1 : -1;
    int col_delta =  right ? 1 : -1;

    int steps_until_opponent = 1;
    while (true) {
        int row_pre = row + row_delta * steps_until_opponent; 
        int col_pre = col + col_delta * steps_until_opponent; 
        if (!isValidRow(row_pre) || !isValidColumn(col_pre)) {
            break;
        }
        pieceType piece = board->getPiece(row_pre, col_pre);
        if (vectorContains(opponentPieces, piece)) {
            int steps_after_opponent = 1;
            // Check if the next position is empty (or multiple for crowned pieces)
            while (true) {
                int row_post = row_pre + row_delta * steps_after_opponent; 
                int col_post = col_pre + col_delta * steps_after_opponent; 
                if (!isValidRow(row_post) || !isValidColumn(col_post)) {
                    break;
                }
                if (board->getPiece(row_post, col_post) == pieceType::empty) {
                    moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row_post, col_post, row, col), player));
                } else {
                    break;
                }
                if (isCrowned) {
                    steps_after_opponent++;
                } else {
                    break;
                }
            }
            break;
        }
        if (isCrowned && piece == pieceType::empty) {
            steps_until_opponent++;
        } else {
            break;
        }
    }
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

void GameState::doMove(const Move& move)
{
    board->doMove(move);
}

void GameState::undoMove(const Move& move)
{
    board->undoMove(move);
}

std::vector<Move> GameState::getMoves(Player* player)
{
    std::vector<Move> moves = getForcedMoves(player);

    if (!moves.empty()) {
        return moves;
    }

    return getUnforcedMoves(player);
}

Board* GameState::getBoard() const {
    return board;
}



