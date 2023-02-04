#!/bin/python3

# DRAFT

# https://www.educative.io/courses/grokking-coding-interview-patterns-python/YQOnN622WRO

# phrase = "A roza upala na lapu azorA"
# expected = 'azorA lapu na upala roza A'

phrase = 'Reverse the words in a sentence'
expected = 'sentence a in words the Reverse'

lo = 0
hi = len(phrase)

rev = list(phrase[::-1])
print(rev)

for k, v in enumerate(rev):
    print(k, v)
    if v == ' ':
        hi = k
        while hi != lo:
            tmp = rev[lo]
            rev[hi] = rev[lo]
            rev[lo] = tmp
            lo += 1
            hi -= 1
        word = rev[lo:hi]
        drow = word[::-1]
        # print(list(reversed(word)))

        # after
        lo = k+1
        print('---------------------')
        # for i in range(lo, hi):
            # letter in "first unreversed" word
