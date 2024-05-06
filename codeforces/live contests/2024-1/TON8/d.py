import sys
from copy import deepcopy
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
need to find k best values
note 4.5 second time limit, n caps at 1000, up to 5000 best vals
there should be some sort of scenario where only the best x vals
are kept given the high limit

results is an aggregate of all previous runs
best case ending chain at 0 -> 0
best case ending chain at 1 -> 1
best case ending chain at 2 -> 1-2, 2
best case ending chain at 3 -> 1-3, 2-3, 3 + 1 results
best case ending chain at 4 -> 1-4, 2-4, 3-4 + 1 results, 4 + 2 results

currently roughly 5 billion operations (O(n^3))
"""

for _ in range(readint()):
    n,k = readints()
    ref = list()
    for _ in range(n):
        tmp = [0]*n
        ref.append(tmp)
    for i in range(n):
        tmp = readar()
        for j in range(n-i):
            ref[i][i+j] = tmp[j]
    best = list()
    ans = list()
    best.append([0])
    ans.append([0])
    best.append([ref[0][0]])
    tmp = deepcopy(ans[-1])
    for snth in best[-1]:
        tmp.append(snth)
    tmp.sort()
    tmp.reverse()
    ans.append(tmp[:k])
    for a in range(1,n):
        # get best that END at this point
        tmp = list()
        for b in range(a+1):
            v = ref[b][a]
            if b <= 1:
                heappush(tmp,v)
            else:
                for c in ans[b-1]: # use heap if too slow
                    if len(tmp) == k:
                        if v+c < tmp[0]: break
                        heappop(tmp)    
                    heappush(tmp,v+c)
        tmp.sort()
        tmp.reverse()
        best.append(tmp[:k])

        # combine with previous
        tmp = deepcopy(ans[-1])
        for snth in best[-1]:
            tmp.append(snth)
        tmp.sort()
        tmp.reverse()
        ans.append(tmp[:k])
    print(*ans[-1])
