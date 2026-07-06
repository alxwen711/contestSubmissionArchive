import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
add in connections from lowest to highest cost,
continue until fully connected

onion?
"""

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.parent = -1 
        self.size = 1 # technically only relevant if head of tree
        self.time = 0 # time added to another node?
 
 
def getpath(nodes,x):
    ar = list()
    c = x
    while c != -1:
        ar.append(c)
        c = nodes[c].parent
    return ar
 
def ct(nodes,ar,br): #determine connection time
    d = {} #log by index
    for i in range(len(ar)):
        d[ar[i]] = i
    #compare b path until reaching
    ans = -1
    for j in range(len(br)):
        if d.get(br[j]) != None: #found connection, rest of path is same to root
            for k in range(d[br[j]]-1,-1,-1):
                ans = max(ans,nodes[ar[k]].time)
            return ans
        ans = max(ans,nodes[br[j]].time)
    return -1 #no connection

def solve():
    n,q = readints()
    nodes = ["nop"]
    for i in range(1,n+1):
        nodes.append(Node(i))
    for j in range(1,q+1):
        t,a,b = readints()
        if t == 2:
            if a == b: print(0)
            else:
                ar = getpath(nodes,a)
                br = getpath(nodes,b)
                print(ct(nodes,ar,br))
        else: # merge tree heads
            while nodes[a].parent != -1:
                a = nodes[a].parent
            while nodes[b].parent != -1:
                b = nodes[b].parent
            if a != b: #else already connected
                if (nodes[a].size > nodes[b].size) or (nodes[a].size == nodes[b].size and a < b): #merge b to a
                    nodes[b].parent = a
                    nodes[b].time = j
                    nodes[a].size += nodes[b].size
                else: #merge a to b
                    nodes[a].parent = b
                    nodes[a].time = j
                    nodes[b].size += nodes[a].size
def getHead(nodes,x):
    h = x
    while nodes[h].parent != -1:
        h = nodes[h].parent
    return h

n,m = readints()
q = list()
for ii in range(m):
    k,c = readints()
    ar = readar()
    q.append([c,k,ii,ar])
q.sort()

nodes = ["nop"]
for i in range(1,n+1):
    nodes.append(Node(i))

ans = 0
edges = n-1
for j in range(m):
    cost = q[j][0]
    k = q[j][1]
    ar = q[j][3]
    for c in range(k-1):
        na,nb = ar[0],ar[c+1]
        a,b = getHead(nodes,na),getHead(nodes,nb)
        if a != b: #else already connected
            if (nodes[a].size > nodes[b].size) or (nodes[a].size == nodes[b].size and a < b): #merge b to a
                nodes[b].parent = a
                nodes[a].size += nodes[b].size
                ans += cost
                edges -= 1
            else: #merge a to b
                nodes[a].parent = b
                nodes[b].size += nodes[a].size
                ans += cost
                edges -= 1
    if edges == 0: break
if edges == 0: print(ans)
else: print(-1)
