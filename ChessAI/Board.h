#ifndef BOARD_H
#define BOARD_H

#include "Validator.h"

//create an enum for all the chess pieces


/*
 A general class that handles the data for the board
 init: creates a board with standard setup
 or a saved setup: if specified
*/
class Board
{
private:
	char board[8][8];
protected:
	int movePieceBoard(int oldx, int oldy, int newx, int newy);
	char getPieceAtLocation(int x, int y);
	int *getPieceLocation(char piece);

	//for AI algorithms 
	int *getBoard(void);
public:
	Board();
};

#endif