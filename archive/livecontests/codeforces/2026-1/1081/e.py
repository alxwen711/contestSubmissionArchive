import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
5 second time limit, n <= 10**6

confirm if a configuration could exist (only even counts)

first attempt: just make arbritary "good" swaps until no further?
if no more good swaps, guess a neutral
if no more neutrals, impossible
order of swaps does not matter

assuming each node has even degree, this graph can be decomposed
into an arbritary number of cycles?

If this is the case, then in each cycle the edge setup can be
recorded, then flips can be determined

just use greedy?
"""

class Node:
    def __init__(self):
        self.edges = {}

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    nodes = {}
    counts = [0]*(n+1)
    for i in range(n):
        if nodes.get(ar[i]) == None: nodes[ar[i]] = Node()
        if nodes.get(br[i]) == None: nodes[br[i]] = Node()
        if nodes[ar[i]].edges.get(br[i]) == None: nodes[ar[i]].edges[br[i]] = 0
        if nodes[br[i]].edges.get(ar[i]) == None: nodes[br[i]].edges[ar[i]] = 0
        nodes[ar[i]].edges[br[i]] += 1
        nodes[br[i]].edges[ar[i]] += 1
        counts[ar[i]] += 1
        counts[br[i]] += 1
    flag = True
    for i in counts:
        if i % 2 == 1:
            flag = False
            print(-1)
            break
    if flag: # there is a solution
        edgelist = list()
        for j in range(n+1):
            if counts[j] != 0: # there exists a loop here
                path = True
                index = j
                while path or index != j:
                    key,value = 0,0
                    while value <= 0:
                        key,value = nodes[index].edges.popitem() # just get anything out
                    counts[index] -= 1
                    counts[key] -= 1
                    if value != 1:
                        nodes[index].edges[key] = value - 1
                        nodes[key].edges[index] -= 1
                    else:
                        del nodes[key].edges[index]
                    edgelist.append((index,key))        
                    index = key
                    path = False
        d = {}
        for e in edgelist:
            if d.get(e) == None: d[e] = 0
            d[e] += 1
        ans = list()
        for u in range(n):
            if d.get((ar[u],br[u]),0) != 0: d[(ar[u],br[u])] -= 1
            else:
                ans.append(u+1)
                d[(br[u],ar[u])] -= 1
        print(len(ans))
        print(*ans)
        
