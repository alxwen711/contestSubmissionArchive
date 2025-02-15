import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
what positions allow aron to win?
if q is a leaf, then anything not a leaf for p wins
otherwise, p must be forced to move q into a depth 1 node for q to win
AND p cannot be already in a depth 1 node

if both are in depth 2 or greater, draw

tree dp actually needs to be inverted to count number of depth?? nodes can reach

q is depth 1 and snakes through depth 1 -> any edge going to depth 2 works
q is depth 2 and snakes through depth 1 -> any edgs going to alt depth 2 works


1->1->2
2->1->2

"""

class Node:
    def __init__(self):
        self.edges = {}
        self.deg = 0
        self.depth = -1
        self.leafcount = 0
        self.depth1 = 0
        self.depth2 = 0
        self.ac = 0
        
for _ in range(readint()):
    n = readint()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        u,v = readints()
        u -= 1
        v -= 1
        nodes[u].edges[v] = 1
        nodes[v].edges[u] = 1
        nodes[u].deg += 1
        nodes[v].deg += 1
    # determine depths and dp states
    leafcount = 0
    q = list()
    for i in range(n):
        if nodes[i].deg == 1:
            leafcount += 1
            nodes[i].depth = 0
            nodes[i].leafcount = 1
            q.append(i)
    ans = leafcount*(n-leafcount)
    while len(q) != 0:
        nq = list()
        for j in q:
            for k in nodes[j].edges.keys():
                if nodes[k].depth == -1:
                    nodes[k].depth = nodes[j].depth+1
                    if nodes[k].depth == 1: nodes[k].depth1 += 1
                    else: nodes[k].depth2 += 1
                    nq.append(k)
                if nodes[k].depth > nodes[j].depth:
                    nodes[k].leafcount += nodes[j].leafcount
                    nodes[k].depth1 += nodes[j].depth1
                    nodes[k].depth2 += nodes[j].depth2
        q = nq
    dd = {}
    for iii in range(n):
        if dd.get(nodes[iii].depth) == None: dd[nodes[iii].depth] = list()
        dd[nodes[iii].depth].append(iii)
    degvals = list(dd.keys()) # depth vals
    degvals.sort()
    for p in degvals:
        if p >= 2:
            for r in dd[p]:
                nodes[r].ac += 1
                for s in nodes[r].edges.keys():
                    if nodes[s].depth+1 == nodes[r].depth

                
    for i in range(n):
        if nodes[i].deg != 1: # turn 1 attempt
            for j in nodes[i].edges.keys():
                if nodes[j].depth == 1: # winning line is possible
                    for k in nodes[j].edges.keys():
                        if j == k: continue # do not add direct node
                        if nodes[k].depth > nodes[j].depth:
                            ans += nodes[k].depth2
