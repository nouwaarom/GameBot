#include <gtest/gtest.h>
#include "Board.h"

class BoardTest: public ::testing::Test {

    void SetUp() override {
    }

    void TearDown() override {
    }
};


TEST(BoardTest, testCreateMove)
{
    Board* board = new Board("wwwwwwwwwwwwwwwwwwwwxxxxxxxxxxbbbbbbbbbbbbbbbbbbbb");
}
