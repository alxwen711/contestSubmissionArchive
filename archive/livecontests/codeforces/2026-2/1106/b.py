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
values can only go up to n
"""

for _ in range(readint()):
    n = readint()
    ans = 0
    for i in range(1,n+1):
        c = n//i
        ans += c*c
    print(ans)
    """
    for a in range(1,n+1):
        for b in range(1,n+1):
            for c in range(1,n+1):
                if gcd(lcm(a,b),lcm(b,c)) == gcd(a,c) and b != 1:
                    print((a,b,c))
                    ans += 1
    print(ans)
    """
