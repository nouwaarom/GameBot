# Host Program
This program is the host of the game
It starts the ComputerVision, AI and Arm controller
It also has the role of arbitrator

## Specifictation of communication between Host and AI
* Host initialzes AI with a difficulty(0-99), start(1=AI/2=PLAYER), board(string boardRepresentation)
* Host and AI communicate using zeromq and protobuf

Loop:
    * Host sends PlayerMove
    * AI sends AIMove
        if AIMove is invalid AI is terminated

* When the game ends the Host terminates the AI


# Uses pyflite and flite for voice output
