import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

for _ in range(readint()):
    n = readint()
    ar = readar()
    heapify(ar)
    if n == 1: 
        print(0)
        continue
    ans = max(ar)-ar[0]
    highest = max(ar)
    for _ in range(25*n):
        x = heappop(ar)
        mi = min(2*x,ar[0])
        highest = max(2*x,highest)
        ans = min(ans,highest-mi)
        heappush(ar,2*x)
    print(ans)
