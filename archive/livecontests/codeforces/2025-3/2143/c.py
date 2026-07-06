import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
it must always be possible to obtain maximum
"""

class Node:
    def __init__(self):
        self.parent = list()
        self.children = list()
        self.deg = 0

for _ in range(readint()):
    n = readint()
    nodes = [423324432423324324342]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(n-1):
        a,b,c,d = readints()
        if c > d:
            nodes[b].parent.append(a)
            nodes[a].children.append(b)
            nodes[a].deg += 1
        else:
            nodes[a].parent.append(b)
            nodes[b].children.append(a)
            nodes[b].deg += 1
    ans = [0]*n
    q = list()
    cc = 1
    for i in range(1,n+1):
        if nodes[i].deg == 0:
            q.append(i)
            ans[i-1] = cc
            cc += 1
    while len(q) != 0:
        x = q.pop()
        #print(x)
        for ii in nodes[x].parent:
            nodes[ii].deg -= 1
            if nodes[ii].deg == 0:
                q.append(ii)
                ans[ii-1] = cc
                cc += 1
    print(*ans)
