import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
calculate all initial damage, determine who dies
from there a chain reaction should occur,
re-calc adjacent damage, if dead on recalc +1,
then re-calc adjacents until <=1 left
"""
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

def solve(n,ar,dr):
    la = list()
    ra = list()
    for i in range(n):
        la.append(i-1)
        ra.append(i+1)
    ra[-1] = -1
    tr = [-1]*n
    q = queue()
    for j in range(n):
        q.add((j,0))
    ded = list()
    while not q.empty():
        x = q.dequeue()
        #check if already set
        index,v = x[0],x[1]
        if tr[index] == -1: #not set
            val = 0
            if la[index] != -1: val += ar[la[index]]
            if ra[index] != -1: val += ar[ra[index]]
            if val > dr[index]: #ded
                tr[index] = v
                ded.append(index)
                
        if q.empty(): #update ded list
            ded.sort()
            for ind in ded:
                if la[ind] != -1:
                    ra[la[ind]] = ra[ind]
                    if tr[la[ind]] == -1:
                        q.add((la[ind],v+1))
                if ra[ind] != -1:
                    la[ra[ind]] = la[ind]
                    if tr[ra[ind]] == -1:
                        q.add((ra[ind],v+1))
            ded = list()
    ans = [0]*n
    for ii in tr:
        if ii != -1: ans[ii] += 1
    print(*ans)
    
for _ in range(readint()):
    n = readint()
    ar = readar()
    dr = readar()
    solve(n,ar,dr)
