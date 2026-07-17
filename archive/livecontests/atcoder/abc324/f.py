import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
15/3 + 1000/1000 -> 1015/1003
50/30 + 1000/1000 -> 1050/1030

track best cases by value-ratio pardigram
if lower value, then must have higher beauty-cost

the "optimal" path to intermediate node it not necessarily
the best path to the node

update: we get wa, tle, and many problems

2/1 + 3000/1 -> 3002/2
21/10 + 3000/1 -> 3021/11

what even is optimal here
"""

def optimize(ar): #value-ratio pardigram
    if len(ar) == 0: return []
    br = list()
    for i in range(len(ar)):
        xv = ar[i]
        br.append((xv[0]-xv[1],xv[0]/xv[1],i))
    br.sort()
    cr = list()
    cr.append(ar[br[0][2]])
    r = br[0][1]
    for j in range(1,len(br)):
        if br[j][1] >= r:
            r = br[j][1]
            cr.append(ar[br[j][2]])
    return cr

n,m = readints()
edges = list()
for snth in range(m):
    tmp = readar()
    edges.append(tmp)
edges.sort()
ar = list()
ar.append("nil")
for uuuuu in range(n):
    tmp = list()
    ar.append(tmp)
ar[1].append((0,0))

prev = 1
for x in range(m):
    u,v,b,c = edges[x][0],edges[x][1],edges[x][2],edges[x][3]
    if u != prev: #optimize ar[u]
        prev = u
        ar[u] = optimize(ar[u])
    for i in ar[u]:
        nb,nc = i[0]+b,i[1]+c
        ar[v].append((nb,nc))
ans = 0
for ii in ar[n]:
    ans = max(ans,ii[0]/ii[1])
print(ans)
