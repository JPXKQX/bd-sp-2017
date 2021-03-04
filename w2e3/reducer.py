#!/usr/bin/env python
import sys

current_date = ""
htmax, htmin, hrain, wtmax, wtmin, wrain = "", "", "", "", "", ""


for line in sys.stdin:
    line = line.strip()
    date, airport, tmax, tmin, rain = line.split()


    if date == current_date:
        if airport == 'W':
            wtmax, wtmin, wrain = tmax, tmin, rain
        else:
            htmax, htmin, hrain = tmax, tmin, rain

    else:       
        year = current_date[:4]
        month = current_date[-2:].replace("0", "")


        print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % (year, month, htmax, htmin, hrain, wtmax, wtmin, wrain)
        current_date = date
        htmax, htmin, hrain, wtmax, wtmin, wrain = "", "", "", "", "", ""

        if airport == 'W':
            wtmax, wtmin, wrain = tmax, tmin, rain
        else:
            htmax, htmin, hrain = tmax, tmin, rain



    
    
