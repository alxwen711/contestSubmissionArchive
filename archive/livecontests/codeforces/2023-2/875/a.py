import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
"""
top value is one
track edge that created each one

"""

class Node:
    def __init__(self,ID,val = 0):
        self.ID = ID
        self.val = val
        self.connected = list()
        self.parent = None
        self.edge = -1

    def add(self,x):
        self.connected.append(x)


for i in range(readint()):
    n = readint()
    d = list()
    for snth in range(n+1):
        tmp = list()
        d.append(tmp)
    ar = {}
    for j in range(n-1):
        a,b = readints()
        #if d.get(a) == None: d[a] = list()
        #if d.get(b) == None: d[b] = list()
        d[a].append(b)
        d[b].append(a)
        if a < b: ar[a*n+b] = j
        else: ar[b*n+a] = j
    ar[-1] = 99999999999999
    nodes = list()
    nodes.append(98348)
    for k in range(1,n+1):
        nodes.append(Node(k))
    q = [1]
    h = [1]*(n+1)
    h[1] = 0
    while len(q) != 0:
        x = q.pop()
        br = d[x]
        v = nodes[x].val
        tmp = ar[nodes[x].edge]
        for m in br:
            if h[m] == 1: # new node
                bb = nodes[m]
                ac = min(x,m)*n+max(x,m)
                h[m] = 0
                q.append(m)
                bb.parent = x
                bb.edge = ac
                bb.val = v
                if ar[bb.edge] < tmp: bb.val += 1
    ans = 0
    for nn in range(1,n+1):
        ans = max(ans,nodes[nn].val)
    print(ans)

                
    
