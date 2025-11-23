import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine some sort of way to translate the chord data
into some seg tree usable format

24 -> 31,37,35
26 -> 13,15,37,57

for a segment to cross, exactly 1 of the points must be in range

13 -> 24,26,28
37 -> 24,26,48,68
15 -> 26,28,46,48

this is some sort of 2d segment tree, but every coordinate is used at most once
so it could be 1d seg tree

options for hit range are cadb, acbd
"""

def bsearch(ar,lv,hv): # how many vals in sorted ar in [lv,hv]
    if len(ar) == 0: return 0
    low,high = 0,len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= lv: high = mid
        else: low = mid
    li = low
    if ar[low] >= lv: li = low
    elif ar[high] >= lv: li = high
    else: li = high+1

    low,high = 0,len(ar)-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] <= hv: low = mid
        else: high = mid
    hi = high
    if ar[high] <= hv: hi = high
    elif ar[low] <= hv: hi = low
    else: hi = low-1
    return max(0,hi-li+1)

    
def query(seg,l,r,low,high): # from index l to r, find num of values in low to high range
    li,ri = l,r
    ans = 0
    for i in range(len(seg)):
        if li > ri: break
        if li % 2 == 1:
            ans += bsearch(seg[i][li],low,high)
            li += 1
        if ri % 2 == 0:
            ans += bsearch(seg[i][ri],low,high)
            ri -= 1
        li //= 2
        ri //= 2
    return ans

def merge(ar,br):
    cr = list()
    aindex = 0
    bindex = 0
    a,b = len(ar),len(br)
    while aindex != a or bindex != b:
        if aindex == a:
            cr.append(br[bindex])
            bindex += 1
        elif bindex == b:
            cr.append(ar[aindex])
            aindex += 1
        elif br[bindex] < ar[aindex]:
            cr.append(br[bindex])
            bindex += 1
        else:
            cr.append(ar[aindex])
            aindex += 1
    return cr

n,m = readints()
h = list()
for _ in range(n+1):
    tmp = list()
    h.append(tmp)
for _ in range(m):
    a,b = readints()
    if a > b: a,b = b,a
    h[a//2].append(b//2)
#print(h)

# create seg

seg = [h]
while len(seg[-1]) != 1:
    tmp = list()
    for i in range(len(seg[-1])//2):
        tmp.append(merge(seg[-1][2*i],seg[-1][2*i+1]))
    seg.append(tmp)
    
q = readint()
for _ in range(q):
    c,d = readints()
    c,d = c//2,d//2
    if c > d: c,d = d,c
    print(query(seg,0,c,c+1,d)+query(seg,c+1,d,d+1,n))
