#!/usr/bin/python
import sys

def resolve(arg):
	resolved = ""
	for i, j in enumerate(arg):
		dec = ord(j) - i
		resolved += chr(dec)
	return resolved

if __name__ == '__main__':
	print resolve(sys.argv[1])

