cmake_minimum_required(VERSION 3.4)
project(CheckerAI)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    AIPlayer.cpp
    AIPlayer.h
    Board.cpp
    Board.h
    BusConnector.cpp
    BusConnector.h
    GameState.cpp
    GameState.h
    HostConnector.cpp
    HostConnector.h
    main.cpp
    Makefile
    Move.cpp
    Move.h
    movemessage.pb.cpp
    movemessage.pb.h
    movemessage.proto
    Player.cpp
    Player.h
    README.md)

add_executable(CheckerAI ${SOURCE_FILES})