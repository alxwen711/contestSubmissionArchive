import sys
from itertools import permutations
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
g = readint()
edgelist = list()
for _ in range(g):
    a,b = readints()
    a -= 1
    b -= 1
    edgelist.append((a,b))
edges = {}
h = readint()
for _ in range(h):
    a,b = readints()
    a -= 1
    b -= 1
    edges[(a,b)] = 1
costs = list()
for _ in range(n):
    costs.append(readar())
p = list()
for i in range(n):
    p.append(i)
plist = list(permutations(p))
ans = 987564321456789
for j in plist:
    cel = {} # converted edge list
    for k in edgelist:
        a,b = j[k[0]],j[k[1]]
        if a > b: a,b = b,a
        cel[(a,b)] = 1
    an = 0
    for x in cel.keys():
        if edges.get(x) == None: an += costs[x[0]][x[1]-x[0]-1]
    for y in edges.keys():
        if cel.get(y) == None: an += costs[y[0]][y[1]-y[0]-1]
    if an < ans:
        ans = an
        
print(ans)
