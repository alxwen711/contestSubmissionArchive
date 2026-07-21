import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
each level has to be processed individually
track the minimum and maximum value stored in each node
for each level, do the following:
if it is a leaf node, keep as is (no problem)
else, 2 conditions:
1. maxchild - minchild + 1 = number of children values
2. there has to exist a valid cyclic shift (iterate through list)
if both conditions hold, update the parent node with new min/max

i'm pretty sure looping cases (n-1,n,1,2) in a parent node should be impossible
"""

class Node:
    def __init__(self,v):
        self.parent = -1
        self.children = list()
        self.depth = 0
        self.minval = 9999999
        self.maxval = -9999999
        self.valcount = 0
        if v != 0:
            self.minval = v
            self.maxval = v
            self.valcount = 1

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    nodes = list()
    for ii in range(n):
        nodes.append(Node(br[ii]))
    for i in range(n-1):
        nodes[i+1].parent = ar[i]-1
        nodes[ar[i]-1].children.append(i+1)
    # update the depths
    q = list()
    for t in nodes[0].children:
        q.append(t)
    sv = 0
    while len(q) != 0:
        x = q.pop()
        nodes[x].depth = nodes[nodes[x].parent].depth+1
        sv = max(sv,nodes[x].depth)
        for r in nodes[x].children:
            q.append(r)
    d = {}
    for a in range(n):
        xd = nodes[a].depth
        if d.get(xd) == None: d[xd] = list()
        d[xd].append(a)

    # start solving each node from deepest up
    ans = "YES"
    for level in range(sv,-1,-1):
        for b in d[level]:
            setnode = nodes[b]
            if len(setnode.children) != 0:
                # figure out the children min max cases
                minp,maxp = 99999999999,-9999999999
                leaves = 0
                for p in setnode.children:
                    minp = min(minp,nodes[p].minval)
                    maxp = max(maxp,nodes[p].maxval)
                    leaves += nodes[p].valcount
                if maxp-minp+1 != leaves:
                    ans = "NO"
                    #print(minp,maxp,leaves)
                    break
                # then figure out the cyclical setup
                startingindex = -1
                nv = len(setnode.children)
                for ii in range(nv):
                    if nodes[setnode.children[ii]].minval == minp:
                        startingindex = ii
                        break
                if startingindex == -1: # should not be possible but just in case
                    ans = "NO"
                    break
                for l in range(nv-1):
                    lp = setnode.children[(startingindex+l) % nv]
                    rp = setnode.children[(startingindex+l+1) % nv]
                    if nodes[lp].maxval + 1 != nodes[rp].minval:
                        ans = "NO"
                        #print(lp,rp)
                        break
                if ans == "NO": break
                # assume above is valid, now update the parent
                setnode.minval = minp
                setnode.maxval = maxp
                setnode.valcount = leaves
            
        if ans == "NO": break

    print(ans)
    

    


    
