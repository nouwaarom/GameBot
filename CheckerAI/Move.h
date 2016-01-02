#ifndef MOVE_H
#define MOVE_H

class Move
{
private:
    int oldPosition;
    int newPosition;
protected:
public:
    Move();
    Move(int oldPos, int newPos);

    int getOldPosition();
    int getNewPosition();
};

#endif
