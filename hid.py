#!/usr/bin/python

import sys
import time
import random

string = "123456789\n"

def color(text):
    sys.stdout.write(u"\x1B[{0}m{1}\x1B[0m".format
                                 (random.choice(range(31,36)+
                                               range(90,97)),i))
    sys.stdout.flush()
    time.sleep(random.random()/6)

for i in string:
    color(i)
