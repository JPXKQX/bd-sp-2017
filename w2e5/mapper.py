#!/usr/bin/env python
import sys


counter_A = 0.0
counter_B = 0.0
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    line_sep = line.split()
    if len(line_sep) == 8:
        year, month, htmax, htmin, hrain, wtmax, wtmin, wrain = line_sep
    else:
        continue

    try:
        htmax = float(htmax)
        wtmax = float(wtmax)
    except:
        # Case with no data for one airport, Heathrow (1947-) and Wick (1910-)
        continue

    counter_A += wtmax ** 2
    counter_B += wtmax * htmax

print "%f\t%f" % (counter_A, counter_B)
