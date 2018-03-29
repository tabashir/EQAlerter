#!/usr/bin/python

import os, sys
exec(compile(source=open('StopWatch.py').read(), filename='StopWatch.py', mode='exec'))
stopwatch(sys.argv[1], sys.argv[2], sys.argv[3])
