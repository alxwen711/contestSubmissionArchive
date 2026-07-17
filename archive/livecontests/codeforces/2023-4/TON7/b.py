import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
does order matter (just try earliest possible

BBAAAB

"""

def solve(n,ar):
    h = [0]*(n-1)
    q = list()
    for a in range(n-1):
        if ar[a] == "A" and ar[a+1] == "B":
            q.append(a) #already low to high
            h[a] = 1
    while len(q) != 0:
        x = heappop(q)
        ar[x] = "B"
        ar[x+1] = "A"
        if x != 0:
            if ar[x-1] == "A" and h[x-1] == 0:
                h[x-1] = 1
                heappush(q,x-1)
        if x != n-2:
            if ar[x+2] == "B" and h[x+1] == 0:
                h[x+1] = 1
                heappush(q,x+1)
    return sum(h)

for _ in range(readint()):
    n = readint()
    s = sys.stdin.readline()
    ar = list()
    for i in range(n):
        ar.append(s[i])
    print(solve(n,ar))
    
