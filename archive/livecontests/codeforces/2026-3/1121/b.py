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
ideally go for an increasing line

make 2nd last as low as possible, last as high as possible
make their diff as extreme as possible

keep all other values as low as possible?

some form of greedily tracking the minimal sequence is needed

4 2
-4 12 -6 10


1 2 3 4 6 -10 -10 -10 -10 5

0 1 6
0 -4 14
"""
for _ in range(readint()):
    n,m = readints()
    ar = readar()
    prefix = [892347458972389457234897]
    for i in range(n):
        prefix.append(min(prefix[-1],ar[i]))
    best = -345787234578672348972389
    index = -1
    for a in range(m-1,n):
        if ar[a]-prefix[a] >= best:
            best = ar[a]-prefix[a]
            index = a
    h = list()
    for ii in range(index):
        heappush(h,(ar[ii],ii))
    br = list()
    for _ in range(m-1):
        br.append(heappop(h))
    br.sort(key = lambda x: x[1])
    br.append((ar[index],index))
    ans = 0
    prev = 0
    for snth in range(m):
        ans += (snth+1)*(br[snth][0]-prev)
        prev = br[snth][0]
    print(ans)
