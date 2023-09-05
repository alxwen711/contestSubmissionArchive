import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
either product of two different primes or cube of a prime
find prime factorization
determine which triplets to delete, if any
generate as many pairs as possible
"""

from math import sqrt, floor


def f(x,primes):
    if x == 1: return 1
    if primes[x] == 1: return 2
    n = x
    factors = {}
    while primes[n] != 1:
        if factors.get(primes[n]) == None: factors[primes[n]] = 0
        factors[primes[n]] += 1
        n //= primes[n]
    if factors.get(n) == None: factors[n] = 0
    factors[n] += 1
    fc = 0
    fh = 0
    for i in factors.keys():
        freq = factors[i]
        fc += freq
        fh = max(fh,freq)
    pairs = min(fc//2,fc-fh)
    return fc-(pairs*2)+1

def fsieve(n: int) -> list[int]: 
    ar = [1]*max(2,(n+1))
    ar[0] = 0
    for i in range(2,floor(sqrt(n))+1):
        if ar[i] == 1: #i is prime
            for j in range(i,n//i+1):
                if ar[i*j] == 1: ar[i*j] = i
    return ar


primes = fsieve(1000000)
for i in range(readint()):
    n = readint()
    if n == 1: print(1)
    elif primes[n] == 1: print(2)
    else:
        ar = list()
        ar.append(n)
        factors = {}
        while primes[n] != 1:
            if factors.get(primes[n]) == None: factors[primes[n]] = 0
            factors[primes[n]] += 1
            n //= primes[n]
        if factors.get(n) == None: factors[n] = 0
        factors[n] += 1
        #print(factors)
        for i in factors.keys():
            freq = factors[i]
            if freq >= 3: #varient with trip removal
                br = list()
                for j in range(freq//3+1): #implementation here is suboptimal
                    div = i**(3*j)
                    for k in ar:
                        br.append(k//div)
                ar = br
        ans = 8574985
        #print(ar)
        for s in ar:
            ans = min(ans,f(s,primes))
        print(ans)
