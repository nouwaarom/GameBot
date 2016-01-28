#include "AIBoard.h"

#include <algorithm>

Move AIBoard::selectRandomly(std::vector<Move> v)
{
    static std::random_device rd;
    static std::mt19937 gen(rd());

    std::vector<Move>::iterator start = v.begin();
    std::vector<Move>::iterator end   = v.end();

    std::uniform_int_distribution<> dis(0, std::distance(start, end) - 1);
    std::advance(start, dis(gen));

    return *start;
}

inline int AIBoard::getIndex(int row, int col)
{
    return (5*row) + (col/2);
}

template<typename T>
bool AIBoard::vectorContains(std::vector<T> v, T x)
{
    if (find(v.begin(), v.end(), x) != v.end())
        return true;
    else
        return false;
}

AIBoard::AIBoard(std::string representation, std::vector<char> _friendPieces, std::vector<char> _enemyPieces) : Board(representation)
{
    friendPieces = _friendPieces;
    enemyPieces  = _enemyPieces;
}

std::vector<Move> AIBoard::getForcedMoves()
{
    std::vector<Move> moves;

    std::string::iterator tile;
    for (tile = board.begin(); tile < board.end(); tile++)
    {
        int key = std::distance(board.begin(), tile);
        int row = key / 5;
        int col = 2*(key % 5) + (row % 2);

        if (vectorContains(friendPieces, *tile))
        {
            //check down
            if (row > 1) {
               //check left
               if (col > 1) {
                   if (vectorContains(enemyPieces, board[getIndex(row-1,col-1)])) {
                       if (board[getIndex(row-2, col-2)] == 'x') {
                           moves.push_back(Move(getIndex(row-2,col-2), key, board));
                       }
                   }
               }

               //check right
               if (col < 8) {
                   if (vectorContains(enemyPieces, board[getIndex(row-1,col+1)])) {
                       if (board[getIndex(row-2,col+2)] == 'x') {
                           moves.push_back(Move(getIndex(row-2,col+2), key, board));
                       }
                   }
               }
            }

            //check up
            if (row < 8) {
                //check left
                if (col > 1) {
                    if (vectorContains(enemyPieces, board[getIndex(row+1,col-1)])) {
                        if (board[getIndex(row+2,col-2)] == 'x') {
                            moves.push_back(Move(getIndex(row+2,col-2), key, board));
                        }
                    }
                }

                //check right
                if (col < 8) {
                    if (vectorContains(enemyPieces, board[key+6])) {
                        if (board[key+11] == 'x') {
                           moves.push_back(Move(getIndex(row+2,col+2), key, board));
                        }
                    }
                }
            }
        }
    }

    return moves;
}

std::vector<Move> AIBoard::getMoves()
{
    std::vector<Move> moves;

    bool isWhite = vectorContains(friendPieces, 'w');

    std::string::iterator tile;
    for (tile = board.begin(); tile < board.end(); tile++)
    {

        if (vectorContains(friendPieces, *tile))
        {
            int key = std::distance(board.begin(), tile);
            int row = key / 5;
            int col = 2*(key % 5) + (row % 2);

            //check down if we are black
            if (!isWhite && row > 0) {
                //check left
                if ((col > 0) && board[getIndex(row-1, col-1)] == 'x')
                {
                    moves.push_back(Move(getIndex(row-1, col-1), key, board));
                }

                //check right
                if ((col < 9) && board[getIndex(row-1, col+1)] == 'x')
                {
                    moves.push_back(Move(getIndex(row-1, col+1), key, board));
                }
            }

            //check up if we are white
            if (isWhite && row < 9) {
                //check left
                if ((col > 0) && board[getIndex(row+1, col-1)] == 'x')
                {
                    moves.push_back(Move(getIndex(row+1, col-1), key, board));
                }

                //check right
                if ((col < 9) && board[getIndex(row+1, col+1)] == 'x')
                {
                    moves.push_back(Move(getIndex(row+1, col+1), key, board));
                }
            }
        }
    }
    return moves;
}

void AIBoard::doMove(Move* move)
{
    Piece newPiece = move->getNewPiece();
    std::vector<Piece> removedPieces = move->getRemovedPieces();

    board[newPiece.position] = newPiece.type;

    unsigned int i;
    for (i=0; i<removedPieces.size(); i++) {
        board[removedPieces[i].position] = 'x';
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
