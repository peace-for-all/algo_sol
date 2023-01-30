# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

def divisibleSumPairs(n, k, ar):
    # i < j and ar[i] + ar[j] is divisible by k
    # first line - n and k,
    # second - n ins, each a value of arr[i]
    
    # ar[i] + ar[j] is divisible by k
    i = 0
    out = []
    
    print(f"Find pairs in {ar}, whose sums divisible by {k}")
    for i in range(0,n):
        for j in range(n-1,-1,-1):
            print(f"i {i}, j {j}, ar[i] {ar[i]}, ar[j] {ar[j]}")
            if (ar[i] + ar[j]) % k == 0 and i > j:
                out.append((i,j))
        
    # return int - number of pairs
    print(out)
    return len(out)
