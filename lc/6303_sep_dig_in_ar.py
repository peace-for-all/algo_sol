#!/usr/bin/python

ar = [7,1,3,99, 83]
expected = [7, 1, 3, 9, 9]

all = []
for i in ar:
    istr = str(i)
    for i in list(istr):
        all.append(i)

print(all)