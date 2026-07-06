import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    a = sum(ar)
    b = 0
    ans = 1
    for j in range(n-1):
        a -= ar[j]
        b += ar[j]
        ans = max(ans,gcd(a,b))
    print(ans)
