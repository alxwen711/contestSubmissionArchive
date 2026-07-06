import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
split points into groups that are reachable (at most 2 groups)
convert each diagonal grid into a rectangular one
compute manhatten diff between each (prefix sum twice)
"""
n = readint()
pts = list()
pts.append(list())
pts.append(list())

for _ in range(n):
    x,y = readints()
    if x % 2 == y % 2: pts[0].append((x,y))
    else: pts[1].append((x,y))

ans = 0
ar = list()
br = list()
for a in pts[0]:
    bb = (a[1]-a[0])//2
    br.append(bb)
    ar.append(a[1]-bb)
ar.sort()
br.sort()
asum = 0
bsum = 0
for i in range(len(ar)):
    ans += ar[i]*i-asum
    ans += br[i]*i-bsum
    asum += ar[i]
    bsum += br[i]

ar = list()
br = list()
for b in pts[1]:
    x,y = b[0]-1,b[1]
    bb = (y-x)//2
    br.append(bb)
    ar.append(y-bb)
ar.sort()
br.sort()
asum = 0
bsum = 0
for i in range(len(ar)):
    ans += ar[i]*i-asum
    ans += br[i]*i-bsum
    asum += ar[i]
    bsum += br[i]
print(ans)    
