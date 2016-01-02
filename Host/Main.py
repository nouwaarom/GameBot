#!/usr/bin/env python

import sys
import cv2
import random
import subprocess

AI_PROGRAM_PATH = "../CheckerAI/chess"

def main():
    print "Welcome, I am Hansel, I am the host for this game"

    #print "Do you want to start? (yes/no) "
    #userStarts = sys.stdin.readline()
    userStarts = raw_input("Do you want to start?\n")

    if (userStarts == 'yes'):
        userStarts = 1
    elif (userStarts == 'no'):
        userStarts = 2
    else:
        print "Sorry, I dont understand you"
        return -1;

    difficulty = random.randint(0,99)


    print "Starting Board Recognizer ..."
    # TODO start recognition program

    print "Starting Arm Controller ..."
    # TODO start arm control program

    print "Setting up board .."
    #Setup board
    board = ["x"] * 50
    for i in range(20):
        board[i] = 'w'
        board[i+30] = 'b'

    # TODO check if pieces are on the right tiles and move them if neccessary

    print "Starting AI ..."
    ai_command = [AI_PROGRAM_PATH, "--start", str(userStarts), "--difficulty", str(difficulty), "--board", "".join(board)]

    ai = subprocess.Popen(ai_command,
                          shell  = False,
                          stdin  = subprocess.PIPE,
                          stdout = subprocess.PIPE,
                          stderr = subprocess.PIPE,
                          )

    ai_output, ai_error = ai.communicate()

    print ai_output
    print ai_error


if __name__ == "__main__":
    main()
