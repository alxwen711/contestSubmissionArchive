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
overkill damage is encouraged

use the weakest sword you have that can kill any monster
with a sword first to boost as far as possible, then consider
any remaining monsters that do not have swords
"""



for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    cr = readar()
    heapify(ar)
    ans = 0
    last = list()
    first = list()
    for i in range(m):
        if cr[i] == 0: last.append(br[i])
        else: first.append((br[i],cr[i]))
    first.sort()
    dr = list()
    for j in range(len(first)):
        while len(ar) != 0:
            if ar[0] < first[j][0]:
                heappush(dr,heappop(ar))
            else: break
        if len(ar) == 0: break # proceed to end phase
        ans += 1
        if first[j][1] > ar[0]:
            heappop(ar)
            heappush(ar,first[j][1])
            
    # move anything in ar to dr
    while len(ar) != 0:
        heappush(dr,heappop(ar))

    last.sort()
    for k in range(len(last)):
        while len(dr) != 0:
            if dr[0] < last[k]:
                heappop(dr)
            else: break
        if len(dr) == 0: break # proceed to end phase
        ans += 1
        heappop(dr)
    print(ans)









        
