import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Let e be the edge that if removed this is still a valid tree
ie. use some sort of BFS to find the cycle then choose an arbritary
edge there

solve case where this is a tree (no e)
from starting node, find cost of path to all others, add d[k]
then when traversing nodes? actually this would fail in cases
where the two nodes have nothing to do with starting node

the edges in terms of path cost DON'T mean shit

from a node with value x, must end at x-k

can the loop be utilized?
- find the loop
- then label these as a colour, everything else
results in a bunch of segmented parts, colour these by
the node they connect to on the loop
- go through dicts, if NOT in loop, then size + anything NOT same col
- if on loop, size + anything NOT same col (so loop designation here
means nothing)
- all this boils down to just find the loop
"""

class Node:
    def __init__(self):
        self.edges = set()
        self.parent = -1
        self.col = -1

class Accumul:
    def __init__(self):
        self.total = 0
        self.d = {}

n,k = readints()
nodes = ["nodes"]
for _ in range(n):
    nodes.append(Node())
ar = readar() # node vals
for _ in range(n):
    a,b = readints()
    nodes[a].edges.add(b)
    nodes[b].edges.add(a)

# find the cycle
st_node = 1
ptr = 0
q = [1]
cycle = []
while ptr != len(q):
    for e in nodes[q[ptr]].edges:
        if nodes[e].parent == -1 and e != st_node:
            nodes[e].parent = q[ptr]
            q.append(e)
        elif nodes[q[ptr]].parent != e: # did not traverse to parent
            # find the cycle starting with q[ptr] -> parent -> e
            patha = [q[ptr]]
            h = {}
            h[q[ptr]] = 1
            while nodes[patha[-1]].parent != -1:
                patha.append(nodes[patha[-1]].parent)
                h[patha[-1]] = 1
            pathb = [e]
            while nodes[pathb[-1]].parent != -1:
                pathb.append(nodes[pathb[-1]].parent)
                if h.get(pathb[-1]) == 1:
                    while patha[-1] != pathb[-1]:
                        patha.pop()
                    break
            patha.pop()
            pathb.reverse()
            cycle = patha + pathb
            break
    if cycle != []: break
    ptr += 1

#print(cycle)

# determine the colours
cyclenodes = {}
for c in cycle:
    cyclenodes[c] = 1
    nodes[c].col = c

for c in cycle:
    q = [c]
    while q:
        x = q.pop()
        for u in nodes[x].edges:
            if nodes[u].col == -1 and cyclenodes.get(u) == None:
                nodes[u].col = c
                q.append(u)

# construct dictionary
valdict = {}
for ii in range(n):
    vv = ar[ii]
    if valdict.get(vv) == None: valdict[vv] = Accumul()
    co = nodes[ii+1].col
    if valdict[vv].d.get(co) == None: valdict[vv].d[co] = 0
    valdict[vv].d[co] += 1
    valdict[vv].total += 1

ans = 0
for r in range(n):
    co = nodes[r+1].col
    target = ar[r]-k
    if valdict.get(target) != None:
        ans += valdict[target].total*2-valdict[target].d.get(co,0)
print(ans)
            

            









