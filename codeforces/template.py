#!/bin/python3

import sys

data = []
for line in sys.stdin:
    # data.append([x for x in line.strip().split()])
        data.append(line.strip().split())
data.pop(0) # num lines

