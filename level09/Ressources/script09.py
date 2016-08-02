#!/usr/bin/python
import re, sys

replchars = re.compile(r'[\n\r]')
def replchars_to_hex(match):
	    return r'\x{0:02x}'.format(ord(match.group()))

str = replchars.sub(replchars_to_hex, sys.argv[1])
print str

