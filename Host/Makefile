.PHONY: all clean

MESSAGES=movemessage.proto boardmessage.proto

all: $(MESSAGES) host

clean:
	rm -f host
	rm -f *.pyc

$(MESSAGES):
	protoc --python_out=. $@

host: main.py
	@echo "Writing shortcut script host..."
	@echo '#! /bin/sh' > host
	@echo './main.py "$$@"' >> host
	@chmod +x host
