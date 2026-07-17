import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
LIS must have min and max value (if len >= 2)
if only single len LIS, combine ar/br, reverse sort
if geq than min, must be on left in decreasing order
if lower than min, must be on right in decreasing order

"""
def longest(n,ar):
    br = [-1]*n
    cr = [-1]*(n+1)
    l = 0
    targetval = -1
    for i in range(n):
        low = 1
        high = l+1
        while low < high:
            mid = (low+high)//2
            if ar[cr[mid]] >= ar[i]: high = mid
            else: low = mid + 1
        lo = low
        br[i] = cr[lo-1]
        cr[lo] = i
        if lo > l:
            l = lo
            targetval = ar[cr[l]]
    ans = [-1]*l
    k = cr[l]
    for j in range(l-1,-1,-1):
        ans[j] = ar[k]
        k = br[k]
    return ans,targetval

def longest2(n,ar):
    br = [-1]*n
    cr = [9999999999999999999999999999999999]*(n+1)
    l = 0
    targetval = -1
    for i in range(n):
        low = 1
        high = l+1
        while low < high:
            mid = (low+high)//2
            if ar[cr[mid]] <= ar[i]: high = mid
            else: low = mid + 1
        lo = low
        br[i] = cr[lo-1]
        cr[lo] = i
        if lo > l:
            l = lo
            targetval = ar[cr[l]]
    ans = [-1]*l
    k = cr[l]
    for j in range(l-1,-1,-1):
        ans[j] = ar[k]
        k = br[k]
    return ans,targetval

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    aar = deepcopy(ar)
    aar.reverse()
    br = readar()
    br.sort()
    ans = list()
    cr,dd = longest(n,ar)
    dr,ee = longest2(n,aar)
    #print(cr,dr)
    if len(cr) == 1: #entriely decreasing
        cr = ar+br
        cr.sort()
        cr.reverse()
        print(*cr)
    else:
        x = cr[len(cr)//2]
        #if len(cr) == 2: x = cr[1]
        index = m-1
        while index != -1:
            ans.append(br[index])
            index -= 1
            if br[index] < x: break
            
        for ii in ar:
            ans.append(ii)
        for u in range(index,-1,-1):
            ans.append(br[u])
        ans2 = list()
        x = cr[len(cr)//2]
        #if len(cr) == 2: x = cr[1]
        index = m-1
        while index != -1:
            if br[index] < x: break
            ans2.append(br[index])
            index -= 1
            
        for ii in ar:
            ans2.append(ii)
        for u in range(index,-1,-1):
            ans2.append(br[u])
        aa,b = longest(len(ans),ans)
        aaa,b = longest(len(ans2),ans)
        if aa < aaa: print(*ans)
        else: print(*ans2)

