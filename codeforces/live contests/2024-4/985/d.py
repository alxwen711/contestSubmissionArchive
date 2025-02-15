import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
plan is to remove all degree two nodes using the operation first
this will take at most around m operations
then determine if there is a double node case, if there is
then create the tree by joining two segments continually
otherwise, there are no edges
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.chain = 0
        self.f = -1

def solve(n,m):
    nodes = [0]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        a,b = readints()
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
    ans = list()
    # begin removing deg 2+ nodes
    for i in range(1,n+1):
        e = list()
        for c in nodes[i].edges.keys():
            if nodes[i].edges[c] == 1: e.append(c)
        for j in range(len(e)//2):
            a,b = e[2*j],e[2*j+1]
            nodes[i].edges[a] = 0
            nodes[a].edges[i] = 0
            nodes[i].edges[b] = 0
            nodes[b].edges[i] = 0
            if nodes[a].edges.get(b) == 1:
                nodes[a].edges[b] = 0
                nodes[b].edges[a] = 0
            else:
                nodes[a].edges[b] = 1
                nodes[b].edges[a] = 1
            ans.append((i,a,b))
    start = -1
    for k in range(1,n+1):
        e = list()
        for c in nodes[k].edges.keys():
            if nodes[k].edges[c] == 1: e.append(c)
        if len(e) != 0:
            start = k
            nodes[k].f = e[0]
    if start != -1: # generate tree, else no edges
        a,b = start,nodes[start].f
        nodes[a].chain = 1
        nodes[b].chain = 1
        for l in range(1,n+1):
            if nodes[l].chain == 0: # add to tree setup
                ans.append((a,b,l))
                nodes[l].chain = 1
                nodes[a].edges[b] = 0
                nodes[b].edges[a] = 0
                nodes[a].edges[l] = 1
                nodes[l].edges[a] = 1
                nodes[l].edges[b] = 1
                nodes[b].edges[l] = 1
                nodes[l].chain = 1
                if nodes[l].f != -1:
                    nodes[nodes[l].f].chain = 1
                b = l
    print(len(ans))
    for snth in ans:
        print(snth[0],snth[1],snth[2])
                
                

    
for _ in range(readint()):
    n,m = readints()
    solve(n,m)
