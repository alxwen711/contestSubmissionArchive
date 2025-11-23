import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())



"""
if the graph is not simple to begin with, make it simple


edge deduction formula is weird, number of edges left can decrease
with every single node merge
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.ec = 0
        self.parent = -1
        self.size = 1

n,m = readints()
nodes = [0]
onion = [0]
for _ in range(n):
    nodes.append(Node())
    onion.append(Node())
ec = 0
edgelist = list()
for _ in range(m):
    a,b = readints()
    if a < b: edgelist.append((a,b))
    else: edgelist.append((b,a))
    if nodes[a].edges.get(b) == None:
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
        nodes[a].ec += 1
        nodes[b].ec += 1
        ec += 1
        
q = readint()
ar = readar()
for i in ar:
    e = edgelist[i-1]
    # find parents
    a,b = e[0],e[1]
    while onion[a].parent != -1:
        a = onion[a].parent
    while onion[b].parent != -1:
        b = onion[b].parent
    if a == b: print(ec) # no merge needed
    else: # node merge is needed
        if nodes[a].ec > nodes[b].ec:
            for eb in nodes[b].edges.keys():
                if nodes[eb].ec != 0: # this node still exists
                    nodes[b].ec -= 1
                    nodes[eb].ec -= 1
                    ec -= 1
                    if nodes[a].edges.get(eb) == None and eb != a: # reconnect to a
                        nodes[a].edges[eb] = 1
                        nodes[eb].edges[a] = 1
                        nodes[a].ec += 1
                        nodes[eb].ec += 1
                        ec += 1
            onion[b].parent = a
            onion[a].size += onion[b].size
        else:
            for eb in nodes[a].edges.keys():
                if nodes[eb].ec != 0: # this node still exists
                    nodes[a].ec -= 1
                    nodes[eb].ec -= 1
                    ec -= 1
                    if nodes[b].edges.get(eb) == None and eb != b: # reconnect to b
                        nodes[b].edges[eb] = 1
                        nodes[eb].edges[b] = 1
                        nodes[b].ec += 1
                        nodes[eb].ec += 1
                        ec += 1
            onion[a].parent = b
            onion[b].size += onion[a].size
        print(ec)
