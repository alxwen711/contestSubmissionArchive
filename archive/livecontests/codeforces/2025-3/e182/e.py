import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
easy case: n <= 5000, O(n^2) should work
first determine what the sequences are
then for each possible peak (both sides will have the same peak),
compute the number of possible orders for left side and right side (dp)
then select the peaks used

dp: either ignore it (stay in same position) or possibly add it
if lower than expected, then readd to same position
if exact same, move to next position (if it exists)
higher cannot exist

feels like double counting on peaks is possible with this method

maybe just count at each peak?

3rd test case has a problem
track 2d progressions with inclusion/exclusion,
left cases are simple; right cases on too high values could still
backtrack to a previous position, and cases that are too low could
still get backtracks?????
expected progression is 00,10,20,30...,80,91,92,93,94...

figure out what is going on with the dp setup here, definitely sure something is off here
"""

m = 998244353

for _ in range(readint()):
    n = readint()
    ar = readar()
    left = [ar[0]]
    right = [ar[-1]]
    for i in range(n-1):
        if ar[i+1] > left[-1]: left.append(ar[i+1])
        if ar[-i-2] > right[-1]: right.append(ar[-i-2])
    right.reverse()
    lll = len(left)
    dist = len(left)+len(right)
    dp = [0]*dist
    dpx = [0]*dist # needs to backtrack either to same index or further back
    dp[0] = 1
    for j in ar:
        ndp = deepcopy(dp) # exclude cases
        ndpx = deepcopy(dpx) 
        for d in range(dist):
            if d == 0: # no values are in yet
                if j == left[0]: ndp[1] = (ndp[1]+dp[0]) % m
            elif d < len(left):
                if j == left[d]: # exact match
                    ndp[d+1] = (ndp[d+1]+dp[d]) % m
                elif j <= left[d-1]: # went lower, remain in position
                    ndp[d] = (ndp[d]+dp[d]) % m
                # if going higher, invalid
            elif d != (dist-1): # on right side
                # dp cases
                if j == right[d-lll+1]: # exact match
                    ndp[d+1] = (ndp[d+1]+dp[d]+dpx[d+1]) % m
                elif j < right[d-lll+1]: # went lower, set to backtracker
                    ndpx[d+1] = (ndpx[d+1]+dp[d]+dpx[d+1]) % m
                else: # went higher, reverse backtracker
                    low = 0
                    high = d-lll+1
                    while high-low > 1:
                        mid = (low+high)//2
                        if j < right[mid]: low = mid
                        else: high = mid
                    if j == right[low]:
                        ndp[lll+low] = (ndp[lll+low]+dp[d]+dpx[d]) % m
                    else:
                        ndpx[lll+low] = (ndpx[lll+low]+dp[d]+dpx[d]) % m
            else: # should be complete, assuming no backtracker
                if j == right[-1]:
                    ndp[d] = (ndp[d]+dp[d]+dpx[d]) % m
                elif j < right[-1]:
                    ndpx[d] = (ndpx[d]+dp[d]+dpx[d]) % m
                else: # can never be lower
                    low = 0
                    high = d-lll
                    while high-low > 1:
                        mid = (low+high)//2
                        if j < right[mid]: low = mid
                        else: high = mid
                    if j == right[low]:
                        ndp[lll+low] = (ndp[lll+low]+dp[d]+dpx[d]) % m
                    else:
                        ndpx[lll+low] = (ndpx[lll+low]+dp[d]+dpx[d]) % m
        dp = ndp
        dpx = ndpx
        #print(sum(dp)+sum(dpx))
        #print(dp)
        #print(dpx)
    print(dp[-1])                        
