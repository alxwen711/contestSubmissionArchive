import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

from math import sqrt, floor

def sieve(n: int) -> list:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    br = list()
    cr = list()
    for k in range(len(ar)):
        if ar[k]:
            br.append(k)
            cr.append(k*k)
    return br,cr

primes,ps = sieve(32000)

def ff(x,primes,ps):
    d = {}
    lp = len(primes)
    while x != 1:
        for u in range(lp):
            if ps[u] > x:
                if d.get(x) == None: d[x] = 0
                d[x] += 1
                x = 1
                break
            if x % primes[u] == 0:
                if d.get(primes[u]) == None: d[primes[u]] = 0
                d[primes[u]] += 1
                x //= primes[u]
                break
    ans = list()
    bns = list(d.keys())
    for snth in range(len(bns)):
        ans.append([d[bns[snth]],bns[snth]])
    return ans

for i in range(readint()):
    n = readint()
    ar = ff(n,primes,ps)
    ar.sort()
    ar.reverse()
    m = [1]*len(ar)
    m[0] = ar[0][1]
    for j in range(1,len(m)):
        m[j] = m[j-1]*ar[j][1]
    br = list()
    prev = 983489347809437508247547
    for nn in range(len(ar)):
        if prev != ar[nn][0]:
            prev = ar[nn][0]
            br.append(prev)
    br.append(0)
    cr = list()
    for pls in range(len(br)-1):
        cr.append(br[pls]-br[pls+1])
    cr.reverse()
    prev = 83947568934759435
    inting = 0
    ans = 0
    for dd in range(len(ar)-1,-1,-1):
        if prev != ar[dd][0]:
            prev = ar[dd][0]
            ans += cr[inting]*m[dd]
            inting += 1
    print(ans)
