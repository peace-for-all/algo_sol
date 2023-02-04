#!/bin/python3

# banned - int arr, n and maxSum - ints
# eligible:
# + in arnge [1, n]
# + each gotta be once
# + not in banned
# + sum of ints should not exceed maxSum

# TLE?! :D Correct, tests pass, but TLE.

def maxCount(banned, n, maxSum):
    result = []
    sum_res = 0

    for i in range(1, n+1):
        if i in banned:
            continue

        # the sum of chosen must not exceed maxSum?
        # sum_res = 0
        # for x in result:
        #     sum_res += x
        # if sum_res + i > maxSum:
        #     break

        # the sum of chosen must not exceed maxSum?
        if sum_res + i > maxSum:
            break
        else:
            sum_res = sum_res + i

        result.append(i)

    return len(result)

tests = [
    [[1, 6, 5], 5, 6, 2],
    [[1,2,3,4,5,6,7], 8, 1, 0],
    [[11], 7, 50, 7]
]
for t in tests:
    r = maxCount(t[0], t[1], t[2])
    print(f"Got: {r}, expected: {t[3]}")