import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

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

def solve(n,m,k):
    ar = [-10**20]*n #min vals
    br = [10**20]*n #max vals
    h = [0]*n
    d = [0]*n
    q = queue()
    for j in range(m):
        pos,val = readints()
        d[pos-1] = 1
        ar[pos-1] = val
        br[pos-1] = val
    for t in range(k):
        a,b,c = readints()
        if a > b: a,b = b,a
        a -= 1
        b -= 1
        if h[a] == 0: h[a] = {}
        if h[b] == 0: h[b] = {}
        if h[a].get(b) == None: h[a][b] = c
        else: h[a][b] = min(h[a][b],c)
        if h[b].get(a) == None: h[b][a] = c
        else: h[b][a] = min(h[b][a],c)
        if d[a] == 1 or d[b] == 1: q.add((a,b,c))
    #run bfs?
    while not q.empty():
        x = q.dequeue()
        na = x[0]
        nb = x[1]
        dist = x[2]
        mina = ar[nb]-dist
        maxa = br[nb]+dist
        minb = ar[na]-dist
        maxb = br[na]+dist
        ar[na] = max(ar[na],mina)
        br[na] = min(br[na],maxa)
        ar[nb] = max(ar[nb],minb)
        br[nb] = min(br[nb],maxb)
        if ar[na] > br[na] or ar[nb] > br[nb]: return "NO"
        if d[na] == 0:
            d[na] = 1
            for snth in h[na].keys():
                q.add((na,snth,h[na][snth]))
        if d[nb] == 0:
            d[nb] = 1
            for snthe in h[nb].keys():
                q.add((nb,snthe,h[nb][snthe]))
    return "YES"

        
for i in range(readint()):
    n,m,k = readints()
    print(solve(n,m,k))
