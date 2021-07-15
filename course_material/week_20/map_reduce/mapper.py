#!/usr/bin/env python 
import sys

#stdin = standard input
for line in sys.stdin: 
    
    #strip white spaces at beginning and end of line
    line = line.strip()

    #split each line into words
    words = line.split()

    for word in words:
        print(word + "\t1")

