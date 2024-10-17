import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there are at most 100000 gcd values
only up to about 100 factors
sum setup, how many times is each gcd counted?
"""

def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        m = n
        n = r
        return gcd(m, n)

n = readint()
ar = readar()
d = {}
ans = 0
m = 998244353

for i in range(n):
    x = ar[i]
    br = list(d.keys())
    for c in br:
        y = gcd(x,c)
        if d.get(y) == None: d[y] = 0
        d[y] = (d[y]+d[c]) % m
        ans += (d[c]*y) % m
    print(ans)
    if d.get(x) == None: d[x] = 1
    else: d[x] = (d[x]+1) % m
    print(d)
