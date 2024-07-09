import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
determine the "level" of a node
if it is not high enough, choose the
node with lowest level, increment it to fufill parent reqs
ans += inc*level

can inc higher levels if the sum is low enough (does not incur added cost)

bottom up construction has potential recursive issues I'm still unsure of 
"""
class Node:
    def __init__(self,val):
        self.parent = -1
        self.children = list()
        self.val = val
        self.s = 0
        self.level = -1
        
for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    nodes = list()
    # construct tree
    for i in range(n):
        nodes.append(Node(ar[i]))
    for j in range(n-1):
        nodes[j+1].parent = br[j]-1
        nodes[br[j]-1].children.append(j+1)

    # compute level and overall order setup
    q = list()
    for k in range(n):
        if len(nodes[k].children) == 0:
            q.append(k)
            nodes[k].level = 1
    for snth in range(n):
        x = nodes[q[snth]].parent
        if x != -1:
            if nodes[x].level == -1:
                q.append(x)
                nodes[x].level = nodes[q[snth]].level+1
    for tt in range(n):
        for u in nodes[tt].children:
            nodes[tt].s += nodes[u].val
    # in order of q, determine if parent setups are correct
    ans = 0
    for a in range(n):
        x = q[a]
        if x != 0: # not root
            if nodes[nodes[x].parent].cleared == 0: # clear it out
                s = 0
                for ii in nodes[nodes[x].parent].children:
                    s += nodes[ii].val
                if nodes[nodes[x].parent].val > s:
                    ans += (nodes[nodes[x].parent].val-s)*nodes[x].level
                    nodes[x].val += (nodes[nodes[x].parent].val-s)
                nodes[nodes[x].parent].cleared = 1
    print(ans)
