#!/usr/bin/python

def stopwatch ( duration = 2, alert_msg = "timer ended", granularity = 1 ):
    import os, time, sys, math
    granularity=float(granularity)
    duration=float(duration)
    start = time.time()
    curr = time.time()
    last = start
    # sleep = granularity/2
    fmt = "\r%%.%sf" % (int(abs(round(math.log(granularity,10))))  if granularity<1 else "")
    while (curr-start < duration):
        curr = time.time()
        time_since_screen_update = (curr-last)
        if time_since_screen_update > granularity:
            sys.stdout.write( (fmt % (curr-start)) + ' / ' + str(int((duration))) + 's' )
            sys.stdout.flush()
            last = curr
        else:
            time.sleep( granularity - time_since_screen_update )

    command = 'flite -voice slt -t "' + alert_msg + '"'
    sys.stdout.write(command)
    os.system(command)
