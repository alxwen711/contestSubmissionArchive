import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
if a second highest val is not a child of the highest val, win
choose a value so that opp is forced to choose the highest value
left in the tree (if possible)

opp may not need to choose highest value but can still lose

the highest nodes have to have a different parent, if not, then disregard

if there are multiple lit up nodes, either:

choose the highest value node

assume there's multiple and just choose one?????????

what if you have higher nodes being parents to lower nodes?

if you have lower children, then disregard the values entirely?
"""

class Node:
    def __init__(self,v):
        self.edges = list()
        self.val = v
        self.parent = -1
        
for _ in range(readint()):
    n = readint()
    ar = readar()
    nodes = list()
    for i in range(n):
        nodes.append(Node(ar[i]))
    for _ in range(n-1):
        a,b = readints()
        nodes[a-1].edges.append(b-1)
        nodes[b-1].edges.append(a-1)
    q = [0]
    while len(q) != 0:
        x = q.pop()
        for u in nodes[x].edges:
            if u != 0 and nodes[u].parent == -1:
                nodes[u].parent = x
                q.append(u)
