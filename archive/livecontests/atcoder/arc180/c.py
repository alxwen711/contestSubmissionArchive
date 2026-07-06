import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
n is at most 100, O(n^4) is possible

given low sums the graphing idea might work?

graphing method collapses due to 1 0 1 -2 being impossible in sample 2
splitting nodes into prev/sum -> how to compute correct sum?
cannot use hashing to track what arrays have been hit (will cause collision)
"""


n = readint()
ar = readar()

def debug(nodes):
    for i in nodes.keys():
        print("Node "+str(i)+":")
        print(nodes[i].count)
        print("Sums:",list(nodes[i].vals.keys()))
        print("Previous vals:",list(nodes[i].hit.keys()))
        print()
    print()
    print()
    print()

class Node:
    def __init__(self):
        self.count = 0
        self.vals = {}
        self.hit = {}

m = 1000000007
nodes = {}
nodes[0] = Node()
nodes[0].vals[0] = 1
nodes[0].count = 1

for x in ar:
    newnodes = {}
    for i in nodes.keys():
        for j in nodes[i].vals.keys():
            # do not add to sum, x
            if newnodes.get(x) == None: newnodes[x] = Node()
            if newnodes[x].hit.get(i) == None:
                newnodes[x].hit[i] = 1
                newnodes[x].count = (newnodes[x].count+nodes[i].count) % m
            if newnodes[x].vals.get(j) == None: newnodes[x].vals[j] = 0
            newnodes[x].vals[j] = (newnodes[x].vals[j]+nodes[i].vals[j]) % m
            # add to sum, x
            v = x + j
            if newnodes.get(v) == None: newnodes[v] = Node()
            if newnodes[v].hit.get(i) == None:
                newnodes[v].hit[i] = 1
                newnodes[v].count = (newnodes[v].count+nodes[i].count) % m
            newnodes[v].vals[v] = 1
    nodes = newnodes
    debug(nodes)

ans = 0
for f in nodes.keys():
    ans = (ans+nodes[f].count) % m
    
print(ans)
