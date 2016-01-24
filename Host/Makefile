.PHONY: all clean

all: host

clean:
	rm -f host
	rm -f protoc_middleman movemessage_pb2.py
	rm -f *.pyc

protoc_middleman: movemessage.proto
	protoc --python_out=. movemessage.proto
	@touch protoc_middleman

host: main.py protoc_middleman
	@echo "Writing shortcut script host..."
	@echo '#! /bin/sh' > host 
	@echo './main.py "$$@"' >> host 
	@chmod +x host 
