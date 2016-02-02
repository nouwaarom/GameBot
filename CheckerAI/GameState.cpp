#include "GameState.h"

#include <algorithm>
#include <iostream>

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

GameState::GameState(Board* startBoard, std::vector<pieceType> _friendPieces, std::vector<pieceType> _enemyPieces)
{
    board = startBoard;

    friendPieces = _friendPieces;
    enemyPieces  = _enemyPieces;
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
            //Dont merge moves if they cancel eachother
            if (false == vectorContains(firstRemovedPositions, moveIt->getNewPiece().position))
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

std::vector<Move> GameState::getMovesAtPosition(int position)
{
    std::vector<Move> moves;

    bool isWhite = vectorContains(friendPieces, pieceType::white);

    int row = position / 5;
    int col = 2*(position % 5) + (row % 2);

    //check down if we are black
    if (!isWhite && row > 0) {
        //check left
        if ((col > 0) && board->getPiece(row-1, col-1) == pieceType::empty)
        {
            moves.push_back(board->createMove(row-1, col-1, row, col));
        }

        //check right
        if ((col < 9) && board->getPiece(row-1, col+1) == pieceType::empty)
        {
            moves.push_back(board->createMove(row-1, col+1, row, col));
        }
    }

    //check up if we are white
    if (isWhite && row < 9) {
        //check left
        if ((col > 0) && board->getPiece(row+1, col-1) == pieceType::empty)
        {
            moves.push_back(board->createMove(row+1, col-1, row, col));
        }

        //check right
        if ((col < 9) && board->getPiece(row+1, col+1) == pieceType::empty)
        {
            moves.push_back(board->createMove(row+1, col+1, row, col));
        }
    }

    return moves;
}

std::vector<Move> GameState::getSuccessiveMoves(Move move)
{
    std::vector<Move> moves;

    board->doMove(move);
    moves = getForcedMovesAtPosition(move.getNewPiece().position);

    moves = mergeMoves(move, moves);
    board->undoMove(move);

    return moves;
}

std::vector<Move> GameState::getForcedMovesAtPosition(int position)
{
    std::vector<Move> moves;
    Move move;

    int row = position / 5;
    int col = 2*(position % 5) + (row % 2);

    //check down
    if (row > 1) {
        //check left
        if (col > 1) {
            if (vectorContains(enemyPieces, board->getPiece(row-1,col-1))) {
                if (board->getPiece(row-2, col-2) == pieceType::empty)
                {
                    moves = appendMoves(moves, getSuccessiveMoves(board->createMove(row-2,col-2, row, col)));
                }
            }
        }

        //check right
        if (col < 8) {
            if (vectorContains(enemyPieces, board->getPiece(row-1,col+1))) {
                if (board->getPiece(row-2,col+2) == pieceType::empty)
                {
                    moves = appendMoves(moves, getSuccessiveMoves(board->createMove(row-2,col+2, row, col)));
                }
            }
        }
    }

    //check up
    if (row < 8) {
        //check left
        if (col > 1) {
            if (vectorContains(enemyPieces, board->getPiece(row+1,col-1))) {
                if (board->getPiece(row+2,col-2) == pieceType::empty)
                {
                    moves = appendMoves(moves, getSuccessiveMoves(board->createMove(row+2,col-2, row, col)));
                }
            }
        }

        //check right
        if (col < 8) {
            if (vectorContains(enemyPieces, board->getPiece(row+1,col+1))) {
                if (board->getPiece(row+2,col+2) == pieceType::empty)
                {
                    moves = appendMoves(moves, getSuccessiveMoves(board->createMove(row+2,col+2, row, col)));
                }
            }
        }
    }

    return moves;
}

std::vector<Move> GameState::getMoves()
{
    std::vector<Move> moves;
    std::vector<Move> movesAtPosition;

    std::vector<pieceType>::iterator tile;
    for (tile = board->getBegin(); tile < board->getEnd(); tile++)
    {
        int key = std::distance(board->getBegin(), tile);

        if (vectorContains(friendPieces, *tile))
        {
            movesAtPosition = getMovesAtPosition(key);
            moves.insert(moves.end(), movesAtPosition.begin(), movesAtPosition.end());
        }
    }

    return moves;
}

std::vector<Move> GameState::getForcedMoves()
{
    std::vector<Move> moves;
    std::vector<Move> movesAtPosition;

    std::vector<pieceType>::iterator tile;
    for (tile = board->getBegin(); tile < board->getEnd(); tile++)
    {
        int key = std::distance(board->getBegin(), tile);

        if (vectorContains(friendPieces, *tile))
        {
            movesAtPosition = getForcedMovesAtPosition(key);
            moves.insert(moves.end(), movesAtPosition.begin(), movesAtPosition.end());
        }
    }

    return moves;
}

void GameState::doMove(Move move)
{
    board->doMove(move);
}

int getScore()
{
    return 5;
}
