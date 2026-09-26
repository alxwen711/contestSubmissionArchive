import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

m = 998244353

"""
compute the sum of each layer
"""

fact = [1]

for i in range(1,250000):
    fact.append((fact[-1]*i) % m)

for _ in range(readint()):
    n = readint()
    ar = readar()
    ar.sort()
    v = ar[n-1]
    ans = 0
    bc = 1
    setv = fact[n-1]
    for i in range(n-1,0,-1):
        x = ar[i-1]
        diff = v-(x*(n-i))
        setv = (setv*pow(n-i,m-2,m)) % m
        #print(setv)
        ans += (diff*bc*setv)
        ans = ans % m
        bc = (bc*(n-i)) % m
        v += x
    #print()
    print(ans)
