#! /usr/bin/env python

# See README.txt for information and build instructions.

import movemessage_pb2
import sys

# Main procedure:  Reads the entire address book from a file,
#   adds one person based on user input, then writes it back out to the same
#   file.
if len(sys.argv) != 2:
  print "Usage:", sys.argv[0], "MOVE_FILE"
  sys.exit(-1)

move_message = movemessage_pb2.MoveMessage()

# Read the existing address book.
try:
  f = open(sys.argv[1], "rb")
  move_message.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[1] + ": File not found.  Creating a new file."

move_message.requesttype = movemessage_pb2.MoveMessage.SET_MOVE
move_message.move.name = raw_input("Please enter a move name: ")

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(move_message.SerializeToString())
f.close()
