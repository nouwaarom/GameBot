#ifndef VALIDATOR_H
#define VALIDATOR_H

/*
 * Class that validates a move according to the chess rules
*/
class Validator
{
private:
    int getForcedMoves(int player, char board[10][10]);
protected:
public:
	Validator();
	int validateMove(char piece, int x, int y);
};

#endif
