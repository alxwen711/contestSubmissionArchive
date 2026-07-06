import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
for each degree 3 node,
get the number of degree 2 nodes it has
if a degree 3 node is besides it, count it as part of a super cluster
"""

class Node:
    def __init__(self):
        self.edges = list()
        #self.col = -1
        self.deg = 0  
n = readint()
nodes = [0]
for _ in range(n):
    nodes.append(Node())
for _ in range(n-1):
    a,b = readints()
    nodes[a].edges.append(b)
    nodes[b].edges.append(a)
    nodes[a].deg += 1
    nodes[b].deg += 1
ans = 0
h = [1]*(n+1)
for i in range(1,n+1):
    if nodes[i].deg == 3 and h[i] == 1:
        h[i] = 0
        # get deg 3 cluster
        cluster = [i]
        q = [i]
        while len(q) != 0:
            x = q.pop()
            for j in nodes[x].edges:
                if h[j] == 1 and nodes[j].deg == 3:
                    cluster.append(j)
                    q.append(j)
                    h[j] = 0
        ef = {}
        for a in cluster:
            for b in nodes[a].edges:
                ef[b] = 1
        c = 0
        for j in ef.keys():
            if nodes[j].deg == 2: c += 1
        ans += (c*c-c)//2
print(ans)
