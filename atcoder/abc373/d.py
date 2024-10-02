import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
make everything bidirectional???????
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.v = 0
        self.deg = 0
        self.initi = False

n,m = readints()
nodes = list()
for ss in range(n+1):
    nodes.append(Node())
for _ in range(m):
    u,v,w = readints()
    nodes[u].edges[v] = w
    nodes[v].edges[u] = -w
for i in range(1,n+1):
    if nodes[i].initi == False: # default set to 0
        nodes[i].initi = True
        q = [i]
        while len(q) != 0:
            x = q.pop()
            for y in nodes[x].edges.keys():
                if nodes[y].initi == False: # compute value
                    val = nodes[x].edges[y]
                    nodes[y].v = nodes[x].v+val
                    nodes[y].initi = True
                    q.append(y)
ans = list()
for j in range(1,n+1):
    ans.append(nodes[j].v)
print(*ans)
