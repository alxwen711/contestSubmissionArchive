import sys
from array import array
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
find all k such that there exists diameter a and b (a = b is allowed)
where path a and path b share k edges

the diameter length will be odd
trivially the diameter is one of the k values

choose an arbritary diameter of the tree to branch out from

then each child has two cases, either it is the only diversion segment
or it has to combine with another part to create a two part diversion??

E is also 4 seconds?

determine all leaf nodes that when going up can lead to creation of a diameter
if there is a connection between branches, some sort of additional numeric
internally is possible

so either one or two full length branches can be used
or an internal branch system can be applied

rip timeout

problem tags and discussion are for some reason implying that nnt (fft)
is used here?????

after edits this appears to be correct, but even with various attempts
to improve memory MLE3 is a thing

(lmao)

making an e2 to refactor all this
"""

def dfs(n,edges,dist,parent,ancestor,y):
    for i in range(n):
        dist[i] = -1
        parent[i] = -1
        ancestor[i] = -1
    q = []
    for x in y:
        dist[x] = 0
        q.append(x)
    for j in range(n):
        v = q[j]
        for k in edges[v]:
            if dist[k] == -1:
                dist[k] = dist[v]+1
                parent[k] = v
                ancestor[k] = ancestor[v]
                if ancestor[k] == -1: ancestor[k] = v # use parent instead
                q.append(k)
    

for _ in range(readint()):
    n = readint()
    dist = array("i",[0]*n)
    parent = array("i",[0]*n)
    ancestor = array("i",[0]*n)
    edges = list()
    vc = array("i",[0]*n)
    for _ in range(n):
        edges.append(set())
    for _ in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
        edges[a].add(b)
        edges[b].add(a)

    # find a diameter
    dfs(n,edges,dist,parent,ancestor,[0])
    index = -1
    best = -1
    for u in range(n):
        if dist[u] > best:
            best = dist[u]
            index = u
    dfs(n,edges,dist,parent,ancestor,[index])
    index2 = -1
    best = -1
    for u in range(n):
        if dist[u] > best:
            best = dist[u]
            index2 = u
    diameter = [index2]
    while diameter[-1] != index:
        diameter.append(parent[diameter[-1]])

    # now from this diameter start expanding out
    dfs(n,edges,dist,parent,ancestor,diameter)

    # find nodes in diameter that have a valid extension
    d = {}
    k = len(diameter)-1
    for ii in range(k+1):
        d[diameter[ii]] = min(ii,k-ii)

    validextensions = set()
    validnodes = set()
    for v in range(n):
        if len(edges[v]) == 1 and ancestor[v] != -1:
            if dist[v] == d[ancestor[v]]:
                validextensions.add(ancestor[v])
                validnodes.add(v)
                vc[v] += 1

    ans = array("i",[0]*(k+1))
    ans[k] = 1

    # determine which valid nodes can be pushed upwards
    ds = set(d.keys())
    q = list()
    for snth in range(n):
        if snth not in ds and len(edges[snth]) == 1:
            q.append(snth)
    ptr = 0
    while ptr != len(q):
        x = q[ptr]
        # check if this exact case is usable
        if vc[x] >= 2:
            vc[x] = 1
            ansdist = dist[x]+d[ancestor[x]]
            ans[ansdist] = 1
        xp = parent[x]
        vc[xp] += vc[x]
        edges[xp].remove(x)
        if len(edges[xp]) == 1 and xp not in ds:
            q.append(xp)
        ptr += 1

    # then consider all full branches
    count = {}
    for ve in validextensions:
        dist = d[ve]
        if count.get(dist) == None:
            count[dist] = 0
        count[dist] += 1
        ans[k-dist] = 1

    ohno = list(count.keys())
    ohno.sort()
    for aa in range(len(ohno)-1):
        for bb in range(aa+1,len(ohno)):
            cc = ohno[aa]+ohno[bb]
            ans[k-cc] = 1
    for dd in range(len(ohno)):
        if count[ohno[dd]] > 1:
            ans[k-ohno[dd]-ohno[dd]] = 1
    anslist = [0]
    for snthsnth in range(k+1):
        if ans[snthsnth]:
            anslist[0] += 1
            anslist.append(snthsnth)
    print(*anslist)



        
