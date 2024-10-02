import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
count how many edges are kept after each k from 1 to
wherever the longest is (when no more expansions can occur)
go to each node and expand from the node to its children to
get new "leaf" nodes, if cannot expand further, then prune
the actual leaf and dec parent degree by 1, if this causes
parent degree to be 1, it is a branch chain, iteratively
go backwards until returning to root node, where if its
degree is 0, then the process is complete.
after each expansion, record number of edges total
"""

class Node:
    def __init__(self):
        self.deg = 0
        self.edges = list() # do not use parent
        self.parent = -1

def solve(n): # n-1 edges
    nodes = [Node()]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        a,b = readints()
        nodes[a].edges.append(b)
        nodes[b].edges.append(a)
        nodes[a].deg += 1
        nodes[b].deg += 1
    # assign parents
    q = [1]
    while len(q) != 0:
        x = q.pop()
        for i in nodes[x].edges:
            if nodes[i].parent == -1 and i != 1:
                nodes[i].parent = x
                q.append(i)

    # run iterative
    q = [1]
    ans = 0
    edgecount = 0
    while len(q) != 0:
        # check each current leaf node for further expansion
        nq = list()
        for x in q:
            flag = False
            for i in nodes[x].edges:
                if i != nodes[x].parent:
                    flag = True
                    nq.append(i)
                    edgecount += 1
            if not flag: # delete x and any potential chain
                index = x
                while True:
                    nodes[index].deg -= 1
                    nodes[nodes[index].parent].deg -= 1
                    index = nodes[index].parent
                    edgecount -= 1
                    if nodes[index].deg > 1: break
                    elif index == 1 and nodes[index].deg == 1: break
                    elif nodes[1].deg == 0: # deleted ALL edges
                        break
        q = nq
        ans = max(ans,edgecount)
    return n-1-ans

for _ in range(readint()):
    print(solve(readint()))
