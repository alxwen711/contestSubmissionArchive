import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
there appears to be a central point that must be a square
that enables everything else?
the central points are all located at a node with at least degree 3
we then consider their branch sizes

set an arbritary root, then on this root consider degree 3 case if possible
every other node if at least two children, their sizes should be recorded,
then the remaining branch is from parent (ie. n - children sizes - 1)
for each one that is a square number, determine how many ways there are to choose
a point from three unique branches

degree 2 nodes can also work as a square line, in this case one point must
be this square specifically with other two points each from different branches
(this can also be done on degree 3 nodes)
"""

def increment(ar,prefix):
    #print(ar)
    ans = 0
    n = len(ar)
    br = list()
    # pick 2 from ar
    total = prefix[-1]
    for i in ar:
        total -= i
        ans += i*total
        br.append(i*total)
    if n == 2: return ans

    prefix2 = [0]*n
    for j in range(n-2,-1,-1):
        prefix2[j] = prefix2[j+1]+br[j]
    # pick 3 from ar
    for k in range(n-1):
        ans += ar[k]*prefix2[k+1]
    return ans

squares = set()
for i in range(1001):
    squares.add(i*i)
    
class Node:
    def __init__(self,i):
        self.edges = {}
        self.sq = False
        if i in squares: self.sq = True
        self.parent = -1
        self.degree = 0
        self.childrensizes = list()
        self.size = 1
        

for _ in range(readint()):
    n = readint()
    ar = readar()
    nodes = list()
    for i in range(n):
        nodes.append(Node(ar[i]))
    for _ in range(n-1):
        u,v = readints()
        nodes[u-1].edges[v-1] = 1
        nodes[v-1].edges[u-1] = 1
    # root at 0
    q = [0]
    for j in range(n):
        x = q[j]
        for v in nodes[x].edges.keys():
            if nodes[v].parent == -1 and v != 0:
                nodes[v].parent = x
                nodes[x].degree += 1
                q.append(v)
                
    # build upwards from degree 0
    q = list()
    for snth in range(n):
        if nodes[snth].degree == 0: q.append(snth)

    # compute size lists
    for k in range(n-1):
        x = q[k]
        p = nodes[x].parent
        nodes[p].degree -= 1
        if nodes[p].degree == 0: q.append(p)
        nodes[p].size += nodes[x].size
        nodes[p].childrensizes.append(nodes[x].size)

    ans = 0
    # for each square add to answer
    # 0 case is separate
    #print(0,nodes[0].childrensizes)
    if nodes[0].sq and len(nodes[0].childrensizes) >= 2:
        prefix = [0]
        for u in nodes[0].childrensizes:
            prefix.append(prefix[-1]+u)
        ans += increment(nodes[0].childrensizes,prefix)
    for l in range(1,n):
        #print(l,nodes[l].childrensizes)
        if nodes[l].sq and len(nodes[l].childrensizes) >= 1:
            prefix = [0]
            for u in nodes[l].childrensizes:
                prefix.append(prefix[-1]+u)
            nodes[l].childrensizes.append(n-prefix[-1]-1)
            prefix.append(n-1)
            ans += increment(nodes[l].childrensizes,prefix)
    print(ans)



















        
