import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Bob is trying to force both sets to have the same k_mex
"""

for _ in range(readint()):
    n,k = readints()
    ar = readar()
    h = [0]*(n+1)
    for i in ar:
        h[i] += 1
    ans = "YES"
    for j in range(n):
        if h[j] == 2*k-1: break
        elif h[j] < 2*k-1:
            ans = "NO"
            break
    print(ans)
