import sys
from math import gcd

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def solve(n,ar):
    if n == 1: return 0
    # if all values same, return 0
    ans = 0
    for j in range(n//2):
        a,b = ar[j],ar[-j-1]
        if a != b:
            x  = abs(a-b)
            if ans == 0:
                ans = x
            else: ans = gcd(ans,x)
    return ans

for i in range(readint()):
    n = readint()
    ar = readar()
    print(solve(n,ar))
    
