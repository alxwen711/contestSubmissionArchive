import sys
from math import sqrt,floor

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def fsieve(n: int) -> list[int]: 
    ar = [1]*max(2,(n+1))
    ar[0] = 0
    for i in range(2,floor(sqrt(n))+1):
        if ar[i] == 1: #i is prime
            for j in range(i,n//i+1):
                if ar[i*j] == 1: ar[i*j] = i
    return ar


s = fsieve(1000000)
for i in range(readint()):
    n,m = readints()
    x = s[n]
    if x == 1: x = n
    if m >= x and x != 1: print("NO")
    else: print("YES")
