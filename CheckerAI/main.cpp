#include <vector>
#include <string>
#include <iostream>
#include <boost/program_options.hpp>

#include "Board.h"
#include "Move.h"
#include "AIPlayer.h"
#include "HumanPlayer.h"

using namespace std;

namespace po = boost::program_options;

/*
 * Input AI difficulty
 * Loop:
 *  Input Board State
 *  Output Move
 */
int main(int argc, char *argv[])
{
    po::options_description desc("Allowed options");
    desc.add_options()
        ("help", "get help message")
        ("start", po::value<int>(), "player to start: AI(1), Player(2)")
        ("difficulty", po::value<int>(), "difficultiy of the AI (0-99)")
        ("board", po::value< string >(), "board representation");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    std::cout << "Hello, I am you opponent" << "\n";

    if (vm.count("help")) {
        std::cout << desc << "\n";
        return 1;
    }

    if (vm.count("start")) {
        std::cout << "Someone starts" << "\n";
    }
    else {
        std::cout << "The game ended because nobody started." << "\n";
        return 1;
    }

    if (vm.count("difficulty")) {
        std::cout << "I will beat you" << "\n";
    }
    else {
        std::cout << "I forgot how to play, sorry." << "\n";
        return 1;
    }

    if (vm.count("board")) {
        cout << "I can see the board now" << "\n";
    }
    else {
        std::cout << "Without a board I cant play" << "\n";
        return 1;
    }

	//create a board
	Board* board = new Board(vm["board"].as< string >());

	//create two players
	AIPlayer* ai = new AIPlayer(board);
	HumanPlayer* human = new HumanPlayer();

    Player *whitePlayer, *blackPlayer;

    if (vm["start"].as<int>() == 1) {
        whitePlayer = ai;
        blackPlayer = human;
    }
    else {
        whitePlayer = human;
        blackPlayer = ai;
    }

	//let the players make their moves
    Move* move;
    while (true)
    {
        move = whitePlayer->getMove();
        board->doMove(move);
        if (board->isEnd())
            break;

        blackPlayer->setOpponentMove(move);
        move = blackPlayer->getMove();
        board->doMove(move);
        if (board->isEnd())
            break;

        whitePlayer->setOpponentMove(move);
    }

    std::cout << "Goodbye" << "\n";


    return 1;

}
