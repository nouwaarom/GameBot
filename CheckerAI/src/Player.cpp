#include "Player.h"

Player::Player(std::vector<pieceType> pieces, std::vector<pieceType> opponentPieces)
{
    _pieces = pieces;
    _opponentPieces = opponentPieces;
}

void Player::setOpponent(Player* opponent)
{
    _opponent = opponent;
}

std::vector<pieceType> Player::getPieces()
{
    return _pieces;
}

std::vector<pieceType> Player::getOpponentPieces()
{
    return _opponentPieces;
}

Player* Player::getOpponent()
{
    return _opponent;
}
