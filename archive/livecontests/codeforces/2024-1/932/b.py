import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
mex 1 -> each seg contains 0, no 1
if sol exists, does 2 seg solution exist? (yes)
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    da = [0]*(n+1)
    db = [0]*(n+1)
    for i in ar:
        da[i] += 1
    ma = 0
    mb = 0
    for j in range(n):
        if da[ma] != 0: ma += 1
        else: break
    ans = -1
    for k in range(n-1):
        x = ar[k]
        da[x] -= 1
        if da[x] == 0:
            ma = min(x,ma)
        db[x] += 1
        while db[mb] != 0:
            mb += 1
        if ma == mb:
            ans = k+1
            break
    if ans == -1: print(-1)
    else:
        print(2)
        print(1,ans)
        print(ans+1,n)
