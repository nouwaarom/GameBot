.PHONY: all clean

all: move_message

clean:
	rm -f *.pyc
	rm -f movemessage_pb2.py

move_message:
	protoc --python_out=. movemessage.proto
