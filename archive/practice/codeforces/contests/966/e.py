import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine how many subsquares exist for each cell, then greedily assign
"""

for _ in range(readint()):
    n,m,k = readints()
    w = readint()
    ar = readar()
    vals = list()
    for a in range(n):
        for b in range(m):
            minx = max(0,a-k+1)
            maxx = min(n-k,a)
            miny = max(0,b-k+1)
            maxy = min(m-k,b)
            vals.append((maxx-minx+1)*(maxy-miny+1))
    vals.sort()
    vals.reverse()
    ar.sort()
    ar.reverse()
    ans = 0
    for i in range(w):
        ans += ar[i]*vals[i]
    print(ans)
