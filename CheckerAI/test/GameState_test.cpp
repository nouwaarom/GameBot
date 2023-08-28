#include <gtest/gtest.h>

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

TEST(GameStateTests, TestGetMoves)
{
    const auto expected = 0;
    const auto actual = 1;
    ASSERT_EQ(actual, expected);
}

int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
