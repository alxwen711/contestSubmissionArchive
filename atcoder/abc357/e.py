import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
each one has an outgoing edge
could have multiple incoming edges
every subgraph ends in a cycle?
determine the cycle, set all vals to cycle len
then work backwards up the edges
cycle determination is reasonably possible by
just choosing any node and traversing until dup
"""

class Node:
    def __init__(self):
        self.child = -1
        self.parents = list()
        self.val = 0

n = readint()
nodes = [456]
for _ in range(n):
    nodes.append(Node())

ar = readar()
for i in range(n):
    nodes[i+1].child = ar[i]
    nodes[ar[i]].parents.append(i+1)

for a in range(1,n+1):
    if nodes[a].val == 0: # unexplored subgraph
        d = {}
        br = list()
        index = a
        while d.get(index) == None:
            d[index] = 1
            br.append(index)
            index = nodes[index].child
        # stop at index
        cyclelen = 0
        q = list()
        for b in range(len(br)):
            cyclelen += 1
            if br[-b-1] == index:
                # set up dfs, colour cycle
                for c in range(len(br)-cyclelen,len(br)):
                    nodes[br[c]].val = cyclelen
                    q.append(br[c])        
                break
        while len(q) != 0:
            x = q.pop()
            for e in nodes[x].parents:
                if nodes[e].val == 0:
                    nodes[e].val = nodes[x].val+1
                    q.append(e)
ans = 0
for ji in range(1,n+1):
    ans += nodes[ji].val
print(ans)

            
