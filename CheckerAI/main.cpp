#include <vector>
#include <string>
#include <iostream>
#include <zmq.hpp>
#include <boost/program_options.hpp>

#include "Board.h"
#include "Move.h"
#include "AIPlayer.h"
#include "HostConnector.h"

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
        ("start", po::value<int>(), "player to start: AI(0), Player(1)")
        ("difficulty", po::value<int>(), "difficultiy of the AI (0-99)")
        ("board", po::value< string >(), "board representation");

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, desc), vm);
    po::notify(vm);

    cout << "Hello, I am you opponent" << endl;

    if (vm.count("help")) {
        cout << desc << endl;
        return 1;
    }

    if (!vm.count("start")) {
        cout << "The game ended because nobody started." << endl;
        return 1;
    }

    if (!vm.count("difficulty")) {
        cout << "I forgot how to play, sorry." << endl;
        return 1;
    }

    if (!vm.count("board")) {
        cout << "Without a board I cant play" << endl;
        return 1;
    }

	//create a board
	Board* board = new Board(vm["board"].as< string >());

	HostConnector* connector = new HostConnector();

    std::cout << "Please work now" << endl;

	AIPlayer* ai;
    if (vm["start"].as<int>() == 0) {
        cout << "I start" << std::endl;
        ai = new AIPlayer(board, {'w','W'}, {'b','B'});
    }
    else {
        cout << "You can start" << "\n";
        ai = new AIPlayer(board, {'b','B'}, {'w','W'});
    }

    connector->setAI(ai);

	//let the players make their moves
    while (true)
    {
        connector->getRequest();
    }

    cout << "Goodbye" << "\n";

    return 1;

}
