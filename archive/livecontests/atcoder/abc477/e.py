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
N = 5, the edges are
1 2
2 3
3 4
4 5
5 1

1 6
2 6
3 6
4 6
5 6

so path i to j (assume i < j)
i, i+1, i+2 ..., j (basic +1)
i, n+1, n, ... j (go to back)
other various paths going i -> n+1 ... j (compute min costs going to n+1 first)
paths getting to i -> n ... j?

each one compute x to n+1
if n+1 in path, use that
otherwise, take minimum of both cycle options or just meeting at n+1
"""


n,q = readints()
ar = readar()
br = readar()
cyclecost = sum(ar)
prefix = [0]
for i in ar:
    prefix.append(prefix[-1]+i)


# determine minimum cost to reach n+1
mincosts = list()
h = list()
for ii in range(n):
    mincosts.append(br[ii])
    heappush(h,(br[ii],ii))

while len(h) != 0:
    x = heappop(h)
    cost,index = x[0],x[1]
    if mincosts[index] == cost:
        if (ar[index]+cost) < mincosts[(index+1) % n]:
            mincosts[(index+1) % n] = ar[index]+cost
            heappush(h,(ar[index]+cost,(index+1) % n))
        if (ar[(index-1) % n]+cost) < mincosts[(index-1) % n]:
            mincosts[(index-1) % n] = ar[(index-1) % n]+cost
            heappush(h,(ar[(index-1) % n]+cost,(index-1) % n))


for _ in range(q):
    s,t = readints()
    s -= 1
    t -= 1
    if t == n: print(mincosts[s])
    else:
        ans = mincosts[s]+mincosts[t]
        dist = prefix[t]-prefix[s]
        ans = min(ans,dist,cyclecost-dist)
        print(ans)
