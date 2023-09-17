# Host Program
This program is the host of the game.
It starts the ComputerVision, AI and Arm controller
and has the role of arbitrator.

# Configuration program
This program allows the user to set parameters
to make the board recognizer and arm controller work. (WIP)

## Specifictation of communication between Host and AI
* Host initialzes AI with arguments:
    difficulty(0-99),
    start(1=AI/2=PLAYER),
    board(string boardRepresentation)
* Host and AI communicate using zeromq and protobuf

# Todo
* Improve and standardize logging

# Uses pyflite and flite for voice output (CURRENTLY DISABLED)

# Building protocol buffers
```
$ protoc --python_out=. movemessage.proto
$ pip2 install -U numpy
```

# Development
The idea is to work with behaviour driven development.

## Running tests
Install test requirements
```
$ sudo apt install python3-behave
```
Run the tests
```
$ behave
```

