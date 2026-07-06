import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
each value MUST be above or below k
if exactly k, then ALL values must start at k (either 0 or -1)
>>> 439986238782-26250314066,581370817372-26250314066,409476934981-26250314066,287439719777-26250314066,737637983182-26250314066
(413735924716, 555120503306, 383226620915, 261189405711, 711387669116)
>>> 
>>> gcd(413735924716, 555120503306, 383226620915, 261189405711, 711387669116)
744129361
>>> 413735924716//744129361, 555120503306//744129361, 383226620915//744129361, 261189405711//744129361, 711387669116//744129361
(556, 746, 515, 351, 956)
>>> 556+746+515+351+956
3124

"""

def solve(n,ar):
    if n == 1: return 0
    b = ar[0]
    g = ar[0]
    if b == 0:
        if ar.count(0) == n: return 0
        else: return -1
    for i in range(1,n):
        if b*ar[i] <= 0: return -1
        g = gcd(g,ar[i])
    return abs(sum(ar))//g-n
        
for _ in range(readint()):
    n,k = readints()
    ar = readar()
    br = list()
    for i in ar:
        br.append(i-k)
    print(solve(n,br))
