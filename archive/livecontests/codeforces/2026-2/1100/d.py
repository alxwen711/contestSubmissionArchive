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
is it greedy? (remove the lowest possible high val each time)
greedy idea as it is is definitely wrong somewhere

heap system can be used?

3  6 12  4 10 12
2  3  2  7  8  9

solution is 1,1,1,1,1 to end up as (8,9)

can you eliminate the lowest _ values?

the order of the elements does matter

dp by column?
ans list: (2,3),(3,3),(3,3),(3,4),(4,8),(8,9)

2 3
2 3 3 6
2 2 3 3 6 12
2 2 3 3 4 6 7 12
2 2 3 3 4 6 7 8 10 12
2 2 3 3 4 6 7 8 9 10 12 12


adding an absolute min and absolute max should not change the result?

binary search??
- to reach a value of x, set any value lower as a 0 and the rest as 1s
- you then must eliminate all of the 0's

0 0 1 0 1 1
0 0 0 0 1 0

a 1 can be resolved here; only way to multiple 0 remove is with full 0's

0 0 1 0 1 1
0 0 0 0 1 1

0 1 0 1 1
0 0 0 1 1

0 0 1 1
0 0 1 1

0 1 1
0 1 1

0 1
1 1

1
1

this can be done greedily by the sum of the values
"""


dummy = 999999999

def encode(a,b,c):
    return a*1000000000000+b*1000000+c

def decode(x):
    return (x//1000000)%1000000,x%1000000

def bsearch(n,ar,br):
    nextpos = [(i+1) for i in range(n-1)]
    nextpos.append(899999)
    # setup the heap
    h = list()
    for i in range(n-1):
        a,b,c,d = ar[i],ar[i+1],br[i],br[i+1]
        h.append(encode(a+b+c+d,i,i+1))
    heapify(h)
    while len(h) != 0:
        x = heappop(h)
        st,ed = decode(x)
        if ed == 899999:
            continue # don't try to access this
        a,b,c,d = ar[st],ar[ed],br[st],br[ed]
        if max(a,b,c,d) != dummy:
            vals = [a,b,c,d]
            vals.sort()
            ar[st] = vals[1]
            br[st] = vals[2]
            ar[ed] = dummy
            br[ed] = dummy
            nextpos[st] = nextpos[ed]
            nextpos[ed] = 899999
            if nextpos[st] != 899999:
                e,f = ar[nextpos[st]],br[nextpos[st]]
                heappush(h,encode(vals[1]+vals[2]+e+f,st,nextpos[st]))
            
    ansa = min(min(ar),min(br))
    return ansa == 1

def f(n,ar,br,x):
    cr = [0]*n
    dr = [0]*n
    for i in range(n):
        if ar[i] >= x: cr[i] = 1
        if br[i] >= x: dr[i] = 1
    return bsearch(n,cr,dr)

anslist = list()

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    if n == 1:
        anslist.append(min(ar[0],br[0]))
        continue
    elif n == 2:
        l = [ar[0],ar[1],br[0],br[1]]
        l.sort()
        anslist.append(l[1])
        continue
    low = 1
    high = 2*n
    while high-low > 1:
        mid = (low+high)//2
        if f(n,ar,br,mid): low = mid
        else: high = mid
    if f(n,ar,br,high): anslist.append(high)
    else: anslist.append(low)
             
sys.stdout.write("\n".join(map(str,anslist)))
