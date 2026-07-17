import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if 2 portals overlap, their ranges also overlap
then there's a list of minimums with the portal maximums
that can be used for queries?
"""

def bs(br,x):
    low = 0
    high = len(br)-1
    while high-low > 1:
        mid = (low+high)//2
        if br[mid][0] <= x: low = mid
        else: high = mid
    if br[high][0] <= x: return br[high][1]
    elif br[low][0] <= x: return br[low][1]
    else: return -1

for i in range(readint()):
    n = readint()
    ar = list()
    for j in range(n):
        a,b,c,d = readints()
        ar.append((a,b,c,d))
    ar.sort()
    br = list()
    lb = -99999
    v = -1
    cr = list() # portal segments
    for k in ar:
        while len(cr) != 0:
            if k[0] > cr[0][1]: #entry is right of portal
                heappop(cr)
            elif k[1] < cr[0][0]: #entry is left of portal
                break
            else: #overlap
                heappush(cr,(k[2],k[3]))
                v = max(v,k[3])
                break
            
        if len(cr) == 0: #new portal segment, c
            br.append((lb,v))
            lb = k[0] # a
            v = k[3] # d
            cr.append((k[2],k[3]))
            
    br.append((lb,v))
    br.sort()
    dd = readint()
    q = readar()
    ans = list()
    for f in q:
        ans.append(max(f,bs(br,f)))
    #print(br)
    print(*ans)
