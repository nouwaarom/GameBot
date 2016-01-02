#include "Move.h"

Move::Move()
{
    oldPosition = -1;
    newPosition = -1;
}

Move::Move(int oldPos, int newPos)
{
    oldPosition = oldPos;
    newPosition = newPos;
}

int Move::getOldPosition()
{
    return oldPosition;
}

int Move::getNewPosition()
{
    return newPosition;
}
