#include <gtest/gtest.h>
#include "GameState.h"

class GameStateTest: public ::testing::Test {
protected:
    GameStateTest() {
    }
    ~GameStateTest() override {
    }

    void SetUp() override {
    }

    void TearDown() override {
    }
};

TEST(GameStateTests, TestGetBoard)
{
    Board* startBoard = new Board("xxxx");
    GameState gameState(startBoard);

    ASSERT_EQ(startBoard, gameState.getBoard());
}

TEST(GameStateTests, TestGetBoard2)
{
    Board* startBoard = new Board("xxxx");
    GameState gameState(startBoard);

    ASSERT_NE(startBoard, gameState.getBoard());
}

