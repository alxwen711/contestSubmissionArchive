import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
shortest to longest?
then pull every single dfs?

python really is shit with tuples huh
"""
mv = 99999999999999999
class Node:
    def __init__(self):
        self.edges = {}
        self.size = 1
        self.parent = -1

#al = [0]*20
#bl = [0]*20
def connect(nodes,a,b):
    pa,pb = a,b
    #al[0] = pa
    #bl[0] = pb
    #ac,bc = 1,1
    while nodes[pa].parent != -1:
        pa = nodes[pa].parent
        #al[ac] = pa
        #ac += 1
    while nodes[pb].parent != -1:
        pb = nodes[pb].parent
        #bl[bc] = ba
        #bc += 1
    if pa == pb: return False
    if nodes[pa].size > nodes[pb].size or (nodes[pa].size == nodes[pb].size and pa < pb):
        nodes[pa].size += nodes[pb].size
        nodes[pb].parent = pa
    else:
        nodes[pb].size += nodes[pa].size
        nodes[pa].parent = pb
    return True

def encode(a,b,c):
    return a*100000000+b*10000+c
def decode(x):
    return x//100000000,(x//10000)%10000,x%10000

n = readint()
nodes = list()
for _ in range(n):
    nodes.append(Node())

edges = list()
for i in range(n):
    ar = readar() # n - i - 1 vals here
    for j in range(n-i-1):
        edges.append(encode(ar[j],i,i+j+1))

edges.sort()

check = list()
for e in edges:
    c,pa,pb = decode(e)
    if connect(nodes,pa,pb):
        nodes[pa].edges[pb] = c
        nodes[pb].edges[pa] = c
    else: check.append(e)

# find ALL of the distances via DFS
dfs = list()

for a in range(n):
    q = list()
    d = [mv]*n
    d[a] = 0
    q.append(a)
    while len(q) != 0:
        xx = heappop(q)
        c,x = xx//10000,xx % 10000
        if d[x] == c:
            for u in nodes[x].edges.keys():
                nc = nodes[x].edges[u]+c
                if d[u] > nc:
                    heappush(q,nc*10000+u)
                    d[u] = nc
    dfs.append(d)

ans = "Yes"
for cc in check:
    a,b,c = decode(cc)
    if dfs[b][c] != a:
        ans = "No"
        break
print(ans)

