import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
from each node, what is the furthest distance?
choose a node and find furthest from there, should be leaf, call this x
find furthest from x, call second node y, track distances from x,
longest is full dist
bfs from y, if lower distance replace
for a node, connected until dist-val
all possible x values start with 0, then do a bfs from there
union set ties in x and y
"""

class Node:
    def __init__(self,i):
        self.ID = i
        self.edges = list()
        self.v1 = -1
        self.v2 = -1
        self.v3 = -1
        
    def add(self,x):
        self.edges.append(x)

class queue:
    def __init__(self,limit=100000):
        self.q = list()
        self.pt = 0
        self.l = 0
        self.memRefresh = limit

    def add(self,x) -> None:
        self.q.append(x)
        self.l += 1

    def dequeue(self):
        if self.empty(): return None 
        x = self.q[self.pt]
        self.pt += 1
        #check if memory needs to be refreshed
        if self.pt == self.memRefresh:
            self.pt = 0
            self.l -= self.memRefresh
            self.q = self.q[self.memRefresh:]
        return x

    def top(self):
        if self.empty(): return None
        return self.q[self.pt]

    def length(self) -> int:
        return self.l - self.pt

    def empty(self) -> bool:
        return self.pt == self.l

		



n = readint()
ar = list()
ar.append(0)
for i in range(n):
    ar.append(Node(i))
for j in range(n-1):
    a,b = readints()
    ar[a].add(b)
    ar[b].add(a)
    
q = queue()
height = [-1]*(n+1)
for k in range(1,n+1):
    if len(ar[k].edges) == 1:
        height[k] = 0
        q.add(k)

while not q.empty():
    x = q.dequeue()
    xv = height[x]
    # add new nodes
    for kk in range(len(ar[x].edges)):
        v = ar[x].edges[kk]
        if height[v] == -1:
            height[v] = xv + 1
            q.add(v)

#print(height)
ao = max(height)
dist = ao*2
if height.count(ao) > 1: dist += 1

h = [0]*n
for u in range(1,n+1):
    h[dist-height[u]] += 1
ans = [1]
vvv = 1
for snth in range(n-1):
    vvv += h[snth+1]
    if vvv > n: vvv = n
    ans.append(vvv)
print(*ans)


"""
ar[1].v1 = 0
q = queue()
q.add(1)
longest = list()
l = -1
while not q.empty():
    x = q.dequeue()
    xv = ar[x].v1
    if xv > l: # track longest
        l = xv
        longest = [x]
    else: longest.append(x)
    # add new nodes
    for k in range(len(ar[x].edges)):
        v = ar[x].edges[k]
        if ar[v].v1 == -1:
            ar[v].v1 = xv + 1
            q.add(v)

end1 = longest[0] # first endpoint
ar[end1].v2 = 0
q.add(end1)
longest2 = list()
l2 = -1
while not q.empty():
    x = q.dequeue()
    xv = ar[x].v2
    if xv > l2: # track longest
        l2 = xv
        longest2 = [x]
    else: longest2.append(x)
    # add new nodes
    for k in range(len(ar[x].edges)):
        v = ar[x].edges[k]
        if ar[v].v2 == -1:
            ar[v].v2 = xv + 1
            q.add(v)
longest3 = longest + longest2
longest3 = list(set(longest3))
dist = l2
for o in longest3:
    q.add(o)
    ar[o].v3 = 0

while not q.empty():
    x = q.dequeue()
    xv = ar[x].v3
    # add new nodes
    for kk in range(len(ar[x].edges)):
        v = ar[x].edges[kk]
        if ar[v].v3 == -1:
            ar[v].v3 = xv + 1
            q.add(v)
h = [0]*n
for u in range(1,n+1):
    h[dist-(ar[u].v3)] += 1
ans = [1]
vvv = 1
for snth in range(n-1):
    vvv += h[snth+1]
    if vvv > n: vvv = n
    ans.append(vvv)
print(*ans)
#print(h)
"""
