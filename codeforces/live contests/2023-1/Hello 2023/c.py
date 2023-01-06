import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,x,ar):
    if n == 1: return 0
    ans = 0
    #check right
    s = 0
    hh = []
    for i in range(x,n):
        s += ar[i]
        heappush(hh,ar[i])
        if s < 0:
            ans += 1
            s -= (heappop(hh)*2)
    """
    #flip center
    if ar[x-1] > 0:
        ans += 1
        s = -ar[x-1]
    else: s = ar[x-1]
    """
    hh = []
    s = 0
    #check left until 2nd last
    for j in range(x-1,0,-1):
        s += ar[j]
        heappush(hh,-ar[j])
        if s > 0:
            ans += 1
            s += (heappop(hh)*2)
    return ans

for i in range(readint()):
    n,x = readints()
    ar = readar()
    print(solve(n,x,ar))
