# Host Program
This program is the host of the game
It starts the ComputerVision, AI and Arm controller
It also has the role of arbitrator

## Specifictation of comunication between Host and AI
* Host initialzes AI with a difficulty(0-99), start(1=AI/2=PLAYER), board(string boardRepresentation)

Loop:
    * Host sends PlayerMove (oldLocation to newLocation)
    * AI sends AIMove (oldLocation to newLocation)
        if AIMove is invalid AI is terminated

* When the game ends the Host terminates the AI
