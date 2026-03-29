import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
it's fine until it isn't?
if two sections are completely unconnected and conflict,
flip everything in the smaller setup

every segment's min count needs to be tracked for answer

lmao choke job
"""

class Node:
    def __init__(self):
        self.col = -1
        self.ans = [0,0]
        self.edges = {}
        self.size = 1
        self.parent = -1

def getparent(nodes,a):
    pa = a
    while nodes[pa].parent != -1:
        pa = nodes[pa].parent
    return pa

def connect(nodes,a,b):
    pa,pb = getparent(nodes,a),getparent(nodes,b)
    if pa == pb: return 0
    if nodes[pa].size > nodes[pb].size or (nodes[pa].size == nodes[pb].size and pa < pb):
        nodes[pa].size += nodes[pb].size
        nodes[pb].parent = pa
        return 2
    else:
        nodes[pb].size += nodes[pa].size
        nodes[pa].parent = pb
        return 1
    
def flip(nodes,x):
    a,b = 0,0
    q = [x]
    d = {}
    d[x] = 1
    while len(q) != 0:
        y = q.pop()
        if nodes[y].col == 0:
            a += 1
            nodes[y].col = 1
        else:
            b += 1
            nodes[y].col = 1
        for u in nodes[y].edges.keys():
            if d.get(u) == None:
                d[u] = 1
                q.append(u)
    return a,b

def increment(no,c):
    if min(no.ans) == no.ans[c] and min(no.ans) != max(no.ans): return True

nodes = list()

n,q = readints()
for _ in range(n):
    nodes.append(Node())

ans = 0
flag = False
for _ in range(q):
    u,v = readints()
    u -= 1
    v -= 1
    uc,vc = nodes[u].col,nodes[v].col
    if uc == -1 and vc == -1:
        nodes[u].col = 0
        nodes[v].col = 1
        ans += 1
        nodes[v].parent = u
        nodes[u].size += 1
        nodes[u].ans = [1,1]
    elif uc == -1 and vc != -1:
        nodes[u].col = nodes[v].col ^ 1
        pv = getparent(nodes,v)
        if increment(nodes[pv],nodes[u].col): ans += 1
        nodes[pv].ans[nodes[u].col] += 1
        nodes[u].parent = pv
        nodes[pv].size += 1
    elif vc == -1 and uc != -1:
        nodes[v].col = nodes[u].col ^ 1
        pu = getparent(nodes,u)
        if increment(nodes[pu],nodes[v].col): ans += 1
        nodes[pu].ans[nodes[v].col] += 1
        nodes[v].parent = pu
        nodes[pu].size += 1
    else:
        pu = getparent(nodes,u)
        pv = getparent(nodes,v)
        vv = min(nodes[pu].ans) + min(nodes[pv].ans)
        cv = connect(nodes,u,v) # connected, u is smaller, v is smaller
        if uc == vc:
            if cv == 1: # flip u
                ac,bc = flip(nodes,u)
                ans -= vv
                nodes[pv].ans[0] += nodes[pu].ans[1]
                nodes[pv].ans[1] += nodes[pu].ans[0]
                ans += min(nodes[pu].ans)
            elif cv == 2: # flip v
                ac,bc = flip(nodes,v)
                ans -= vv
                nodes[pu].ans[0] += nodes[pv].ans[1]
                nodes[pu].ans[1] += nodes[pv].ans[0]
                ans += min(nodes[pv].ans)
            else: flag = True
        else:
            if cv == 1: # add u
                ans -= vv
                nodes[pv].ans[0] += nodes[pu].ans[0]
                nodes[pv].ans[1] += nodes[pu].ans[1]
                ans += min(nodes[pu].ans)
            elif cv == 2: # add v
                ans -= vv
                nodes[pu].ans[0] += nodes[pv].ans[0]
                nodes[pu].ans[1] += nodes[pv].ans[1]
                ans += min(nodes[pv].ans)            
            
    nodes[u].edges[v] = 1
    nodes[v].edges[u] = 1
    if flag: print(-1)
    else: print(ans)
