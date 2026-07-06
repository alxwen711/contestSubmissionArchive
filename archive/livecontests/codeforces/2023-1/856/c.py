import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
1 1
2 2
3 3
4 4
5 5
"""
for i in range(readint()):
    n = readint()
    ar = readar()
    dp = [0]*n
    f = [0]*(n+5)
    l = 0
    s = 0
    for j in range(n):
        if ar[j] > l:
            f[ar[j]] += 1
            s += 1
        while s > l:
            l += 1
            s -= f[l]
        dp[j] = l
    print(*dp)
