import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

class Node:
    def __init__(self):
        self.deg = 0
        self.children = list()
        self.parent = -1
        self.wide = False
        self.depthscore = 1

"""
compute a depth score, if single child reset depth to 0
total is the sum of depths and node count?
inversely build depth, then if there are multiple children take second highest
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for i in range(n-1):
        nodes[i+1].parent = ar[i]-1
        nodes[ar[i]-1].deg += 1
        nodes[ar[i]-1].children.append(i+1)
        
    q = list()
    for j in range(n):
        if nodes[j].deg == 0:
            q.append(j)
        if nodes[j].deg >= 2:
            nodes[j].wide = True
    ans = n
    for k in range(n):
        x = q[k]
        if x != 0:
            nodes[nodes[x].parent].deg -= 1
            nodes[nodes[x].parent].depthscore = max(nodes[nodes[x].parent].depthscore,nodes[x].depthscore+1)
            if nodes[nodes[x].parent].deg == 0: q.append(nodes[x].parent)
        if nodes[x].wide:
            ar = list()
            for u in nodes[x].children:
                ar.append(nodes[u].depthscore)
            ar.sort()
            ans += ar[-2]
    print(ans)

            
