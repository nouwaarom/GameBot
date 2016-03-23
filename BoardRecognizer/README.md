# Board recognition program

The boardrecognizer program can recognize a board with green markings on the vertexes

The idea is that the recognizer can only see the difference between black and white pieces.
The host should keep track of the actual piece type

This program is still pretty buggy and error prone, ideas on how to improve this are welcome


## TODO
Create UI for changing mask

## Description of the function of classes
Recognizer gets frames and displays them.
Boardrecognizer takes frame and returns if the frame contains a board
    after that the board can bet fetched from the board recognizer
PieceRecognizer takes a frame and returns the pieces on the board