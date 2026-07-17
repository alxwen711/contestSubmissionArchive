import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
idea should be to select all non-negative with a negative
-3 -5 -2 -5 -1 3
assume at least half (rounded up) MUST be selected
"""

for _ in range(readint()):
    n,c = readints()
    ar = readar()
    for i in range(n):
        ar[i] -= c
    ar.sort()
    ar.reverse()
    minindex = (n+1)//2
    ans = sum(ar[:minindex])
    for j in range(minindex,n):
        if ar[j] > 0: ans += ar[j]
        else: break
    print(ans)
