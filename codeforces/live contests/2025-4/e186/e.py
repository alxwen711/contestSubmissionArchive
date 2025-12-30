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
y is the minimum cost of the gift
z is the minimum cost for +1
x is the min box req for +1 (if using a box)

greedily remove the cheapest box with largest box req each time,
and then need some sort of fast computation for number of boxes possible

removing cheapest box each time will either:
not be in largest set -> natural +1
be in largest set -> at worst equal

first try using none of the boxes (greed coins as hard as possible)
then throw the most expensive gift possible in a box?

1111110000000
111110?000000


use as many boxes as possible first
add number possible with coins
then possible to intentionally remove boxes with cheapest gifts,
basic recompute via a heap

possible that neither are optimized? (both scenarios have wa2)
i can kinda see setups where neither are optimal for necessity;
as to how to properly compute...?
"""


def bsearch(n,ar,weights,x): # x is number of boxes to use
    sp = n-x
    for i in range(x):
        if weights[i][0] > ar[sp+i]: return False
    return True

    
for _ in range(readint()):
    n,m,k = readints()
    ar = readar()
    br = list()
    for _ in range(n):
        x,y,z = readints()
        k -= y
        br.append((z-y,-x))
    br.sort()
    cr = list()
    for i in range(n):
        cr.append((-br[i][1],-br[i][0],i))
    cr.sort()
    ar.sort()
    low = 0
    high = min(m,n) # number actually possible
    h = [0]*n # 0 = unused, 1 = box, 2 = bought
    best = 0
    dr = list()
    while high-low > 1:
        mid = (low+high)//2
        if bsearch(m,ar,cr,mid): low = mid
        else: high = mid
    if bsearch(m,ar,cr,high):
        for j in range(high):
            h[cr[j][2]] = 1 # used in box
            dr.append(cr[j][2])
    else:
        for j in range(low):
            h[cr[j][2]] = 1 # used in box
            dr.append(cr[j][2])

    # get initial answer (max box + any coins possible)
    er = list()
    for snth in range(n):
        if h[snth] == 0:
            if k < br[snth][0]: break
            else:
                k -= br[snth][0]
                h[snth] = 2
                heappush(er,-snth)
    ans = n-h.count(0)

    possible = list()
    for iii in range(n):
        if h[iii] == 0: possible.append(iii)
    
    # now start removing from box set and check if answer could improve
    dr.sort()
    count = ans
    for ii in range(len(dr)):
        v = dr[ii]
        if len(er) == 0: break
        if v > (-er[0]): break
        h[v] = 0
        heappush(possible,v)
        count -= 1

        # eject at least 1 from er (if possible)

        if len(er) != 0:
            removal = -heappop(er)
            k += br[removal][0]
            heappush(possible,removal)
            h[removal] = 0
            count -= 1

        # readd as needed
        while len(possible) != 0:
            if k >= br[possible[0]][0]:
                k -= br[possible[0]][0]
                h[possible[0]] = 2
                count += 1
                heappush(er,-heappop(possible))
            else: break
    print(ans)




            
