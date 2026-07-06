import sys
from math import gcd,lcm

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is up to 50000, arrays are not equal, there are SIX seconds
C1 probably does not work here (possible that increasing multiple
values can cause a higher gcd to occur)

determine first what is the minimum value each number could be
anything that could be set to the minimum, do so
then greedily consider cases by most to least restrictive multiple of c
that could be used?
"""

p = [1]*1000000
p[0] = 0
p[1] = 0
primes = list()
for i in range(2,1000000):
    if p[i] == 1:
        primes.append(i)
        for j in range(2*i,i,1000000):
            p[j] = 0


for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    g = ar[0]
    for i in range(1,n):
        g = gcd(g,ar[i])
    ans = 0
    # construct minimum array
    cr = [0]*n
    cr[0] = lcm(gcd(ar[0],ar[1]),g)
    cr[-1] = lcm(gcd(ar[-1],ar[-2]),g)
    for j in range(1,n-1):
        cr[j] = lcm(gcd(ar[j],ar[j+1]),gcd(ar[j],ar[j-1]),g)
    consider = list()
    for j in range(n):
        if cr[j] <= br[j] and cr[j] != ar[j]:
            ans += 1
            ar[j] = cr[j]
        elif cr[j]*2 <= br[j]: consider.append((br[j]//cr[j],cr[j],j))
    # now consider what could be incremented upwards
    consider.sort()
    for k in consider:
        for u in primes:
            if u > k[0]: break
            jj = k[2]
            testv = cr[jj]*u
            test = True
            if jj != 0:
                if gcd(testv,ar[jj-1]) != gcd(ar[jj],ar[jj-1]): test = False 
            if jj != n-1:
                if gcd(testv,ar[jj+1]) != gcd(ar[jj],ar[jj+1]): test = False
            if test:
                ar[jj] = testv
                ans += 1
                break
    print(ans)
    #print(consider)
    #print(ar)
    #print(cr)
