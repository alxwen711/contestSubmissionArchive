import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
restriction cases:
ai + aj >= 0 (o = 1)
ai + aj < 0 (o = 2)

easy case: n <= 1000, all pairs specified
hard case: n <= 200000, not all pairs specified
use some sort of DAG?

easy case: each value +/- is known, use +/- pair comps
possible to have a 4 chain of contradiction

hard case: only note the edges first

determine what node variants are forced?
assume everything is positive first
upon finding a - edge, at least one of these must be negative

if there exists insufficient information (no individual node is specified +/-),
try both scenarios, intentionally start on a node with conflicting edges to
get some sort of chain force??? (then what happens if multiple of these exist)
"""

class Node:
    def __init__(self):
        self.deg = 0
        self.val = 0
        self.edges = list()

for _ in range(readint()):
    n,m = readints()
    chain = list()
    for _ in range(n):
        tmp = [0]*n
        chain.append(tmp)
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        o,i,j = readints()
        i -= 1
        j -= 1
        chain[i][j] = o
    flag = False
    for a in range(n-1):
        for b in range(a+1,n):
            sa,sb = chain[a][a],chain[b][b]
            if sa == sb:
                if sa != chain[a][b]:
                    flag = True
                    break
            else:
                if chain[a][b] == sa: #a magnitude > b magnitude
                    nodes[b].edges.append(a)
                    nodes[a].deg += 1
                else:
                    nodes[a].edges.append(b)
                    nodes[b].deg += 1                    
        if flag: break
    if flag:
        print("NO")
        continue
    else:
        # try to construct the answer
        q = list()
        for u in range(n):
            if nodes[u].deg == 0: q.append(u)
        ans = [0]*n
        flag = True
        for sn in range(n):
            if sn == len(q):
                flag = False
                break
            index = q[sn]
            if chain[index][index] == 1: ans[index] = sn+1
            else: ans[index] = -sn-1
            for v in nodes[index].edges:
                nodes[v].deg -= 1
                if nodes[v].deg == 0: q.append(v)
        if flag:
            print("YES")
            print(*ans)
        else:
            print("NO")
    
