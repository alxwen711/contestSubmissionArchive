import sys
from math import gcd,lcm
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
cost can be any factor of a[i]*b[i]
bi is only up to 10000
something with gcd is involved
cost is some multiple of lcm bi
possible is gcd of ai*bi?
"""
for i in range(readint()):
    n = readint()
    ar = list()
    br = list()
    for j in range(n):
        a,b = readints()
        ar.append(a)
        br.append(b)
    index = 0
    ans = 0
    chain = False
    a,b = 0,0
    while index < n:
        if not chain:
            ans += 1
            if index+1 == n: break
            a = gcd(ar[index]*br[index],ar[index+1]*br[index+1])
            b = lcm(br[index],br[index+1])
            if a % b == 0:
                index += 2
                chain = True
            else: index += 1
        else:
            a = gcd(ar[index]*br[index],a)
            b = lcm(b,br[index])
            if a % b == 0: index += 1
            else:
                chain = False
    print(ans)
