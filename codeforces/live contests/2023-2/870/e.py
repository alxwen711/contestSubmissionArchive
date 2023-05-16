import sys
#import queue
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
each model's beauty vals are a vector
if vec a completely exceeds vec b (ai > bi for all i), then parentage found
determine maximum value by downwards traversal (bfs, readd nodes if higher found)
.discard to remove from set
"""

class Node:
    def __init__(self,val,m):
        self.val = val
        self.ans = 0
        self.children = 0
        self.parents = list()
        self.ar = [0]*m

    #def add(self,x):
    #    self.children.add(x)


class queue:
    def __init__(self):
        self.q = list()
        self.pt = 0
        self.l = 0
        
    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l

def nodeList(n: int,v,m) -> list[Node]:
    ar = list()
    for i in range(n):
        ar.append(Node(v[i],m))
    return ar

m,n = readints()
v = readar()
nodes = nodeList(n,v,m)

for i in range(m):
    br = readar()
    for j in range(n):
        nodes[j].ar[i] = br[j]

def cm(ar,br,n):
    for snth in range(n):
        if ar[snth] >= br[snth]: return False
    return True

root = [1]*n
for a in range(n-1):
    for b in range(a+1,n):
        # cmp node[a] node[b]
        if cm(nodes[a].ar,nodes[b].ar,m): # a < b
            root[a] = 0
            nodes[a].children += 1
            nodes[b].parents.append(a)
        elif cm(nodes[b].ar,nodes[a].ar,m): # b < a
            root[b] = 0
            nodes[b].children += 1
            nodes[a].parents.append(b)

q = queue()
for c in range(n):
    if root[c] == 1:
        q.add(c)

best = 0        
for nthnh in range(n):
    x = q.dequeue()
    no = nodes[x]
    cc = no.val + no.ans
    if cc > best: best = cc
    for ii in no.parents:
        if cc > nodes[ii].ans: nodes[ii].ans = cc
        nodes[ii].children -= 1
        if nodes[ii].children == 0: q.add(ii)
print(best)
