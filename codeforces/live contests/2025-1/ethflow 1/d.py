import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
start from largest value as the head
"""

class Node:
    def __init__(self,v):
        self.val = v
        self.edges = list()
        self.inc = 0
        self.hit = False

def solve():
    n = readint()
    nodes = list()
    for _ in range(n):
        a,b = readints()
        nodes.append(Node(a))
    for _ in range(n-1):
        a,b = readints()
        nodes[a-1].edges.append(b-1)
        nodes[b-1].edges.append(a-1)
    best = -1
    index = -1
    for i in range(n):
        if nodes[i].val > best:
            best = nodes[i].val
            index = i
    nodes[index].hit = True
    q = [index]
    while len(q) != 0:
        x = q.pop()
        high = nodes[x].val
        children = list()
        for e in nodes[x].edges:
            if nodes[e].hit == False:
                nodes[e].hit = True
                children.append(e)
                high = max(high,nodes[e].val)
                q.append(e)
        for c in children:
            nodes[c].inc = nodes[x].inc+high-nodes[c].val
    ans = -1
    for u in range(n):
        ans = max(ans,nodes[u].val+nodes[u].inc)
    return ans

    
for _ in range(readint()):
    print(solve())
