import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine what nodes unlock other nodes

starting state will have a set of unlockable nodes

for each step afterwards, determine how many previous sets could
have led there

0,0,0,1,0,0,0,0
0,0,0,1,1,0,0,0
0,0,0,1,1,1,3,3

there can be multiple, add those as additional requisites

is minimum requirement a valid restriction?

possible this was idea, from hints this involves rooted tree
at node n (since it's never removed)
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.req = -1
        self.deg = 0

def create_sparse(n):
    ar = list()
    tmp = [0]*n
    ar.append(tmp)
    while len(ar[-1]) != 1:
        tmp = [0]*(len(ar[-1])//2)
        ar.append(tmp)
    return ar

def update(ar,i,v):
    index = i
    for j in range(len(ar)):
        if len(ar[j]) == index: break
        ar[j][index] = (ar[j][index]+v) % 998244353
        index //= 2

def query(ar,li,ri):
    l,r = li,ri
    ans = 0
    for i in range(len(ar)):
        if l > r: break
        if l % 2 == 1:
            ans = (ans + ar[i][l]) % 998244353
            l += 1
        if r % 2 == 0:
            ans = (ans + ar[i][r]) % 998244353
            r -= 1
        l //= 2
        r //= 2
    return ans

for _ in range(readint()):
    n = readint()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
        nodes[a].deg += 1
        nodes[b].deg += 1
    # initial passthrough to get starting value
    maxleaf = -1
    q = list()
    for i in range(n):
        if nodes[i].deg == 1:
            maxleaf = i
            q.append(i)
    
    # construct the requirements?
    for j in range(n):
        cr = list(nodes[j].edges.keys())
        cr.sort()
        if len(cr) == 1:
            nodes[j].req = cr[0]
        else:
            nodes[j].req = cr[-2]
        
    # run the sparse scuff
    ans = create_sparse(n)
    update(ans,maxleaf,1)
    for u in range(maxleaf+1,n):
        mv = nodes[u].req
        mmv = 9999999999999999
        for lll in nodes[u].edges.keys():
            mmv = min(lll,nodes[lll].req)
        mv = max(mv,mmv)
        incremental = query(ans,mv+1,n-1)
        update(ans,u,incremental)
    print(max(1,ans[0][n-1]))
    #print(ans[0])
            
