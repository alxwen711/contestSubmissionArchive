import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
two colour with parents
assume the graph is connected
"""

class Node:
    def __init__(self):
        self.edges = list()
        self.parent = -1
        self.col = -1

for _ in range(readint()):
    n,m = readints()
    nodes = [0]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        a,b = readints()
        nodes[a].edges.append(b)
        nodes[b].edges.append(a)
    q = [1]
    nodes[1].col = 0
    ans = list()
    ans1 = list()
    ans2 = list()
    while len(q) != 0:
        x = q.pop()
        for u in nodes[x].edges:
            if nodes[u].col == -1:
                nodes[u].col = nodes[x].col ^ 1
                nodes[u].parent = x
                q.append(u)
            elif nodes[u].col == nodes[x].col: # cycle found, must have u-x
                ans1.append(x)
                while ans1[-1] != 1:
                    ans1.append(nodes[ans1[-1]].parent)

                ans2.append(u)
                while ans2[-1] != 1:
                    ans2.append(nodes[ans2[-1]].parent)

                # determine where these chains match
                d = {}
                for iii in range(len(ans1)):
                    d[ans1[iii]] = iii

                for kk in range(len(ans2)):
                    if d.get(ans2[kk]) != None:
                        ans = list()
                        for snth in range(d[ans2[kk]]+1):
                            ans.append(ans1[snth])
                        for why in range(kk-1,-1,-1):
                            ans.append(ans2[why])
                        break
                break
        if len(ans) != 0: break
        
    if len(ans) == 0: print(-1)
    else:
        print(len(ans))
        print(*ans)
        

                
