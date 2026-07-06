import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
the graph has no loops (cycles are fine, real nice wording)
the graph may be unconnected

assume basic two colouring?
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.col = -1

for _ in range(readint()):
    n,m = readints()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        a,b = readints()
        a -= 1
        b -= 1
        nodes[a].edges[b] = 1
        nodes[b].edges[a] = 1
    ans = 0
    for i in range(n):
        if nodes[i].col == -1:
            q = [i]
            z,o = 0,0
            nodes[i].col = 0
            flag = True
            while len(q) != 0:
                x = q.pop()
                if nodes[x].col == 0: z += 1
                else: o += 1
                for j in nodes[x].edges.keys():
                    if nodes[j].col == -1:
                        nodes[j].col = nodes[x].col ^ 1
                        q.append(j)
                    elif nodes[j].col == nodes[x].col: flag = False
            if flag: ans += max(z,o)
    print(ans)


                    
