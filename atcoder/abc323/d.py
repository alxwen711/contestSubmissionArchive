import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = list()
d = {}
for i in range(n):
    s,c = readints()
    heappush(ar,s)
    d[s] = c
ans = 0
while len(ar) != 0:
    x = heappop(ar)
    y = d[x]
    ans += (y % 2)
    if y > 1:
        if d.get(2*x) == None:
            d[2*x] = 0
            heappush(ar,2*x)
        d[2*x] += (y//2)
print(ans)
    
