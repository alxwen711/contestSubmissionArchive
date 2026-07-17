import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
get gcd for min x
find highest val
keep subbing until a hit is found
"""

def solve(n,ar):
    if n == 1: return 1
    if n == 2: return 3
    d = {}
    for i in ar:
        d[i] = 1
    m = max(ar)
    g = 0 #also x
    for j in ar:
        diff = m-j
        g = gcd(g,diff)
    t = m
    while d.get(t) != None:
        t -= g
    ar.append(t)
    ans = 0
    for q in ar:
        ans += ((m-q)//g)
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
