.PHONY: all clean

CC=g++
CFLAGS=-Wall -g -I /usr/include/boost -pthread -std=c++11 -c
LDFLAGS=
LIBRARIES=-lboost_program_options -lzmq -lpthread -lprotobuf
SOURCES=main.cpp Board.cpp Move.cpp Player.cpp AIBoard.cpp AIPlayer.cpp HostConnector.cpp movemessage.pb.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=chess

all: protoc_middleman $(SOURCES) $(EXECUTABLE)

# FIXME this is probaply not the nicest way to do stuff
protoc_middleman: movemessage.proto
	protoc --cpp_out=. movemessage.proto
	mv movemessage.pb.cc movemessage.pb.cpp
	@touch protoc_middleman

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) $(LIBRARIES) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(EXECUTABLE) $(OBJECTS)
	rm -f protoc_middleman movemessage.pb.h
