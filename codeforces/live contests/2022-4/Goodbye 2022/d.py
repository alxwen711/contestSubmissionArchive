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


def cycles(c,d,l):
    cycle = 0
    h = [1]*len(c)
    for w in range(len(d)):
        if h[w] == 1:
            cycle += 1
            h[w] = 0
            endpt = c[w]
            loc = w
            cv = d[loc]
            while cv != c[w]:
                choices = l[cv]
                if len(choices) != 2: return -1 #broken cycle case
                nloc = choices[0]
                if nloc == loc: nloc = choices[1]
                h[nloc] = 0
                if cv == c[nloc]: cv = d[nloc]
                else: cv = c[nloc]
                loc = nloc
    return cycle
                
"""
def solve(n,a,b):
    ans = 1
    hit = {}
    emp = [0]*n
    q = queue()
    d = list()
    for snthsnth in range(n+1):
        tmp = list()
        d.append(tmp)
    #check x x cases
    for i in range(n):
        d[a[i]].append(i)
        if a[i] == b[i]:
            if hit.get(a[i]) == None:
                q.add(a[i])
                hit[a[i]] = 1
                ans = (ans * n) % 998244353
                emp[i] = 1
            else: return 0
        else: d[b[i]].append(i)
    #check h y cases
    #print(d)
    while not q.empty():
        x = q.dequeue()
        #print(x)
        for j in range(len(d[x])):
            if emp[d[x][j]] == 0:
                #print(d[x])
                emp[d[x][j]] = 1
                if a[d[x][j]] != x:
                    if hit.get(a[d[x][j]]) != None: return 0
                    q.add(a[d[x][j]])
                    hit[a[d[x][j]]] = 1
                if b[d[x][j]] != x:
                    if hit.get(b[d[x][j]]) != None: return 0
                    q.add(b[d[x][j]])
                    hit[b[d[x][j]]] = 1
    
    
    #find remaining pair states
    cr = list()
    dr = list()
    l = {}
    index = 0
    for f in range(n):
        if emp[f] == 0:
            cr.append(a[f])
            dr.append(b[f])

    #cr,dr = rmdup(cr,dr)
            if l.get(a[f]) == None: l[a[f]] = list()
            if l.get(b[f]) == None: l[b[f]] = list()
            l[a[f]].append(index)
            l[b[f]].append(index)
            index += 1
    #count cycles
    cc = cycles(cr,dr,l)
    if cc == -1: return 0
    for snth in range(cc):
        ans = (ans*2) % 998244353
    return ans
"""

def solve(n,a,b):
    ans = 1
    hit = {}
    emp = [0]*n
    q = queue()
    d = list()
    for snthsnth in range(n+1):
        tmp = {}
        d.append(tmp)
    for i in range(n):
        d[a[i]][i] = 1
        d[b[i]][i] = 1
    for j in range(n+1):
        d[j] = list(d[j].keys())
        if len(d[j]) == 1: #single case
            q.add(j)
    #remove all single value cases

    #remove x x cases?

    #use queue to keep track of indices to remove, if empty, *2 and choose one randomly
            

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    print(solve(n,ar,br))
