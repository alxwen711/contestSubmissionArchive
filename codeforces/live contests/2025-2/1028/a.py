import sys
from math import gcd
from heapq import *
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
2*2*3
2*3*5
2*2*5
12,30,20

use dp to find the fastest path to the gcd
"""

def f(ar,g):
    """
    ma = max(ar)
    dp = [100000]*(ma+1)
    for i in ar:
        dp[i] = 0
    for a in range(ma,g-1,-1):
        for b in range(a+1,ma+1):
            if dp[a] != 100000 and dp[b] != 100000:
                gg = gcd(a,b)
                dp[gg] = min(dp[gg],max(dp[a],dp[b])+1)
    return dp[g]-1
    """
    ans = -1
    n = len(ar)
    while True:
        ans += 1
        a,b = -1,-1
        gg = 759783945948
        for x in range(n-1):
            for y in range(x+1,n):
                if gcd(ar[x],ar[y]) < gg:
                    gg = gcd(ar[x],ar[y])
                    a,b = x,y
        if gg == g: break
        if ar[a] > ar[b]:
            ar[a] = gg
        else: ar[b] = gg
    return ans
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    if n == 1: print(0)
    else:
        g = gcd(ar[0],ar[1])
        for i in range(2,n):
            g = gcd(g,ar[i])
        ans = 0
        for snth in ar:
            if snth != g: ans += 1
        if ans == n: # must create a g somewhere
            ans += f(ar,g)
        print(ans)
