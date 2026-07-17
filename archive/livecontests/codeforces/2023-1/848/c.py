import sys
from itertools import combinations
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def score(a,h,ar,br,n):
    ans = 0
    #init lookup
    d = {}
    for i in range(len(ar)):
        d[ar[i]] = br.count(ar[i])
    chain = 0
    for j in range(n):
        if h[j] == 1 or d[a[j]] != 0: chain += 1
        else:
            ans += (chain*chain+chain)//2
            chain = 0
    ans += (chain*chain+chain)//2
    return ans


for i in range(readint()):
    n,k = readints()
    a = input()
    b = input()
    h = [0]*n
    d = {}
    for j in range(n):
        if a[j] == b[j]: h[j] = 1
        d[a[j]] = 1
    ar = list(d.keys())
    br = list(combinations(ar,min(len(ar),k)))
    #print(br)
    best = -1
    for m in range(len(br)):
        best = max(best,score(a,h,ar,br[m],n))
    print(best)
