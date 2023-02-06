#!/bin/python3

# n is happy when
# sum of squares of its numbers lead to 1 eventually => happy (true)
# endless loop? -> not happy (false)

def is_happy_naive(n):
    next_n = prev_n = repeats = 0
    count = 0

    while n > 1:
        print(f"n: {n}")
        n_iter = list(str(n))
        n_next_lst = []

        n_sum = 0
        for i in n_iter:
            i = int(i)
            print(i)
            next_n = i * i
            print(f"Square: {next_n}")
            # 2, then 8 in 28
            n_sum += next_n
        n = n_sum

        print(f"Sum of 2 and 8 in 28; n = {n}, sum squares = {n_sum}")

        # prev_n = n
        # n = next_n
        # if prev_n == next_n:
        #     repeats += 1

        # if repeats >= 2: # magic number - idk why 2
        #     return False

        # this for any case
        if count > 100:
            print(f"Cycles: {count}")
            return False 
        count += 1

    print('happy')
    return True

# if is_happy_naive(23) != True:
#     print("\n\n\n")
#     print("TRY AGAIN: 23 should be happy: 1")
# assert is_happy_naive(23) == True, '23 isnt happy'

if is_happy_naive(2) != False:
    print('2 should cause endless loop, isnt happy')