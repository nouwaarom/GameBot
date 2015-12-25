#include <iostream>

#include "Board.h"
#include "Validator.h"
#include "AIPlayer.h"
#include "HumanPlayer.h"
#include "GUI.h"

//the main function manages the game
int main(int argc, char **argv)
{
	std::cout << "Welcome to the chess program";

	//create a board
	Board board;

	//create a validator
	Validator validator;

	//create two players
	AIPlayer ai;
	HumanPlayer human;

	//decide which player is first
	std::cout << "Who do you want to go first?";

	//now let the players make their move
		//validate the move

}