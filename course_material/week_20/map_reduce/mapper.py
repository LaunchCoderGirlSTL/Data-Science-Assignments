#!/usr/bin/env python
import sys

#stdin = standard input
for line in sys.stdin:

    #strip white spaces at begining and end of line
    line = line.strip()

    #split each line up
    words = line.split()

    #process each word and assign a value of 1 to each word
    for word in words:
        print(word + "\t1")

#mapper - breaking up words into units

#echo 'a quick brown fox jumps over a lazy dog'|./mapper.py