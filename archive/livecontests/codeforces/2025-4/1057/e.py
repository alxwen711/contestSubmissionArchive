import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
function f is for all bases 2 to m, the k value so that for a
given a! and b!, a! and b! have differening trailing 0's in base k
and have the minimal number of 0's as well



get the prime factorization of n?

in most cases the f function will evaluate to 0 unless m is small
but m is at least n

 2357
10000
21000
31100
43100
53110
64210
74211
87211
97411
X8421

general case is as follows:
choose highest base that obtains answer of 1
push the counters until 1 is obtained
choose highest base that obtains answer of 2
push counters until 2 is obtained
repeat as needed until at a certain point

if n = 2, answer is always 0

find highest prime that is under n, this MUST be 1?
this makes the assumption that for all ranges x to 2x where x >= 2,
there exists a prime number

then find next highest prime that results in solution of 2+
and then next highest, etc

10000000 10000000 is only 279933

the maximum distance between primes is 154

use a prime to jump upwards
walk backwards to find 1/2/3...
but we can go higher upwards possibly?????

brute force factors? (n factorial not n, REALLY unsure how this works)

F something is really screwy
"""

sieve = [i for i in range(10000001)]
primes = [2]
for j in range(4,10000001,2):
    sieve[j] = 2
for i in range(3,3200):
    if sieve[i] == i:
        primes.append(i)
        for j in range(2*i,10000001,i):
            sieve[j] = i
for j in range(3200,10000001):
    if sieve[j] == j: primes.append(j)

def factors(x):
    if x <= 1: return [x]
    d = {}
    while sieve[x] != x:
        ff = sieve[x]
        if d.get(ff) == None: d[ff] = 0
        d[ff] += 1
        x //= ff
    if d.get(x) == None: d[x] = 0
    d[x] += 1
    flist = [1]
    for snth in d.keys():
        ar = list()
        for fff in flist:
            for g in range(d[snth]+1):
                ar.append(fff*(snth**g))
        flist = ar
    return flist

#pseudo dict
okay = [-1]*10000001
for i in range(len(primes)):
    okay[i] = i

for _ in range(readint()):
    n,m = readints()
    ans = 0
    # get to lowest highest prime, then binary search
    low = 0
    high = 664578
    while high-low > 1:
        mid = (low+high)//2
        if primes[mid] <= n: low = mid
        else: high = mid
    base = 232
    if primes[high] <= n: base = primes[high]
    else: base = primes[low]
    for k in range(base+1,n):
        bruteforce(n,k,m)
    

