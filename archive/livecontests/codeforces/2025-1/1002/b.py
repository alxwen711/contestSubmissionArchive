import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
maximal division case, then you have to check every single one
non-maximal, only up to 2
7 6
1 1 1 2 3 3 4
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    ans = 1
    if n == k:
        for i in range(k//2):
            if ar[2*i+1] == ans: ans += 1
            else: break
    else:
        if ar[1:n-k+2].count(1) == n-k+1: ans += 1
    print(ans)
