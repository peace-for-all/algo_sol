# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

def breakingRecords(scores):
    # breaks season record for most and least points in a game
    # int array with numbers she broke records; 0 for most points records and 1 is for least points records (2 numbers)
    lowest = max(scores) # big cheat - max()!
    highest = min(scores)
    
    rec = [0, 0]
    for k,v in enumerate(scores):
        print(scores)
        print(f"{k}: {v}, prev: {scores[k-1]} ({k-1})") # k-1 is -1! 
        if k-1 < 0:
            continue
        
        if v > highest:
            print(f"{v} > {highest}")
            # if v > scores[k-1]:
                # print(f"{v} > {scores[k-1]}, +1 rec")
            rec[0] += 1
            highest = v
        # if v > scores[k-1] and v > highest:

        if v < lowest:
            print(f"{v} < {lowest}")
        # if v < scores[k-1] and v < lowest:
            # if v < scores[k-1]:
                # print(f"{v} < {scores[k-1]}, +1 rec, new low!")
            rec[1] += 1
            lowest = v
    return rec 

    # The problem? First element is considered "lowest" record. 
    # StackOverflow? Everybody uses max(), min(), sort() functions (IMO it's a cheat, should do without it)
    # Also: HackerRank doesn't give a KeyError in case of [0-1]th element in list; it just gives you k[-1]th element, which is the last.