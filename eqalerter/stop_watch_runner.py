#!/usr/bin/python

import os
import sys
exec(compile(source=open('stop_watch.py').read(), filename='stop_watch.py', mode='exec'))
stopwatch(sys.argv[1], sys.argv[2], sys.argv[3])
