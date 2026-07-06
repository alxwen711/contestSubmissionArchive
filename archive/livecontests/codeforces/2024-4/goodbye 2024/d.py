import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
max value strangely only goes up to 50000000
the values in br can be rearranged as needed
compute incrementing as preprocessing

if both arrays are sorted, then this is optimal
ordered set might be bait here
"""

def segtree(ar,br):
    n = len(ar)
    base = list()
    m = 998244353
    for i in range(n):
        base.append(min(ar[i],br[i]))
    ans = list()
    ans.append(base)
    while len(ans[-1]) != 1:
        tmp = list()
        for ii in range(len(ans[-1])//2):
            tmp.append((ans[-1][2*ii]*ans[-1][2*ii+1]) % m)
        ans.append(tmp)
    return ans

def update(ar,index,newval):
    m = 998244353
    ar[0][index] = newval % m
    ii = index//2
    for i in range(1,len(ar)):
        if len(ar[i]) == ii: break
        else: ar[i][ii] = (ar[i-1][ii*2]*ar[i-1][ii*2+1]) % m
        ii //= 2

def compute(ar):
    ans = 1
    m = 998244353
    for i in ar:
        if len(i) % 2 == 1: ans = (ans*i[-1]) % m
    return ans

for _ in range(readint()):
    n,q = readints()
    ar = readar()
    br = readar()
    cr = deepcopy(ar)
    dr = deepcopy(br)
    changes = list()
    for _ in range(q):
        a,b = readints()
        if a == 1:
            cr[b-1] += 1
            changes.append((a,cr[b-1]-1,cr[b-1]))
        else:
            dr[b-1] += 1
            changes.append((a,dr[b-1]-1,dr[b-1]))
    ar.sort()
    br.sort()
    ans = segtree(ar,br)
    ansl = list()
    ansl.append(compute(ans))
    index = -1
    baseval = -1
    for c in changes:
        #print(ar)
        #print(br)
        low = 0
        high = n-1
        if c[0] == 1: # change ar
            while high-low > 1:
                mid = (low+high)//2
                if ar[mid] > c[1]: high = mid
                else: low = mid
            if ar[high] <= c[1]: index = high
            else: index = low
            baseval = min(ar[index],br[index])
            ar[index] += 1
        else: # change br
            while high-low > 1:
                mid = (low+high)//2
                if br[mid] > c[1]: high = mid
                else: low = mid
            if br[high] <= c[1]: index = high
            else: index = low
            baseval = min(ar[index],br[index])
            br[index] += 1
        newval = min(ar[index],br[index])
        if newval != baseval:
            update(ans,index,newval)
        ansl.append(compute(ans))
    print(*ansl)
    
