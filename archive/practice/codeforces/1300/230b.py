import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    return ar

n = readint()
ar = readar()
s = sieve(1000000)
d = {}
for j in range(1000001):
    if s[j]: d[j*j] = 1
for i in range(n):
    x = ar[i]
    if d.get(x) == 1: print("YES")
    else: print("NO")
