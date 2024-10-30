import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
compute how many squares each queen covers
= sum of x lines - (x-1) for central collision

there may be queens that full cover other lines

then for remaining lines compute number of collisions
in board

if collision count is 1, subtract 1
if collision count is 3, subtract 2
if collision count is 6, subtract 3
"""

n,m = readints()
ans = n*n
hor = {}
ver = {}
ld = {}
rd = {}
for _ in range(m):
    lc = 0
    a,b = readints()
    if hor.get(a) == None:
        hor[a] = 1
        ans -= n
    if ver.get(b) == None:
        ver[b] = 1
        ans -= n
    if ld.get(a+b) == None:
        ld[a+b] = 1
        ans -= (n-abs(n+1-a-b))
    if rd.get(a-b) == None:
        rd[a-b] = 1
        ans -= (n-abs(a-b))
hor = list(hor.keys())
ver = list(ver.keys())
ld = list(ld.keys())
rd = list(rd.keys())
#print(hor)
#print(ver)
#print(ld)
#print(rd)
#print(ans)
dupes = {}
#1,4,5,-3
# hor-ver
for h in hor:
    for v in ver:
        if dupes.get((h,v)) == None: dupes[(h,v)] = 0
        dupes[(h,v)] += 1

for h in hor:
    for l in ld:
        a = h
        b = l-a
        if max(a,b) <= n and min(a,b) >= 1:
            if dupes.get((a,b)) == None: dupes[(a,b)] = 0
            dupes[(a,b)] += 1

for h in hor:
    for r in rd:
        a = h
        b = a-r
        if max(a,b) <= n and min(a,b) >= 1:
            if dupes.get((a,b)) == None: dupes[(a,b)] = 0
            dupes[(a,b)] += 1

for v in ver:
    for l in ld:
        b = v
        a = l-b
        if max(a,b) <= n and min(a,b) >= 1:
            if dupes.get((a,b)) == None: dupes[(a,b)] = 0
            dupes[(a,b)] += 1


for v in ver:
    for r in rd:
        b = v
        a = r+b
        if max(a,b) <= n and min(a,b) >= 1:
            if dupes.get((a,b)) == None: dupes[(a,b)] = 0
            dupes[(a,b)] += 1

for l in ld:
    for r in rd:
        if l % 2 == r % 2:
            a = (l+r)//2
            b = l-a
            if max(a,b) <= n and min(a,b) >= 1:
                if dupes.get((a,b)) == None: dupes[(a,b)] = 0
                dupes[(a,b)] += 1
h = [0]*7
for d in dupes.keys():
    v = dupes[d]
    h[v] += 1
    if v == 1: ans += 1
    elif v <= 3: ans += 2
    else: ans += 3
print(ans)
#print(dupes)
#print(h)
