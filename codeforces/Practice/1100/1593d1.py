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
    x = min(ar)
    for j in range(n):
        ar[j] += -x
    ans = -1
    for k in range(n):
        x = ar[k]
        if x != 0:
            if ans == -1: ans = x
            else: ans = gcd(ans,x)
    print(ans)
