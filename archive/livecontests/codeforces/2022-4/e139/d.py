import sys
from math import gcd,floor,sqrt
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
try EVERY factor??
"""
def sieve(n: int) -> list[bool]:
    ar = [True]*max(2,(n+1))
    ar[0] = False
    ar[1] = False
    for i in range(2,floor(sqrt(n))+1):
        if ar[i]: #i is prime
            for j in range(i,n//i+1):
                ar[i*j] = False
    return ar

def mp(diff,helper):
    l = max(2,round(diff**0.5)+1)
    for t in range(len(helper)):
        if diff % helper[t] == 0: return helper[t]
        if helper[t] > l: break
    return diff


x = sieve(3200)
helper = list()
for s in range(len(x)):
    if x[s]: helper.append(s)
d = {}
for i in range(readint()):
    a,b = readints()
    diff = b-a
    ans = 123456
    if d.get((a,b)) != None: print(d[(a,b)])
    elif diff == 1: print(-1)
    elif gcd(a,b) != 1: print(0)
    else:
        L = mp(diff,helper)
        if L == diff: ans = (L - (a % L))
        else: #find a way to get all factors
            ans = 0
            for t in range(L):
                if gcd(a+t,b+t) != 1: break
                ans += 1
        print(ans)
        d[(a,b)] = ans
