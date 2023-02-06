#!/bin/python3

import sys

data = []
for line in sys.stdin:
    # data.append([x for x in line.strip().split()])
        data.append(line.strip().split())
data.pop(0)

def count_sheeps(ars):
    # 4 - 1, 3 - 2, 2 - 3, 1 - 4
    answer = ''
    types = {'4': '1', '3': '2', '2': '3', '1': '4'}
    counts = {4: 0, 3: 0, 2: 0, 1: 0}

    for a in ars:
        for n in a:
            n = int(n)
            counts[n] += 1
            
        for k, v in types.items():
            k = int(k)
            v = int(v)
            if counts[k] > v:
                answer = 'NO'
        if not answer:
            answer = 'YES'
            
        print(answer)

count_sheeps(data)