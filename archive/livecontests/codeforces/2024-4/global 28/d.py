import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
only coders above the first (kevin) will matter ranking wise
greedily clump the hardest problems together
"""

def binsearch(ar,x):
    n = len(ar)
    if n == 0: return 0
    low = 0
    high = n-1
    while high-low > 1:
        mid = (low+high)//2
        if ar[mid] >= x: high = mid
        else: low = mid
    if ar[low] >= x: return n-low
    elif ar[high] >= x: return n-high
    return 0

for _ in range(readint()):
    n,m = readints()
    ar = readar()
    br = readar()
    cr = list()
    x = ar[0]
    for i in ar:
        if i > x: cr.append(i)
    cr.sort()
    dr = list()
    for j in br:
        if j > x: dr.append(binsearch(cr,j)+1)
        else: dr.append(1)
    dr.sort()
    #print(dr)
    ans = list()
    for k in range(1,m+1):
        vv = 0
        for u in range(m//k):
            vv += dr[(u+1)*k-1]
        ans.append(vv)
    print(*ans)
