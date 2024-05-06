import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
at most 100 mill values, but could be done faster by assigning ranks
"""

def seg_init(n):
    ar = list()
    x = n
    while x != 0:
        tmp = [0]*x
        ar.append(tmp)
        x //= 2
    return ar

def seg_inc(ar,index,x):
    i = index
    for a in range(len(ar)):
        if len(ar[a]) == i: break
        ar[a][i] += x
        i //= 2

def query(ar,l,r): # get sum
    ans = 0
    for b in range(len(ar)):
        if l > r: break
        if l % 2 == 1:
            ans += ar[b][l]
            l += 1
        if r % 2 == 0:
            ans += ar[b][r]
            r -= 1
        l //= 2
        r //= 2
    return ans

n = readint()
ar = readar()
ar.reverse()
br = deepcopy(ar)
br.sort()
d = {}
index = 0
for i in range(n):
    if d.get(br[i]) == None:
        d[br[i]] = index
        index += 1
ans = 0
segsum = seg_init(index)
segcount = seg_init(index)
for j in range(n):
    x = ar[j]
    ii = d[x]
    seg_inc(segsum,ii,x)
    seg_inc(segcount,ii,1)
    ans += (query(segsum,ii+1,index-1)-(x*query(segcount,ii+1,index-1)))
print(ans)
