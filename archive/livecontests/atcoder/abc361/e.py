import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())


"""
tree setup, must visit every node
solve from every leaf and go upwards?
would then be just sum of branches*2-(top two branches)

9/32 (23 WAs, something is fundementally flawed here)
something with the branching setup, only can remove highest cost?
above change still has 9/32, probably different method?

is it greedy?
"""

class Node:
    def __init__(self):
        self.cost = 0
        self.deg = 0
        self.edges = {}
        self.costs = list()

n = readint()
nodes = list()
for _ in range(n):
    nodes.append(Node())

for _ in range(n-1):
    a,b,c = readints()
    a -= 1
    b -= 1
    nodes[a].deg += 1
    nodes[b].deg += 1
    nodes[a].edges[b] = c
    nodes[b].edges[a] = c

# get all leaves
q = list()
for i in range(n):
    if nodes[i].deg == 1:
        q.append(i)
el = n-1
for j in range(n):
    x = q[j]
    # compute cost of x
    if len(nodes[x].costs) <= 1: nodes[x].cost = sum(nodes[x].costs)
    else:
        nodes[x].costs.sort()
        nodes[x].cost = sum(nodes[x].costs)*2-nodes[x].costs[-1]#-nodes[x].costs[-2]
        if j == n-1 and len(nodes[x].costs) >= 2: nodes[x].cost -= nodes[x].costs[-2]
    # transfer to "parents"
    for e in nodes[x].edges.keys():
        cv = nodes[x].cost+nodes[x].edges[e]
        if nodes[e].deg > 1 and el != 1: 
            nodes[e].deg -= 1
            nodes[x].deg -= 1
            el -= 1
            nodes[e].costs.append(cv)
            if nodes[e].deg == 1: q.append(e)
        elif el == 1 and nodes[e].deg == 1: # last edge
            el -= 1
            nodes[e].deg -= 1
            nodes[x].deg -= 1
            nodes[e].costs.append(cv)
            q.append(e)
    if j == n-1: print(nodes[x].cost) # answer

