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
e.py but with more memory optimazation attempts/shenanigans
(ngl kinda getting ridiculous)

setup an edgelist and track start/end pointers for where each node is
since edges will only ever be removed, this should be okay;
removal only needs the degree count to go down, edges don't actually
have to be destroyed

actually maybe just tracking deg and using lists instead is easier
and now there is WA10. Okay so now I really have no clue what happened here
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
    deg = array("i",[0]*n)
    edges = list()
    vc = array("i",[0]*n)
    for _ in range(n):
        edges.append(list())
    for _ in range(n-1):
        a,b = readints()
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
        deg[a] += 1
        deg[b] += 1

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
        if deg[v] == 1 and ancestor[v] != -1:
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
        if snth not in ds and deg[snth] == 1:
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
        deg[xp] -= 1
        if deg[xp] == 1 and xp not in ds:
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



        
