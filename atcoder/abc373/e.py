import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

def f(n,m,k,rank,cr,y,x,br):
    #if y == 0: # no votes added
    #    return rank < m
    nvc = x+y # k-y votes left
    low = 0
    high = len(br)-1
    while high-low > 1:
        mid = (low+high)//2
        if br[mid] <= nvc: high = mid
        else: low = mid
    nr = low
    if br[low] > nvc: nr = high
    if br[high] > nvc: nr = high+1
    if nr >= m: return False # rank is initially too high
    req = cr[m]-cr[nr]
    if rank[x] < m: req = cr[m+1]-x-cr[nr]
    req = (nvc+1)*(m-nr)-req
    if req > k-y: return True
    return False

n,m,k = readints()
ar = readar()
r = k-sum(ar) # votes remaining
if m == n:
    ans = [0]*n
    print(*ans)
else:
    br = deepcopy(ar)
    br.sort()
    br.reverse()
    rank = {}
    for ii in range(n):
        if rank.get(br[ii]) == None:
            rank[br[ii]] = ii
    cr = [0] # highest current totals
    for i in range(n):
        cr.append(cr[-1]+br[i])
    threshold = br[m-1]
    ans = list()
    for j in range(n):
        x = ar[j]
        t = cr[m]
        if x >= threshold: t = cr[m+1]-x
        low = 0
        high = r
        while high-low > 1:
            # determine new rank with internal binary search
            mid = (low+high)//2
            if f(n,m,r,rank,cr,mid,x,br): high = mid
            else: low = mid
        if f(n,m,r,rank,cr,low,x,br): ans.append(low)
        elif f(n,m,r,rank,cr,high,x,br): ans.append(high)
        else: ans.append(-1)
    print(*ans)


            
