import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
given the size of branches under a node, want to split as evenly as possible
start from children nodes and queue upwards
reverse bfs order, push branch sizes upwards
"""

class node:
    def __init__(self,ID):
        self.ID = ID
        self.children = list()
        self.parent = -1
        self.cs = list()

def optimal(ar,x):
    n = x//2+1
    dp = set() #array setup is faster, lmao
    dp.add(0)
    for i in ar:
        tmp = set()
        for j in dp:
            tmp.add(j)
            if j+i < n: tmp.add(i+j)
        dp = tmp
    mv = max(dp)    
    return mv*(x-mv)
        

n = readint()
ar = readar()

nodes = list()

for i in range(n):
    nodes.append(node(i))

for j in range(n-1):
    nodes[j+1].parent = ar[j]-1
    nodes[ar[j]-1].children.append(j+1)

bfs = [0]
pt = 0
while pt != n:
    for fol in nodes[bfs[pt]].children:
        bfs.append(fol)
    pt += 1
    
bfs.reverse()

ans = 0
for k in bfs:
    no = nodes[k]
    s = sum(no.cs)+1
    if len(no.cs) == 2: ans += no.cs[0]*no.cs[1]
    elif len(no.cs) > 2:
        ans += optimal(no.cs,s-1) #divide as evenly as possible
    nodes[no.parent].cs.append(s)

print(ans)
