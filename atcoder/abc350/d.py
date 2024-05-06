import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
determine how many are connected with each other for maximal edge count
subtract this from current number of edges
"""

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.edges = list()
        self.hit = 0

n,m = readints()
ar = list()
for i in range(n):
    ar.append(Node(i))
for j in range(m):
    a,b = readints()
    a -= 1
    b -= 1
    ar[a].edges.append(b)
    ar[b].edges.append(a)
ans = -m
for k in range(n):
    if ar[k].hit == 0:
        br = [k]
        ar[k].hit = 1
        score = 1
        while len(br) != 0:
            x = br.pop()
            for l in ar[x].edges:
                if ar[l].hit == 0:
                    ar[l].hit = 1
                    br.append(l)
                    score += 1
        ans += (score*score-score)//2
print(ans)
