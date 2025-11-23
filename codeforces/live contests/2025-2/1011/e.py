import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n = 10000, O(n^2)?
k must be at least max(B)+1
"""

def f(n,ar,blist,x):
    d = {}
    for a in ar:
        v = a % x
        if d.get(v) == None:
            d[v] = 0
        d[v] += 1
    for b in blist.keys():
        if d.get(b) == None: return False
        if d[b] != blist[b]: return False
    return True

def solve(n,ar,br):
    ar.sort()
    br.sort()
    for i in range(n):
        if ar[i] < br[i]: return -1
    sa = sum(ar)
    sb = sum(br)
    mv = max(br)+1
    diff = sa-sb
    if diff == 0: return 1000000000
    blist = {}
    for b in br:
        if blist.get(b) == None: blist[b] = 0
        blist[b] += 1
    for i in range(mv,2*diff):
        if i*i > diff: return -1
        if diff % i == 0:
            if f(n,ar,blist,i): return i
            #if f(n,ar,blist,diff//i): return diff//i
    return -1
            
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))
    
    
