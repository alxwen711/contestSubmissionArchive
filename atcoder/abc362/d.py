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
    def __init__(self,w):
        self.w = w
        self.edges = {}
        self.cost = 1000000000000000000000000
        self.searched = 0
        

n,m = readints()
ar = readar()
nodes = list()
for i in ar:
    nodes.append(Node(i))
for _ in range(m):
    u,v,b = readints()
    u -= 1
    v -= 1
    nodes[u].edges[v] = b
    nodes[v].edges[u] = b
nodes[0].cost = nodes[0].w
r = n
q = [(nodes[0].w,0)]
while len(q) != 0:
    x = heappop(q)
    cost = x[0]
    nod = x[1]
    if nodes[nod].searched == 0:
        r -= 1
        nodes[nod].cost = cost
        nodes[nod].searched = 1
        for t in nodes[nod].edges.keys():
            nc = nodes[nod].cost+nodes[nod].edges[t]+nodes[t].w
            heappush(q,(nc,t))
        if r == 0: break
ans = list()
for ii in range(1,n):
    ans.append(nodes[ii].cost)
print(*ans)



        
