# Gamebot
The goal of this project is to create an artificial agent you can play games with.
Currently there is only a simple draughts AI available

## License
This software is licensed under GPLv3. See LICENSE

## Project Structure
 This project has 3 parts, information of these parts can be found in the directories.
 * An AI that plays draughts (Done)
    implemented in c++
 * A program that can recognize the board and pieces (Semi working, WIP)
    this program is implemented in python and uses openCV
 * A program that controls a manipulator (TODO)

 * And a Host program that starts all other programs
    Manages the communication between the other programs
    And has the role of an arbitrator

    Communication between programs works using zeroMq and google protobuf


## Used libraries
* PyFlite  - https://github.com/tflowers/pyflite
* Protobuf - https://github.com/google/protobuf
* ZeroMq   - http://zeromq.org/
* Boost    - http://www.boost.org/
* PySerial - https://pythonhosted.org/pyserial/


## Setup and Installation
### Linux
* install libzmq3-dev and python-zmq
* install protobuf
* install boost program options
* install flite-dev and pyflite

* execute make in Host, CheckerAI and BoardRecognizer directories

now Host/host is the program you want to execute

### Other platforms
* I havent tested on any other platfrom

## TODO
* finish board recognizer
* implement arm controller
* create chess AI
* write documentation
* make tests
* Create a design for the robot arm

## Documentation
For short summaries of each project read the README's in the directories
Real documentation will come... someday...

## Contributing
Just create an issue or pull request. All help is welcome

## Authors
Elbert van de Put   -   elbert@t-matix.nl
