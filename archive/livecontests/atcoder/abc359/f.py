import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
all vertices must be of minimum degree 1
greedily choose lowest increments?
"""
n = readint()
ar = readar()

h = []
ans = 0
for i in ar:
    heappush(h,(i*3,i))
    ans += i
for _ in range(2*n-2-n):
    x = heappop(h)
    ans += x[0]
    heappush(h,(x[0]+x[1]+x[1],x[1]))
print(ans)
