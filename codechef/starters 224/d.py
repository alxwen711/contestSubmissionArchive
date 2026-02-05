import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
problem f allows nodes to be touched 3 times, here this is 2 times
(only 1 possible walk if 1 time)
ans can be large? combine multiple backtracks
traversing 0 to n-1
tree dp methods? O(n log n) algo needed
main path can be interrupted by choosing alternate branch

compute path from 1 to n
single case: sum of previous single/double
double case: consider other branches (how? number of nodes???) and previous node (single)
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.parent = -1
        self.single = 1
        self.double = 0
        
m = 998244353

def count_nodes(nodes,e,p):
    # count number of nodes from e excluding p in search
    q = [e]
    d = {}
    d[e] = 1
    while len(q) != 0:
        x = q.pop()
        for ee in nodes[x].edges.keys():
            if ee != p and d.get(ee) == None:
                d[ee] = 1
                q.append(ee)
    return len(list(d.keys()))

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
    # compute the path from 0 to n-1
    q = [0]
    while len(q) != 0:
        x = q.pop()
        for e in nodes[x].edges.keys():
            if nodes[e].parent == -1 and e != 0:
                nodes[e].parent = x
                q.append(e)
    path = [n-1]
    while path[-1] != 0:
        path.append(nodes[path[-1]].parent)
    path.reverse()

    for i in range(len(path)):
        p = path[i]
        if p != 0: # not first node
            nodes[p].single = (nodes[path[i-1]].single+nodes[path[i-1]].double) % m
        if p != n-1: # not last node
            prev = nodes[p].parent
            nextnode = path[i+1]
            for e in nodes[p].edges.keys():
                if e != nextnode:
                    if e == prev: nodes[p].double = (nodes[p].double+nodes[e].single) % m
                    else: # count nodes
                        nc = count_nodes(nodes,e,p)
                        nodes[p].double = (nodes[p].double + (nc*nodes[p].single)) % m
    print(nodes[n-1].single)






            
