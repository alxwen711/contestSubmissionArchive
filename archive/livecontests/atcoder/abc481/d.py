import sys
from heapq import *

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

class Node:
    def __init__(self):
        self.edges = {}
        self.dist = 999999999

n,m,s,t = readints()
nodes = [0]
for _ in range(n):
    nodes.append(Node())

for _ in range(m):
    a,b = readints()
    nodes[a].edges[b] = 1

for i in range(1,n+1):
    lowest = 99999999
    for j in nodes[i].edges.keys():
        lowest = min(lowest,j)
    if lowest != 99999999: nodes[i].edges[lowest] = 0

nodes[s].dist = 0
q = [(0,s)]

while q:
    x = heappop(q)
    if x[1] == t: break
    if x[0] == nodes[x[1]].dist: # explore edges
        for k in nodes[x[1]].edges.keys():
            v = nodes[x[1]].edges[k] + x[0]
            if v < nodes[k].dist:
                nodes[k].dist = v
                heappush(q,(v,k))
if nodes[t].dist == 999999999: print(-1)
else: print(nodes[t].dist)





            
