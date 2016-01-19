CC=g++
CFLAGS=-Wall -g -I /usr/include/boost -std=c++11 -c
LDFLAGS=
LIBRARIES=-lboost_program_options -lzmq
SOURCES=main.cpp Board.cpp Move.cpp Player.cpp AIBoard.cpp AIPlayer.cpp HostConnector.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=chess

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) $(LIBRARIES) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(EXECUTABLE) $(OBJECTS)
