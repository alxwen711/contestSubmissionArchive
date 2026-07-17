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
greedy mini heap?
only need to store the 40ish or so highest values?
"""

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    ar.sort()
    ar.reverse()
    for _ in range(q):
        # construct heap
        highest = [0]*35
        for a in range(min(35,n)):
            highest[a] = -ar[a]
        x = readint()
        ex = 1
        br = list()
        while x != 0:
            if x % 2 == 1: br.append(ex)
            x //= 2
            ex *= 2
        br.reverse()
        ans = 0
        for b in br:
            y = -heappop(highest)
            if y >= b: heappush(highest,-(y-b))
            else: ans += b - y
        print(ans)
