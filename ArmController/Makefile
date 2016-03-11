.PHONY: all clean

all: protoc_middleman

clean:
	rm -f protoc_middleman boardmessage_pb2.py
	rm -f *.pyc

protoc_middleman: boardmessage.proto
	protoc --python_out=. boardmessage.proto
	@touch protoc_middleman
