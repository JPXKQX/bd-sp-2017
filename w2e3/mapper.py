#!/usr/bin/env python
import sys
import os

fname = os.environ['map_input_file']
airport = 'W' if 'wickairport' in fname else 'H'

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    year, month, tmax, tmin, rain = line.split()
    try:
        month = int(month)
    except:
        continue
    print '%s%02d\t%s\t%s\t%s\t%s' % (year, month, airport, tmax, tmin, rain)
