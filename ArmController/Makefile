.PHONY: all clean

all: controller

clean:
	rm -f controller
	rm -f protoc_middleman boardmessage_pb2.py
	rm -f *.pyc

protoc_middleman: boardmessage.proto
	protoc --python_out=. boardmessage.proto
	@touch protoc_middleman

controller: main.py protoc_middleman
	@echo "Writing shortcut script controller..."
	@echo '#! /bin/sh' > controller
	@echo './main.py "$$@"' >> controller
	@chmod +x controller
