import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
e has more solves?
this one track distances, then there is some sort
of greedy by taking a direct child and throwing
it as deep as possible

if there is only one child, then traverse deeper?
always track the best possible throw
"""

class Node:
    def __init__(self,v):
        self.val = v
        self.depth = -1
        self.edges = {}
        self.total = v # sum of subtree
        self.score = 0 # score if root left unchanged
        self.best = 0
        self.md = -1
        self.md2 = -1

def getchildren(nodes,x):
    c = list()
    for u in nodes[x].edges.keys():
        if nodes[u].depth - 1 == nodes[x].depth: c.append(u)
    return c

for _ in range(readint()):
    n = readint()
    ar = readar()
    nodes = ["node"]
    for iii in range(n):
        nodes.append(Node(ar[iii]))
    for _ in range(n-1):
        a,b = readints()
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
    nodes[1].depth = 0
    nodes[1].md = 0
    q = [1]
    for i in range(n):
        x = q[i]
        for d in nodes[x].edges.keys():
            if nodes[d].depth == -1:
                nodes[d].depth = nodes[x].depth + 1
                nodes[d].md = nodes[x].depth + 1
                q.append(d)
    br = list()
    for j in range(1,n+1):
        br.append(10000000*nodes[j].depth+j)
    br.sort()
    br.reverse()
    ans = [0]*n
    for k in range(n):
        x = br[k] % 10000000 # solve node x
        ch = getchildren(nodes,x)
        for c in ch:
            nodes[x].total += nodes[c].total
            nodes[x].score += nodes[c].score+nodes[c].total
            if nodes[c].md > nodes[x].md:
                nodes[x].md2 = nodes[x].md
                nodes[x].md = nodes[c].md
            elif nodes[c].md > nodes[x].md2: nodes[x].md2 = nodes[c].md
        # determine how much score can be increased by
        if len(ch) == 0: ans[x-1] = nodes[x].score # 0
        elif len(ch) == 1:
            nodes[x].best = nodes[ch[0]].best
            ans[x-1] = nodes[x].score+nodes[x].best
        else: # some sort of new best must be possible?
            b = 0
            for c in ch:
                b = max(b,nodes[c].best)
                v = nodes[x].md
                if v == nodes[c].md: v = nodes[x].md2
                diff = v-nodes[c].depth+1
                b = max(b,diff*nodes[c].total)
            nodes[x].best = max(nodes[x].best,b)
            ans[x-1] = nodes[x].score+nodes[x].best
    print(*ans)
    #for iiii in range(1,n+1):
    #    y = nodes[iiii]
    #    print(y.val,y.depth,y.total,y.score,y.best,y.md,y.md2)



        
