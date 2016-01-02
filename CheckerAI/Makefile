CC=g++
CFLAGS=-Wall -g -I /usr/include/boost -c
LDFLAGS=-L /usr/lib/boost/lib
LIBRARIES=-lboost_program_options
SOURCES=main.cpp Board.cpp Move.cpp Validator.cpp Player.cpp AIPlayer.cpp HumanPlayer.cpp
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=chess

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) $(LIBRARIES) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(EXECUTABLE) $(OBJECTS)
