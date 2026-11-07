import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
From 1 to v, you must choose the shortest path
then there is priority in lower numbered edge

you need previous ranking and current edge

inheriting value -> always go by priority value
"""

p = 998244353

n,m = readints()
nodes = [0]

class Node:
    def __init__(self):
        self.edges = {}
        self.val = -1
        self.pval = 999999999999999999999

for _ in range(n):
    nodes.append(Node())
for _ in range(m):
    a,b,c = readints()
    if a != b: nodes[a].edges[b] = min(nodes[a].edges.get(b,99),c)

nodes[1].val = 0
nodes[1].pval = 0

rank = {}
rank[1] = 0

layer = set()
layer.add(1)

while layer:
    nextlayer = set()
    for l in layer:
        v = nodes[l].val
        r = rank[l]
        for e in nodes[l].edges.keys():
            if nodes[e].val == -1:
                nextlayer.add(e)
                nodes[e].val = (v*10+nodes[l].edges[e]) % p
                nodes[e].pval = r*100+nodes[l].edges[e]
            elif e in nextlayer and r*100+nodes[l].edges[e] < nodes[e].pval:
                nodes[e].val = (v*10+nodes[l].edges[e]) % p
                nodes[e].pval = r*100+nodes[l].edges[e]
    #print(layer)
    if nextlayer:
        rank = {}
        br = list()
        lookup = set()
        for snth in nextlayer:
            lookup.add(nodes[snth].pval)
        lookup = list(lookup)
        lookup.sort()
        dd = {}
        for iii in range(len(lookup)):
            dd[lookup[iii]] = iii
        for ef in nextlayer:
            rank[ef] = dd[nodes[ef].pval]
    layer = nextlayer

anslist = list()
for ii in range(2,n+1):
    anslist.append(nodes[ii].val)

sys.stdout.write("\n".join(map(str,anslist)))


