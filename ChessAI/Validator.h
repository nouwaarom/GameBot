#ifndef VALIDATOR_H
#define VALIDATOR_H

/*
	A class that validates a move according to the chess rules
*/
class Validator
{
private:
protected:
public:
	Validator();
	int validateMove(char piece, int x, int y);
};

#endif