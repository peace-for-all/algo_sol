# https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

def bonAppetit(bill, k, b):
    # Write your code here
    # k - item anna doesn't eat
    total = 0
    bill.pop(k)
    for it in bill:
        total += it 
    
    if int(total / 2) == b:
        print('Bon Appetit')
    else:
        print(int(b - total/2))
       
# Trivial, one of those "read the desc carefully and it's all clear" cases.
# Didn't look anything up, just coded.
