
include(FetchContent)

FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.11.0
)
FetchContent_MakeAvailable(googletest)
add_library(GTest::GTest INTERFACE IMPORTED)
target_link_libraries(GTest::GTest INTERFACE gtest_main)

set(TEST_SOURCES
    Board_test.cpp
    GameState_test.cpp)


add_executable(core_test ${TEST_SOURCES})

target_link_libraries(core_test
    PRIVATE
    CheckerAICore
    GTest::GTest)

add_test(unit_tests core_test)
