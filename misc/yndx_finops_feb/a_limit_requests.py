#!/bin/python3

OK = 200
ER_USER = 429
ER_SERV = 503

with open('input.txt', 'r') as f:
    data = f.readlines()

user_lim, serv_lim, duration = data.pop(0).split()
data.pop(len(data)-1) # not needing in py?

tbl = {}
for d in data:
    res = 0 # will be ok / er
    time, uid = d.split()
    
    if uid not in tbl:
        tbl[uid] = {'cnt': 1, 'times': [time]}
        res = OK
    else:
        if tbl[uid]['cnt'] + 1 > user_lim:
            res = ER_USER
        # unfinished :(


    # ER_USER: if (time - duration) from this user >= user_lim 

    # ER_SERV: if (time - duration) from all users >= serv_lim

    # else res = OK

    print(res)
    stdout.flush()


# Не забывайте о том, что ваша программа должна сбрасывать буфер вывода после вывода строчки с тайм-аутом. 
# stdout.flush()