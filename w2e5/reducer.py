#!/usr/bin/env python
import sys

# input comes from STDIN
counterA = 0
counterB = 0
for line in sys.stdin:
    line = line.strip()
    a, b = line.split()
    try:
        a = float(a)
        b = float(b)
    except:
        continue

    counterA += a
    counterB += b

print "%f" % (counterB / counterA)