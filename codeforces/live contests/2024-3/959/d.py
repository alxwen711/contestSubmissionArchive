import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
first edge is divisible by 1, then 2,3,4...

is it always possible?

how to choose order of edges? (most to least restrictive?)

get remainders of each value
for each remainder group, determine any two nodes not currently connected
connect them, repeat until done
"""
class Node:
    def __init__(self,i,v):
        self.val = v
        self.i = i
        self.parent = -1
        self.size = 1

def getParent(nodes,x):
    ans = x
    while nodes[ans].parent != -1:
        ans = nodes[ans].parent
    return ans

for _ in range(readint()):
    n = readint()
    ar = readar()
    nodes = list()
    ans = list()
    for i in range(n):
        nodes.append(Node(i,ar[i]))

    # determine edges
    for a in range(n-1,0,-1):
        d = {}
        for ii in range(n):
            v = ar[ii] % a
            if d.get(v) == None: d[v] = list()
            d[v].append(ii)
        na,nb = -1,-1
        for r in range(a):
            if d.get(r) != None:
                for e in range(1,len(d[r])):
                    pa,pb = getParent(nodes,d[r][0]),getParent(nodes,d[r][e])
                    if pa != pb:
                        na = d[r][0]
                        nb = d[r][e]
                        ans.append((na+1,nb+1))
                        # connect nodes pa/pb
                        if nodes[pa].size > nodes[pb].size or (nodes[pa].size == nodes[pb].size and nodes[pa].i < nodes[pb].i):
                            nodes[pb].parent = pa
                            nodes[pa].size += nodes[pb].size
                        else:
                            nodes[pa].parent = pb
                            nodes[pb].size += nodes[pa].size
                        break
            if na != -1: break
    print("YES")
    ans.reverse()
    for i in ans:
        print(i[0],i[1])
