import sys

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
    def __init__(self,ID,val):
        self.ID = ID
        self.val = val
        self.ans = 0
        self.children = 0
        self.parents = list()
        self.ar = list()

#    def add(self,x):
#        self.children += 1

    
def nodeList(n: int,v) -> list[Node]:
    ar = list()
    for i in range(n):
        ar.append(Node(i,v[i]))
    return ar

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

m,n = readints()
v = readar()
nodes = nodeList(n,v)

for i in range(m):
    br = readar()
    for j in range(n):
        nodes[j].ar.append(br[j])

def cmv(ar,n):
    ans = 0
    for iii in range(n):
        ans <<= 30
        ans += ar[iii]
    return ans

def cm(ar,br,n):
    for snth in range(n):
        if ar[snth] >= br[snth]: return False
    return True
"""
root = [1]*n
for a in range(n-1):
    for b in range(a+1,n):
        # cmp node[a] node[b]
        if cm(nodes[a].ar,nodes[b].ar,m): # a < b
            root[a] = 0
            nodes[a].add(b)
            nodes[b].parents.append(a)
        elif cm(nodes[b].ar,nodes[a].ar,m): # b < a
            root[b] = 0
            nodes[b].add(a)
            nodes[a].parents.append(b)
"""
def mv(a,m,n):
    for hh in range(n):
        if a[hh] == m[hh]: return True
    return False

# determine hiearchcial list first
# list hiearchy can just be sorted by first value
cr = list()
for vv in range(n):
    cr.append((nodes[vv].ar[0],vv))
cr.sort()

mr = list()
for aaa in range(m):
    lowest = 87342985732985
    for bbb in range(n):
        lowest = min(lowest,nodes[bbb].ar[aaa])
    mr.append(lowest)

#print(cr)
root = [0]*n
for a in range(n):
    ni = cr[a][1] # node index testing
    nnnn = nodes[ni]
    if not mv(nnnn.ar,mr,m):
        qq = queue()
        for tt in range(n):
            if root[tt] == 1: qq.add(tt)
        while not qq.empty():
            x = qq.dequeue()
            aa = nodes[x]
            if cm(aa.ar,nodes[ni].ar,m): #direct child
                root[x] = 0
                #nodes[x].add(ni)
                aa.children += 1
                nodes[ni].parents.append(x)
            else:
                for htn in nodes[x].parents: # try parents
                    qq.add(htn)
    root[ni] = 1

q = queue()
for c in range(n):
    if root[c] == 1:
        q.add(c)

best = 0        
while not q.empty():
    x = q.dequeue()
    no = nodes[x]
    cc = no.val + no.ans
    best = max(best,cc)
    for ii in no.parents:
        vvv = nodes[ii]
        vvv.ans = max(vvv.ans,cc)
        vvv.children -= 1
        if vvv.children == 0: q.add(ii)
print(best)
