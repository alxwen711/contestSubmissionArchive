import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
#ar = list()
br = list()
n = 100
m = 100
for a in range(1,n+1):
    for b in range(1,m+1):
        c = a + b
        d = b*gcd(a,b)
        #if c % d == 0: ar.append((a,b))
        if d % c == 0: br.append((a,b))
#print(ar)
br.sort()
print(br)

only factors look to be involved
true in part a, but part b there's something else
(10,15) is a valid pair in B
these all have a ratio setup of one of the following:
(1,x)
(x,1)
(2,p2), where 2+p2 = p3, p2,p3 are primes

there are a lot more co-prime cases
if it works one way, it works the other way

"""
"""
from math import sqrt, floor

def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    br = list()
    for ii in range(len(ar)):
        if ar[ii]: br.append(ii)
    return br



primes = sieve(2000000)
"""

def f(a,b,g):
    c = a + b
    d = b*g
    if d % c == 0: return 1 # c % d for pt a
    return 0
d = {}
m = 987654321
for _ in range(readint()):
    n,m = readints()
    #ar = list()
    ans = min(n,m)//2 # (i,i) cases
    for i in range(1,min(n,m)+1): #small val
        for j in range(i+1,min(n,m)+1): #large val
            if i == j: break
            a = i*(i+j)
            b = j*(i+j)
            if max(a,b) > max(n,m): break
            if a <= n and b <= m:
                ans += 1
                
                for snth in range(2,min(n//a,m//b)+1):
                    v = a*snth*m+b*snth
                    if d.get(v) == None:
                        d[v] = 1
                        ans += f(a*snth,b*snth,(i+j)*snth)
            if b <= n and a <= m:
                ans += 1
                for snth in range(2,min(n//b,m//a)+1):
                    v = a*snth*m+b*snth
                    if d.get(v) == None:
                        d[v] = 1
                        ans += f(b*snth,a*snth,(i+j)*snth)
            
    print(ans)
    #print(ar)
            
