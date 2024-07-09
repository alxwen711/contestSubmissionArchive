import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
assign each to middle
iterate through with prefix sum to get min length with fixpoint for mid
assign other two sections to other people, check if high enough
"""

def bsearch(n,ar,x,r):
    low = x
    high = n-2
    while high-low > 1:
        mid = (low+high)//2
        if (ar[mid+1]-ar[x]) >= r: high = mid
        else: low = mid
    if (ar[low+1]-ar[x]) >= r: return low
    elif (ar[high+1]-ar[x]) >= r: return high
    return -1

def solve(n,ar,br,cr):
    asum = [0]
    bsum = [0]
    csum = [0]
    for i in range(n):
        asum.append(asum[-1]+ar[i])
        bsum.append(bsum[-1]+br[i])
        csum.append(csum[-1]+cr[i])
    req = (asum[-1]+2)//3
    # ar case
    for a in range(1,n-1):
        x = bsearch(n,asum,a,req)
        if x == -1: break
        if bsum[a] >= req and (csum[-1]-csum[x+1]) >= req:
            print(a+1,x+1,1,a,x+2,n)
            return
        if csum[a] >= req and (bsum[-1]-bsum[x+1]) >= req:
            print(a+1,x+1,x+2,n,1,a)
            return
    # br case
    for b in range(1,n-1):
        x = bsearch(n,bsum,b,req)
        if x == -1: break
        if asum[b] >= req and (csum[-1]-csum[x+1]) >= req:
            print(1,b,b+1,x+1,x+2,n)
            return
        if csum[b] >= req and (asum[-1]-asum[x+1]) >= req:
            print(x+2,n,b+1,x+1,1,b)
            return
    # cr case
    for c in range(1,n-1):
        x = bsearch(n,csum,c,req)
        if x == -1: break
        if asum[c] >= req and (bsum[-1]-bsum[x+1]) >= req:
            print(1,c,x+2,n,c+1,x+1)
            return
        if bsum[c] >= req and (asum[-1]-asum[x+1]) >= req:
            print(x+2,n,1,c,c+1,x+1)
            return
    print(-1)
    return
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    cr = readar()
    solve(n,ar,br,cr)
