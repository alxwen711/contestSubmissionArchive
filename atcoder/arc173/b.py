import sys
from math import gcd
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if there isn't a line with some very high number of colinear pts,
answer should be n//3 (limit is about 2/3rds of n)
"""

n = readint()
pts = list()
for _ in range(n):
    x,y = readints()
    pts.append((x,y))
d = {}
for a in range(n-1):
    for b in range(a+1,n):
        #compute slope
        num = pts[b][1]-pts[a][1]
        dom = pts[b][0]-pts[a][0]
        if dom == 0:
            num = 0
            dom = 0
        elif num == 0:
            dom = 1
        else:
            if num < 0:
                num *= -1
                dom *= -1
            g = gcd(num,dom)
            num //= g
            dom //= g
        #compute y-int
        yintn = pts[b][0]
        yintd = 0
        if num == 0:
            if dom == 1:
                yintn = pts[b][1]
                yintd = 1
        else:
            yintn = pts[a][1]*dom-pts[a][0]*num
            yintd = dom
            g = gcd(yintn,yintd)
            yintn //= g
            yintd //= g
        x = (num,dom,yintn,yintd)
        if d.get(x) == None: d[x] = list()
        d[x].append((a,b))
ans = n//3
for h in d.keys():
    dd = {}
    nn = 0
    for i in d[h]:
        if dd.get(i[0]) == None:
            dd[i[0]] = 1
            nn += 1
        if dd.get(i[1]) == None:
            dd[i[1]] = 1
            nn += 1
    ans = min(ans,n-nn)
print(ans)
        
