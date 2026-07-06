import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

class Node:
    def __init__(self,val):
        self.val = val
        self.connected = list()

    def add(self,x):
        self.connected.append(x)

def nodeList(n: int) -> list[Node]:
    ar = list()
    ar.append(None)
    for i in range(1,n+1):
        ar.append(Node(i))
    return ar

def edge(a: Node, b: Node):
    a.add(b)
    b.add(a)

for i in range(readint()):
    d = input() #dummy line
    n,k = readints()
    if n < 3:
        print(0)
        if n == 2: d = input() #dummy line
    else:
        ar = nodeList(n)
        freq = [0]*(n+1)
        for j in range(n-1):
            u,v = readints()
            edge(ar[u],ar[v])
            freq[u] += 1
            freq[v] += 1
        vals = [0]*(n+1)
        r = 1
        ntc = list()
        for kk in range(n+1):
            if freq[kk] == 1: #leaf
                vals[kk] = 1
                ntc.append(ar[kk])
        while len(ntc) != 0:
            r += 1
            nntc = list()
            for _ in range(len(ntc)):
                x = ntc[_]
                for f in range(len(x.connected)):
                    y = x.connected[f].val
                    if freq[y] != 0: freq[y] -= 1
                    if freq[y] == 1: #new leaf
                        vals[y] = r
                        nntc.append(ar[y])
                freq[x.val] = 0
            ntc = nntc
        r += 1
        for why in range(1,n+1):
            if vals[why] == 0: vals[why] = r
        #print(vals)
        ans = 0
        for m in range(n+1):
            if vals[m] > k: ans += 1
        print(ans)
    

