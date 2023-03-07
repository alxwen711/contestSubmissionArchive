import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
"""
need to find n primes in this set
then for each combinatation find
the number of ways to arrange remaining numbers

if not prime or duplicate then must be an exponent
effectively a partition permutation problem
with the restriction that one set has to contain
only values from a given set (primes)


some prime setups result in exponent group having more/less duplicates
example: 150 val set, 100 primes with 50 duplicates

~~# number of permutations of the 2n values where~~
first n values are unique primes
= number of ways to satisfy first half
* number of ways to satisfy second half
- number of illegal setups

above fails because permutations [2,3,3,1] and [3,2,1,3] are equivalent
divide by n!? or make first half a combination to fix it in place
"""

from math import gcd,sqrt,ceil
from random import randint


def prime(n: int) -> bool:
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n <= 1: return False
    d,s = n-1,0
    while d % 2 == 0:
        s += 1
        d = d // 2
    for i in range(100):
        a = randint(2,n-2)
        if trial(n,s,a,d): return False
    return True


def trial(n: int, s: int, a: int, d: int) -> bool:
    val = pow(a,d,n)
    if val == 1 or val == n-1: return False
    for i in range(s-1):
        val = pow(val,2,n)
        if val == n-1: return False
    return True


p = {}
for i in range(n):
    if prime(ar[i]):
        if p.get(ar[i]) == None: p[ar[i]] = 0
        p[ar[i]] += 1
br = list(p.keys())
pcount = len(br)
if pcount < n: print(0)
else:
    


