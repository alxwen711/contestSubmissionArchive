import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
max value is 10**18
use only primes up to 1000000
"""

p = [1]*1000000

primes = list()
for i in range(2,1000000):
    if p[i] == 1:
        primes.append(i)
        for j in range(2*i,1000000,i):
            p[j] = 0


for _ in range(readint()):
    n = readint()
    ar = list()
    for i in range(n):
        ar.append(primes[i]*primes[i+1])
    print(*ar)
