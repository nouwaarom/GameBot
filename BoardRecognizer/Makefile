.PHONY: all clean

all: recognizer

clean:
	rm -f recognizer
	rm -f protoc_middleman boardmessage_pb2.py
	rm -f *.pyc

protoc_middleman: boardmessage.proto
	protoc --python_out=. boardmessage.proto
	@touch protoc_middleman

recognizer: main.py protoc_middleman
	@echo "Writing shortcut script host..."
	@echo '#! /bin/sh' > recognizer
	@echo './main.py "$$@"' >> recognizer
	@chmod +x recognizer
