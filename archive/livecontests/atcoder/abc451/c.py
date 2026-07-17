import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

hh = list()
for _ in range(readint()):
    q,h = readints()
    if q == 1: heappush(hh,h)
    else:
        while len(hh) != 0:
            if hh[0] <= h:
                heappop(hh)
            else: break
    print(len(hh))
        
