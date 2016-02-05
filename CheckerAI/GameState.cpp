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

std::vector<Move> GameState::getSuccessiveForcedMoves(Move move)
{
    std::vector<Move> moves;

    int position = move.getNewPiece().position;
    int row = position / 5;
    int col = 2*(position % 5) + (row % 2);

    board->doMove(move);
    moves = getForcedMovesAtPosition(row, col);

    moves = mergeMoves(move, moves);
    board->undoMove(move);

    return moves;
}

//Todo merge with getMovesAtPosition
std::vector<Move> GameState::getMovesAtPosition(int row, int col)
{
    std::vector<Move> moves;

    pieceType piece = board->getPiece(row,col);

    bool isCrowned = (piece == pieceType::white_crown) || (piece == pieceType::black_crown);
    bool isWhite   = vectorContains(friendPieces, pieceType::white);
    bool isBlack   = vectorContains(friendPieces, pieceType::black);

    int i;
    //check left down
    for (i=1; (board->getPiece(row-i,col-i) == pieceType::empty) && (((i==1) && isBlack) || isCrowned); i++)
    {
        moves.push_back(board->createMove(row-i, col-i, row, col));
    }

    //check right down
    for (i=1; (board->getPiece(row-i,col+i) == pieceType::empty) && (((i==1) && isBlack) || isCrowned); i++)
    {
        moves.push_back(board->createMove(row-i, col+i, row, col));
    }

    //check left up
    for (i=1; (board->getPiece(row+i,col-i) == pieceType::empty) && (((i==1) && isWhite) || isCrowned); i++)
    {
        moves.push_back(board->createMove(row+i, col-i, row, col));
    }

    //check right
    for (i=1; (board->getPiece(row+i,col+i) == pieceType::empty) && (((i==1) && isWhite) || isCrowned); i++)
    {
        moves.push_back(board->createMove(row+i, col+i, row, col));
    }

    return moves;
}

std::vector<Move> GameState::getForcedMovesAtPosition(int row, int col)
{
    std::vector<Move> moves;
    Move move;

    pieceType piece = board->getPiece(row,col);

    bool isCrowned = (piece == pieceType::white_crown) || (piece == pieceType::black_crown);

    int i, j;
    //check left down
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row-i,col-i) == pieceType::empty)); i++)
    {
        if (vectorContains(enemyPieces, board->getPiece(row-i-1,col-i-1)))
        {
            for (j=2; (board->getPiece(row-i-j, col-i-j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row-i-2,col-i-2, row, col)));
            }
        }
    }

    //check right down
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row-i,col+i) == pieceType::empty)); i++)
    {
        if (vectorContains(enemyPieces, board->getPiece(row-i-1,col+i+1)))
        {
            for (j=2; (board->getPiece(row-i-j, col+i+j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row-i-2,col+i+2, row, col)));
            }
        }
    }

    //check left up
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row+i,col-i) == pieceType::empty)); i++)
    {
        if (vectorContains(enemyPieces, board->getPiece(row+i+1,col-i-1)))
        {
            for (j=2; (board->getPiece(row+i+j, col-i-j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row+i+2,col-i-2, row, col)));
            }
        }
    }

    //check right
    for (i=0; (i==0) || (isCrowned && (board->getPiece(row+i,col+i) == pieceType::empty)); i++)
    {
        if (vectorContains(enemyPieces, board->getPiece(row+i+1,col+i+1)))
        {
            for (j=2; (board->getPiece(row+i+j, col+i+j) == pieceType::empty) && ((j==2) || isCrowned); j++)
            {
                moves = appendMoves(moves, getSuccessiveForcedMoves(board->createMove(row+i+2,col+i+2, row, col)));
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

        int row = key / 5;
        int col = 2*(key % 5) + (row % 2);

        if (vectorContains(friendPieces, *tile))
        {
            movesAtPosition = getMovesAtPosition(row, col);
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

        int row = key / 5;
        int col = 2*(key % 5) + (row % 2);

        if (vectorContains(friendPieces, *tile))
        {
            movesAtPosition = getForcedMovesAtPosition(row, col);
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
