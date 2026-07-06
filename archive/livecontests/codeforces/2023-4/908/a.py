import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
use directed graph to check which states are reachable by other states
go from destination to previous state, bfs through stages to get longest
chain
if a loop exists, auto pass
"""
class Node:
    def __init__(self):
        self.edges = list()

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


def solve(n,k,ar):
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for i in range(n):
        if ar[i] <= n: #else can never be a fixed point
            pos = i-ar[i]+1
            if pos < 0: pos += n
            nodes[(pos+ar[i]) % n].edges.append(pos) #one way edge
            #print("edge",(pos+ar[i]) % n,pos)
    q = queue()
    q.add((0,0))
    ans = 0
    h = [-1]*n
    h[0] = 0
    while not q.empty():
        x = q.dequeue()
        ans = max(ans,x[1])
        c = x[1]+1
        for u in nodes[x[0]].edges:
            if h[u] == -1: #new node
                h[u] = c
                q.add((u,c))
            elif c != h[u]: return "Yes" #loop found
    #print(ans,h)
    if ans >= k: return "Yes"
    return "No"
    
for _ in range(readint()):
    n,k = readints()
    ar = readar()
    print(solve(n,k,ar))
