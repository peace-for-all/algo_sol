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

# if is_happy_naive(2) != False:
#     print('2 should cause endless loop, isnt happy')

def is_happy_fast_slow(n):
    print(f"Got {n}")

    def calc_sum_squares(n):
        prod = 0
        nlst = list(str(n))
        for i in nlst:
            i = int(i)
            prod += i*i
        return prod

    slow = n 
    fast = calc_sum_squares(n)

    while slow != fast: # NOPE, while what?
        if fast != 1 and fast != slow:
            slow += 1
            fast += 2
        if fast == 1:
            return True
    return False 

    print(f"Slow: {slow}, fast: {fast}")

if __name__ == '__main__':
    is_happy_fast_slow(28)