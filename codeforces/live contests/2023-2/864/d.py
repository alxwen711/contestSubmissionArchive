import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
How to do 2 operations in less than O(n) time
1 operation -> store importance values
generate initial sums from bottom up
on rotation, x is parent
parent is parent-x
num of nodes in parent drops by x's subtree
num of nodes in x is parent subtree
can represent children in a heap, (most children, lowest id)
2 operation:
adjusting importance value is simple, only x and child will have changes
for x, pop largest child
for child, add new subtree x as child
for parent, x's subtree child node has its id swapped with child, then manual heap
operation??
note for parents, their subtree size and importance does not change
"""


def comp(a,b):
    if a[0] < b[0]: return True
    elif a[0] == b[0] and a[1] < b[1]: return True
    return False

class node:
    def __init__(self,ID,val):
        self.id = ID
        self.val = val
        self.parent = -1
        self.leaf = True
        self.subsize = 1
        self.importance = val
        self.children = [] #heap?
        #init values, not needed later
        self.ichild = list()
        self.depth = 0

    def initchildren(self,nl):
        a,b = 0,0
        for i in range(len(self.ichild)):
            bb = nl[self.ichild[i]]
            a += bb.importance
            b += bb.subsize
            heappush(self.children,(-bb.subsize,bb.id))
        self.importance = a + self.val
        self.subsize = b+1

    def rotate(self,nl):
        p = nl[self.parent]
        ct = heappop(self.children)
        c = nl[ct[1]]
        c.subsize = self.subsize
        self.subsize += ct[0]
        #adjust importance
        ti = c.importance
        c.importance = self.importance
        self.importance -= ti


        #change children/parents
        heappush(c.children,(-self.subsize,self.id))
        c.parent,self.parent = self.parent,c.id
        #parent node adjustments
        g = p.children.index((-c.subsize,self.id))
        p.children[g] = (-c.subsize,c.id)
        while g != 0:
            pg = (g-1)//2
            if comp(p.children[g],p.children[pg]):
                p.children[g],p.children[pg] = p.children[pg],p.children[g]
                g = pg
            else: break

        
n,m = readints()
ar = readar()
nodes = list()
nodes.append("potato")
for i in range(n):
    nodes.append(node(i+1,ar[i]))
edges = {}
for j in range(n-1):
    a,b = readints()
    if edges.get(a) == None: edges[a] = list()
    if edges.get(b) == None: edges[b] = list()
    edges[a].append(b)
    edges[b].append(a)

#det hiearchy
h = [0]*(n+1)
st = [1]
h[1] = 1
while len(st) != 0:
    x = st.pop()
    for v in edges[x]:
        if h[v] == 0:
            h[v] = 1
            st.append(v)
            nodes[x].leaf = False
            nodes[v].parent = x
            nodes[v].depth = nodes[x].depth+1
            nodes[x].ichild.append(v)

#build up from bottom layer
br = list()
for ii in range(1,n+1):
    br.append((nodes[ii].depth,ii))
br.sort()
for jj in range(n):
    x = nodes[-jj-1]
    if not x.leaf:
        x.initchildren(nodes)

#test here if needed
"""
for iii in range(1,n+1):
    print(iii,"node stats")
    print(nodes[iii].parent,nodes[iii].depth,nodes[iii].importance)
"""

for s in range(m):
    t,x = readints()
    if t == 1: print(nodes[x].importance)
    else: #rotate hell with x
        if len(nodes[x].children) != 0:
            nodes[x].rotate(nodes)


