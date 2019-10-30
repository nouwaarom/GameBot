# Gamebot
The goal of this project is to create a general game playing agent.
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
  ```
    sudo apt install libprotobuf-dev python-protobuf protobuf-compiler 
  ```
* install boost program options
  ```
    sudo apt install libboost-program-options-dev
  ```
* install flite-dev and pyflite

* execute make in Host, CheckerAI and BoardRecognizer directories

now Host/host is the program you want to execute
note that the host spawns other processes and
that they may not be killed correctly in case of an exception.

### Other platforms
* I havent tested on any other platfrom

## TODO
* finish board recognizer
* implement arm controller
* create general game playing AI
* write documentation
* make tests
* Create a design for the robot arm
* move to python3?

## Documentation
For short summaries of each project read the README's in the directories
Real documentation will come... someday...

## Contributing
Just create an issue or pull request. All help is welcome

## Authors
* Elbert van de Put   -   elbert@t-matix.nl
* Daan de Graaf - daandegraaf9@gmail.com
