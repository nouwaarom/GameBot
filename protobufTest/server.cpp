#include <iostream>
#include <fstream>
#include <string>
#include "movemessage.pb.h"

using namespace std;

// Iterates though all people in the AddressBook and prints info about them.
void ProcessMessage(const aiconnector::MoveMessage& move_message)
{
    switch (move_message.requesttype())
    {
        case aiconnector::MoveMessage::GET_MOVE:
            cout << "  Get Move" << endl;
            break;
        case aiconnector::MoveMessage::SET_MOVE:
            {
            const aiconnector::MoveMessage::Move& move = move_message.move();

            cout << "  Set Move: " << move.name() << endl;
            }
            break;
        default:
            cout << "  Not a Request" << endl;
            break;
    }
}

// Main function:  Reads the entire address book from a file and prints all
//   the information inside.
int main(int argc, char* argv[])
{
  // Verify that the version of the library that we linked against is
  // compatible with the version of the headers we compiled against.
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  if (argc != 2) {
    cerr << "Usage:  " << argv[0] << " MOVE_MESSAGE_FILE" << endl;
    return -1;
  }

  aiconnector::MoveMessage move_message;

  {
    // Read the existing address book.
    fstream input(argv[1], ios::in | ios::binary);
    if (!move_message.ParseFromIstream(&input)) {
      cerr << "Failed to parse address book." << endl;
      return -1;
    }
  }

  ProcessMessage(move_message);

  // Optional:  Delete all global objects allocated by libprotobuf.
  google::protobuf::ShutdownProtobufLibrary();

  return 0;
}
