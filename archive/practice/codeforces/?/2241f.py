import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
The last segment must consist of odd 1 count followed by odd 0 count
it can then have inf 1's afterwards
inf 0's can occur before as well
this also has to be a subsequence
strip all front 0's and back 1's

11001100

Alice is able to effectively nuke a ton of the earlier string segment if needed
if odd 0 length at end, win by using all of them and either all 1's or everything
except rightmost (which will be moved to the end by construction)
also if odd 1's in general with any number of 0's at end, Alice wins
(take a 0 from end with all 1's)

if above conditions are not met, there has to be some of stall/move count?
or maybe Alice is just cooked? (from first WA it seems no)

after initial cleaning, just iterate through determine if
there exists some subsequence where ALL 1's are chosen AND an odd number of
inverses are possible

if there is odd number of 0's at back, can choose all here and take arbritary
odd 1 count
maybe refactor to even length segments?
"""

for _ in range(readint()):
    n = readint()
    s = readin()
    ar = list()
    flag = True
    # convert to array with first digit 1 and last digit 0
    for i in s:
        if flag:
            if i == "1":
                flag = False
                ar.append(int(i))
        else:
            ar.append(int(i))
    while len(ar) != 0:
        if ar[-1] == 1: ar.pop()
        else: break
    ans = "Bob"
    if len(ar) != 0:
        prev = ar[0]
        l = 0
        br = list()
        for k in range(len(ar)):
            if prev == ar[k]: l += 1
            else:
                br.append(l)
                l = 1
            prev = ar[k]
        br.append(l)
        for c in br:
            if c % 2 == 1: ans = "Alice"
    print(ans)


    
