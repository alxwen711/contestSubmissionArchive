import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
2,3,5,7,11,13,17,19

2 -> -1
3 -> -1
4 -> 3 4 1 2
5 -> 4 5 1 2 3
7 -> 6 7 1 2 3 4 5
9 -> 3 4 5 6 7 8 9 1 2
11 -> 8 9 10 11 7 1 2 3 4 5 6
15 -> 14 15 10 11 12 13 9 1 2 3 4 5 6 7 8   13->7->2->-7
"""

from math import sqrt, floor

def sieve(n: int):
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    br = {}
    cr = list()
    for k in range(n+1):
        if ar[k] == True:
            br[k] = 1
            cr.append(k)
    return br,cr

primes,primeList = sieve(100000)

def solve(n,primes,primeList):
    limit = n
    v = 1
    ans = list()
    for snth in range(n,0,-1):
        if primes.get(abs(snth-v)) != None: #prime hit
            for a in range(snth,limit+1):
                ans.append(a)
                v += 1
            limit = snth-1
            if primes.get(v-1) != None: #1 finish
                for b in range(1,limit+1):
                    ans.append(b)
                break
    print(*ans)
        
    
for i in range(readint()):
    n = readint()
    solve(n,primes,primeList)
