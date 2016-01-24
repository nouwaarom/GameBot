# See README.txt.

.PHONY: all cpp python clean

all: cpp python

cpp:    server_cpp
python: client_python

clean:
	rm -f server_cpp client_python
	rm -f protoc_middleman movemessage.pb.cc movemessage.pb.h addressbook_pb2.py
	rm -f *.pyc
	rmdir tutorial 2>/dev/null || true

protoc_middleman: movemessage.proto
	protoc --cpp_out=. --python_out=. movemessage.proto
	@touch protoc_middleman

server_cpp: server.cpp protoc_middleman
	pkg-config --cflags protobuf  # fails if protobuf is not installed
	c++ server.cpp movemessage.pb.cc -o server_cpp `pkg-config --cflags --libs protobuf`

client_python: client.py protoc_middleman
	@echo "Writing shortcut script client_python..."
	@echo '#! /bin/sh' > client_python
	@echo './client.py "$$@"' >> client_python
	@chmod +x client_python
