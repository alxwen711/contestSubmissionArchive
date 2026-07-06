import sys
from itertools import combinations

"""
A few speed improvments important here:
arrays intialize faster than dicts in general
[0]*130 still takes longer than [0]*26, even
with subtracting 97 from each ord setup it's
significantly faster
initializing arrays with 0 values is faster
than with False values
"""

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def score(a,h,ar,br,n):
    ans = 0
    #init lookup setup
    d = [0]*26
    #set each in br to 1
    for u in range(len(br)):
        d[ord(br[u])-97] = 1
    chain = 0
    for j in range(n):
        if h[j] == 1 or d[ord(a[j])-97]: chain += 1
        else:
            ans += (chain*chain+chain)//2
            chain = 0
    ans += (chain*chain+chain)//2
    return ans


for i in range(readint()):
    n,k = readints()
    a = sys.stdin.readline()[:n]
    b = sys.stdin.readline()[:n]
    #print(a,b)
    h = [0]*n
    d = [0]*26 
    for j in range(n):
        if a[j] == b[j]: h[j] = 1
        d[ord(a[j])-97] = 1
    ar = list()
    for ss in range(26):
        if d[ss]: ar.append(chr(ss+97))
    #br = list(combinations(ar,min(len(ar),k)))
    #print(br)
    best = -1
    for m in combinations(ar,min(len(ar),k)):
        xx = score(a,h,ar,m,n)
        if xx > best: best = xx
    sys.stdout.write(str(best)+"\n")
