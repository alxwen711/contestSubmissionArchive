import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
26 nodes in the graph
each two chr string is an edge, self edges are possible but
are represented by nodes that must be touched
edges are one way
find some way to walk on the graph the fewer times and hit every edge

maximum leaves in a subtree?

traverse each node, then from largest to smallest tree

2nd case above still has issues

probably alternate idea is to take head nodes (no paths going in)
determine all of the possible branches that are "optimal"
optimal means they traverse as many nodes as possible and end on a leaf

there might be only 26 of these at most?
actually probably not, 1-way bijection of a 13-13 split can create 169

but if optimized, then bitset include/exclude could complete
"""

class Node:
    def __init__(self):
        self.edges = list()
        self.used = False
        
nodes = list()
for _ in range(26):
    nodes.append(Node())

n = readint()
for _ in range(n):
    s = readin()
    a,b = ord(s[0])-65,ord(s[1])-65
    nodes[a].edges.append(b)
    nodes[a].used = True
    nodes[b].used = True

treesets = list()
for i in range(26):
    if nodes[i].used:
        hit = [0]*26
        nodelist = [i]
        hit[i] = 1
        leaves = 0
        q = [i]
        print("build",i)
        while len(q) != 0:
            x = q.pop()
            if len(nodes[x].edges) == 0:
                leaves += 1
                print(x)
            else:
                for j in nodes[x].edges:
                    if hit[j] == 0:
                        hit[j] = 1
                        q.append(j)
                        nodelist.append(j)
        if leaves == 0: leaves += 1
        treesets.append((-len(nodelist),i,leaves,nodelist))
        print(treesets[-1])
treesets.sort()
hit = [1]*26
ans = 0
for t in treesets:
    if hit[t[1]] == 1:
        #print(t)
        ans += t[2]
        for snth in t[3]:
            hit[snth] = 0
print(ans)
#print(treesets)


        
