#include "GameState.h"

#include <algorithm>

template<typename T>
bool GameState::vectorContains(std::vector<T> v, T x)
{
    if (find(v.begin(), v.end(), x) != v.end())
        return true;
    else
        return false;
}

GameState::GameState(Board* startBoard, std::vector<pieceType> _friendPieces, std::vector<pieceType> _enemyPieces)
{
    board = startBoard;

    friendPieces = _friendPieces;
    enemyPieces  = _enemyPieces;
}

std::vector<Move> GameState::getForcedMoves()
{
    std::vector<Move> moves;

    std::vector<pieceType>::iterator tile;
    for (tile = board->getBegin(); tile < board->getEnd(); tile++)
    {
        int key = std::distance(board->getBegin(), tile);
        int row = key / 5;
        int col = 2*(key % 5) + (row % 2);

        if (vectorContains(friendPieces, *tile))
        {
            //check down
            if (row > 1) {
               //check left
               if (col > 1) {
                   if (vectorContains(enemyPieces, board->getPiece(row-1,col-1))) {
                       if (board->getPiece(row-2, col-2) == pieceType::empty) {
                           moves.push_back(board->createMove(row-2,col-2, row, col));
                       }
                   }
               }

               //check right
               if (col < 8) {
                   if (vectorContains(enemyPieces, board->getPiece(row-1,col+1))) {
                       if (board->getPiece(row-2,col+2) == pieceType::empty) {
                           moves.push_back(board->createMove(row-2,col+2, row, col));
                       }
                   }
               }
            }

            //check up
            if (row < 8) {
                //check left
                if (col > 1) {
                    if (vectorContains(enemyPieces, board->getPiece(row+1,col-1))) {
                        if (board->getPiece(row+2,col-2) == pieceType::empty) {
                            moves.push_back(board->createMove(row+2,col-2, row, col));
                        }
                    }
                }

                //check right
                if (col < 8) {
                    if (vectorContains(enemyPieces, board->getPiece(row+1,col+1))) {
                        if (board->getPiece(row+2,col+2) == pieceType::empty) {
                           moves.push_back(board->createMove(row+2,col+2, row, col));
                        }
                    }
                }
            }
        }
    }

    return moves;
}

std::vector<Move> GameState::getMoves()
{
    std::vector<Move> moves;

    bool isWhite = vectorContains(friendPieces, pieceType::white);

    std::vector<pieceType>::iterator tile;
    for (tile = board->getBegin(); tile < board->getEnd(); tile++)
    {

        if (vectorContains(friendPieces, *tile))
        {
            int key = std::distance(board->getBegin(), tile);
            int row = key / 5;
            int col = 2*(key % 5) + (row % 2);

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
        }
    }
    return moves;
}

void GameState::doMove(Move* move)
{
    Piece newPiece = move->getNewPiece();
    std::vector<Piece> removedPieces = move->getRemovedPieces();

    board->setPiece(newPiece.position, newPiece.type);

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++) {
        board->setPiece(removedPieces[i].position, pieceType::empty);
    }

    return;
}

void undoMove(Move move)
{

}

int getScore()
{
    return 5;
}
