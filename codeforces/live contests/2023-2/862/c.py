import sys
from math import sqrt
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def bsearch(ar,n,x):
    low = 0
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] == x: return ar[mid]
        elif ar[mid] > x: high = mid
        else: low = mid
    a = abs(ar[low]-x)
    b = abs(ar[high]-x)
    if a > b: return ar[high]
    return ar[low]
    

def solve(n,m,ar,br):
    ar.sort()
    for i in range(m):
        a,b,c = br[i][0],br[i][1],br[i][2]
        if a*c <= 0: print("NO")
        else:
            d = 4*a*c
            # find closest value to b
            k = bsearch(ar,n,b)
            if ((b-k)**2 - d) < 0:
                print("YES")
                print(k)
            else: print("NO")

for i in range(readint()):
    n,m = readints()
    ar = list()
    for j in range(n):
        ar.append(readint())
    br = list()
    for k in range(m):
        a,b,c = readints()
        br.append([a,b,c])
    solve(n,m,ar,br)
