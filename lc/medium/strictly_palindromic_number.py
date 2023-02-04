#!/bin/python3

# https://leetcode.com/problems/strictly-palindromic-number/

# Notes: medium, because it's not just a "palindrome" question; it needs to check every base in a range. :-)

def isPalindromic(nb: int) -> bool:
    nb_str = list(str(nb))
    i = 0
    for i in range(0, len(nb_str)-1):
        j = len(nb_str) - 1 - i
        if nb_str[i] != nb_str[j]:
            return False
    return True

def isStrictlyPalindromic(n: int) -> bool:
    for b in range(2, n-1): # bcs inclusive
        # TODO: Do conversion here!
        nb = n / b

        isPalindromic(nb)
    
    return True

if __name__ == '__main__':
    print(isPalindromic(198091))