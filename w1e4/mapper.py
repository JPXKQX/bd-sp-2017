#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

	# Students to output <lineLength, 1>
	lineLength = len(line.split())
	print '%s\t%s' % (lineLength, 1)
