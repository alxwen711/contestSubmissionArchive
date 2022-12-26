import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

#node 1 is the root
#n^2 is impossible, some sort of O(n)
class Node:
    def __init__(self,x):
        self.id = x
        self.edge = {}
        self.parent = None
        self.depth = -1

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

def f(ar,x):
    br = list()
    for i in range(len(x)):
        br.append([ar[x[i]].depth,x[i]])
    br.sort()
    br.reverse()
    hit = {}
    ans = list()
    for j in range(len(br)):
        n = br[j][1]
        if hit.get(n) == None:
            ans.append(n)
            hit[1] = 1
            it = n
            while it != 1:
                hit[it] = 1
                it = ar[it].parent
    return ans

def ff(ar,x,aar):
    ans = list()
    for i in range(len(ar)):
        b = ar[i]
        for j in range(x):
            if aar[b].parent == None:
                break
            b = aar[b].parent
        ans.append(b)
    return ans
            
def e(n,ar):
    ans = 0
    for k in range(len(n)):
        ans += (ar[n[k]].depth*2)
    return ans

n,d = readints()
ar = list()
ar.append(None)
for i in range(n):
    ar.append(Node(i+1))

for j in range(n-1):
    a,b = readints()
    ar[a].edge[b] = 1
    ar[b].edge[a] = 1

anodes = readar()
bnodes = readar()

ar[1].depth = 0
q = queue()
q.add(1)
while not q.empty():
    x = q.dequeue()
    cr = list(ar[x].edge.keys())
    for k in range(len(cr)):
        if ar[cr[k]].depth == -1:
            ar[cr[k]].parent = x
            ar[cr[k]].depth = ar[x].depth+1
            q.add(cr[k])
        
patha = f(ar,anodes[1:])
pathb = f(ar,bnodes[1:])
primea = f(ar,ff(patha,d,ar))
primeb = f(ar,ff(pathb,d,ar))
pa = f(ar,patha+primeb)
pb = f(ar,pathb+primea)

print(e(pa,ar)+e(pb,ar))
"""
for s in range(1,len(ar)):
    print(s,ar[s].depth)
print(patha,pathb,primea,primeb)

track path to the root, can eliminate nodes if they ancestor
go to deep node, back to ancestor, repeat until all nodes touched then root
find apath, then bpath
create a deepest node path
- in order of deepest node
- traverse back to top of tree, switch off any nodes found
- repeat until all deepest nodes found

a' and b' are deepest node paths with d levels of pushing up
answer is min(a+b',b+a')
distance is sum of depths*2
"""

