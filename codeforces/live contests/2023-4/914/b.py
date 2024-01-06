import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
sort values, keep index?
for each value track where next value is higher than sum of previous combined
log highest index for each val
"""

def solve(n,ar):
    br = deepcopy(ar)
    br.sort()
    m = [0]*n
    s = br[0]
    for i in range(1,n):
        if br[i] > s: m[i] = 1
        s += br[i]
    bi = 0
    cr = list()
    for ai in range(n):
        if ai == bi:
            while bi != n:
                bi += 1
                if bi == n: break
                if m[bi] == 1: break
        cr.append(bi-1)
    d = {}
    for e in range(n):
        d[br[e]] = cr[e]
    ans = list()
    for j in ar:
        ans.append(d[j])
    print(*ans)
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
