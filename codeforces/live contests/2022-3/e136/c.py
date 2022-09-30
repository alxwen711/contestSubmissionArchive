import sys
from math import comb
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
7,8,5,6,3,4,1,2
a = 7,6,3,2
b = 8,5,4,1


"""
"""
def game(a,b):
    first = True
    a.sort()
    b.sort()
    for k in range(len(a)):
        hit = False
        if first: #player 1's turn
            target = a.pop(-1)
            for s in range(len(b)):
                if b[s] > target:
                    hit = True
                    b.pop(s)
                    break
            if not hit: return 1
            first = False
        else: #player 2's turn
            target = b.pop(-1)
            for t in range(len(a)):
                if a[t] > target:
                    hit = True
                    a.pop(t)
                    break
            if not hit: return 2
            first = True
    return 0

#1,3,12,42,153,560
"""
"""
6 card game = 4+2
3 2 1 , last two cards don't matter in non tie
6 4

from itertools import combinations
x = [0,1,2,3,4,5,6,7,8,9,10,11]
arr = list(combinations(x,6))
ar = list()
for sn in range(len(arr)):
    tmp = list()
    for why in range(6):
        tmp.append(arr[sn][why])
    ar.append(tmp)
awin,bwin,tie = 0,0,0
for i in range(len(ar)):
    a = ar[i]
    b = list()
    for j in range(12):
        if a.count(j) == 0: b.append(j)
    res = game(a,b)
    if res == 1: awin += 1
    elif res == 2: bwin += 1
    else: tie += 1
print(awin,bwin,tie)

"""
#12
"""
does a have 12 -> a wins
does a not have 11 -> b wins 
does b have 10 -> b wins
does b not have 9 -> a wins
...
does a not have 3 -> b wins
does b have 2 -> b wins
if all failed -> tie
"""
m = 998244353
for i in range(readint()):
    n = readint()
    awin = 0
    bwin = 0
    count = 0
    for j in range(n,1,-1):
        if count == 0: #a win
            awin = (awin + comb(j-1,(j//2)-1)) % m
            count = 1
        elif count == 1: #a lose
            bwin = (bwin + comb(j-1,(j//2)-1)) % m
            count = 2
        elif count == 2: #b win
            bwin = (bwin + comb(j-1,(j//2)-1)) % m
            count = 3
        else: #b lose
            awin = (awin + comb(j-1,(j//2)-1)) % m
            count = 0
    print(awin,bwin,1)
    
