#!/bin/python3

# Merge jsons
import json
import sys

offers = []
with open('input.txt', 'r') as f:
    offers = f.readlines()
    n = int(offers.pop(0)) # unsafe

# can I read them 1 by 1?
onew = {}
for i in range(0, n):
    try:
        of_lst_dicts = json.loads(offers[i])

        # k-way merge with tournament tree? :-) (not many arrays here)
        for of_dict in of_lst_dicts['offers']: 
            # main "action" here: got items like {'offer_id': 'offer1', 'market_sku': 10846332, 'price': 1490} 
            # print(of_dict['offer_id'], of_dict['price'])
            if of_dict['price'] not in onew:
                onew[of_dict['price']] = of_dict
            else:
                # already have it! => compare offer_ids
                old_data = onew[of_dict['price']]

                if old_data['offer_id'] <= of_dict['offer_id']: # can't be equal? 
                    onew[of_dict['price']] = [old_data, of_dict]
                else:
                    onew[of_dict['price']] = [of_dict, old_data]

    except:
        print(f"Error: {sys.exc_info()[0]}: {sys.exc_info()[1]}, skipping line {i}")
        continue

# sort non-descending (asc w/equal elements) by price or (if equal) offer_id
onew_sorted = dict(sorted(onew.items())) #pythonic!

# unpack list with equal price, but "non-desc" offer_ids
onew_sorted_list = []
for k, v in onew_sorted.items():
    if isinstance(v, list):
        for i in v:
            onew_sorted_list.append(i)
    else:
        onew_sorted_list.append(v)

try:
    jstr = json.dumps({"offers": [v for k, v in onew_sorted.items()]})
    print(jstr)
except:
    print(f"Error: {sys.exc_info()[0]}: {sys.exc_info()[1]}")