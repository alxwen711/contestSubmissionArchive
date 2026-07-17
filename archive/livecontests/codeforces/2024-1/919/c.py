import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
brute force has at most 160 factors (159 since 1 case always passes)
for each subarray,
find differences between each value in sorted
gcd the differences
"""
def f(n,ar,i): #split into i arrays
    dr = list()
    seg = n//i
    gg = 0
    for a in range(seg):
        #br = list()
        #for b in range(i):
        #    br.append(ar[a+b*seg])
        #br.sort()
        #cr = list()
        g = 0
        for c in range(i-1):
            v = ar[(c+1)*seg+a]-ar[c*seg+a]    
            g = gcd(g,v)
            if g == 1: return 0
        gg = gcd(gg,g)
        if gg == 1: return 0
    return 1
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    ans = 1
    for i in range(2,n+1):
        if n % i == 0:
            ans += f(n,ar,i)
    print(ans)
