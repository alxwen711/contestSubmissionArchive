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
easy scenario: use lt binary to search if possible each time
at most 80000 possible node pairs, this info is usable
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.val = 10000

def trial(nodes,a,b,l):
    nodes[a].val = 0
    qu = [(0,a)]
    while len(qu) != 0:
        tt = heappop(qu)
        t = tt[1]
        if t == b: break
        if tt[0] == nodes[t].val:
            for u in nodes[t].edges.keys():
                vv = nodes[t].val
                if nodes[t].edges[u] > l: vv += 1
                if nodes[u].val > vv:
                    nodes[u].val = vv
                    heappush(qu,(nodes[u].val,u))
    ans = nodes[b].val
    for snth in range(1,len(nodes)):
        nodes[snth].val = 10000
    #print(l,ans)
    return ans

class data:
    def __init__(self,base,bi):
        self.lk = base
        self.li = bi
        self.hk = base
        self.hi = bi
        self.d = {}
        self.d[base] = bi

def getinfo(prev,a,b,k,m):
    if prev.get((a,b)) == None: return 0,m-1
    refdict = prev[(a,b)]
    if refdict.d.get(k) != None: return refdict.d[k],refdict.d[k]
    if k > refdict.hk: return 0,refdict.hi
    if k < refdict.lk: return refdict.li,m-1
    return refdict.hi,refdict.li

def solve():
    n,m,q = readints()
    nodes = [0]
    for _ in range(n):
        nodes.append(Node())
    ed = {}
    for _ in range(m):
        u,v,w = readints()
        nodes[u].edges[v] = w
        nodes[v].edges[u] = w
        ed[w] = 1
    ed = list(ed.keys())
    ed.sort()
    ans = list()
    prev = {}
    for _ in range(q):
        a,b,k = readints()
        if k > 2*m:
            ans.append(ed[0])
            continue
        low,high = getinfo(prev,min(a,b),max(a,b),k,m)
        if low == high:
            ans.append(ed[low])
            continue
        while high-low > 1:
            mid = (low+high)//2
            if k > trial(nodes,a,b,ed[mid]): high = mid
            else: low = mid
        if k > trial(nodes,a,b,ed[low]):
            ans.append(ed[low])
            if prev.get((min(a,b),max(a,b))) == None:
                prev[(min(a,b),max(a,b))] = data(k,low)
            else:
                prev[(min(a,b),max(a,b))].d[k] = low
                if k < prev[(min(a,b),max(a,b))].lk:
                    prev[(min(a,b),max(a,b))].lk = k
                    prev[(min(a,b),max(a,b))].li = low
                if k > prev[(min(a,b),max(a,b))].hk:
                    prev[(min(a,b),max(a,b))].hk = k
                    prev[(min(a,b),max(a,b))].hi = low
        else:
            ans.append(ed[high])
            if prev.get((min(a,b),max(a,b))) == None:
                prev[(min(a,b),max(a,b))] = data(k,high)
            else:
                prev[(min(a,b),max(a,b))].d[k] = high
                if k < prev[(min(a,b),max(a,b))].lk:
                    prev[(min(a,b),max(a,b))].lk = k
                    prev[(min(a,b),max(a,b))].li = high
                if k > prev[(min(a,b),max(a,b))].hk:
                    prev[(min(a,b),max(a,b))].hk = k
                    prev[(min(a,b),max(a,b))].hi = high
    print(*ans)
    
for _ in range(readint()):
    solve()
