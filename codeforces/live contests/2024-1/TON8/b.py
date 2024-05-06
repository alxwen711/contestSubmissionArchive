import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
4 3 2 1 0
-4 -3 -2 -1 5
solution is ALWAYS possible,
so this means can fill out incrementally?
solve backwards?
"""
for _ in range(readint()):
    n = readint()
    ar = readar()
    d = [0]*n
    ans = list()
    mex = n
    for i in range(n):
        v = ar[-i-1]
        s = mex-v
        ans.append(s)
        if s < mex: mex = s
    ans.reverse()
    print(*ans)
