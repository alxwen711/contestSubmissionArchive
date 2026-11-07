import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
11111 -> 1111 1111
1010 -> 101 101

if x <= k, remove
find minimal operations to remove

ternary search on the divisions?

possible solution: split

can we just brute force this? not really

binary search number of splits needed to allow
for a clean sweep line

the maximum answer is at most 357322
we can generally limit the answer to 2n
naively then up to n//2 splits (rounded up, 1 case should take 3 if k = 0)

suppose y splits are used, base val is k

y+k, y+1+k, y+2+k ..., n+y+y+k are the limits of the remaining values

3 4 5 6 7 8 9

let's still try splitting the largest ones naively?
there are cases where we do not split the largest
if we have a problem, find the largest value that could cover
a split, then remove

there is a limit on number of splits

keep the heap structure?

some values have to be split more than once
"""

from copy import deepcopy

def f(n,k,ar,x):
    splitvals = list()
    sp = 0
    splits = x
    maxv = k+x
    ptr = 0
    while ptr != n:
        if sp != len(splitvals):
            # there may be a split to consider
            if ptr+len(splitvals)-sp == n:
                # all remaining cases HAVE to fit under split
            elif ar[ptr+1] > splitvals[sp]*2:
                # largest value left, must go under split
                ptr += 1
                sp += 1
            # normal case
            
        else: # no splits
            if ar[ptr] <= maxv: # add to list normally
                ptr += 1
                maxv += 1
            else: # assume a split occurs somewhere
                splitvals.append(maxv)
                maxv += 2
                splits -= 1
                if splits == -1: return False

    return sp == len(splitvals)
        

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    ar.sort()
    #br = list()
    #for uhoh in ar:
    #    br.append(-uhoh)
    heapify(br)
    ar = br
    low = 0
    high = n//2+10
    while high-low > 1:
        mid = (low+high)//2
        if f(n,k,ar,mid): high = mid
        else: low = mid
    if f(n,k,ar,low): print(low*2+n)
    else: print(high*2+n)
