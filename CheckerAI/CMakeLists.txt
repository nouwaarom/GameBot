cmake_minimum_required(VERSION 3.4)
project(CheckerAI)

find_package(Protobuf REQUIRED)
find_package(Boost 1.74 REQUIRED COMPONENTS program_options)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17")

protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS movemessage.proto)

set(SOURCE_FILES
    src/AIPlayer.cpp
    src/Board.cpp
    src/BusConnector.cpp
    src/GameState.cpp
    src/HostConnector.cpp
    src/main.cpp
    src/Move.cpp
    src/Player.cpp)

add_executable(CheckerAI ${SOURCE_FILES} ${PROTO_SRCS} ${PROTO_HDRS})

target_include_directories(CheckerAI PRIVATE include ${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(CheckerAI ${Protobuf_LIBRARIES} Boost::program_options zmq)
