import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there can be multiple components, initial game is probably
just connecting all these components
also dependent on the degree of the node being connected
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.colour = -1

n,m = readints()
nodes = list()
for _ in range(n+1):
    nodes.append(Node())

for _ in range(m):
    a,b = readints()
    nodes[a].edges[b] = 1
    nodes[b].edges[a] = 1

components = list()

for i in range(1,n+1):
    if nodes[i].colour == -1:
        red,blue = 1,0
        nodes[i].colour = 0
        q = [i]
        while len(q) != 0:
            x = q.pop()
            for k in nodes[x].edges.keys():
                if nodes[k].colour == -1:
                    nodes[k].colour = nodes[x].colour ^ 1
                    if nodes[k].colour == 0: red += 1
                    else: blue += 1
                    q.append(k)
        components.append((red,blue))


