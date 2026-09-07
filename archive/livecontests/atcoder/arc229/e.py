import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
any node with a 2 and 3 edge can be a split or rejoin point
okay so this isn't troll dfs
"""

class Node:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.one = list()
        self.two = list()
        self.three = list()
        

        
for _ in range(readint()):
    n,m = readints()
    nodes = list()
    for _ in range(n+1):
        nodes.append(Node())
    for _ in range(m):
        a,b,c = readints()
        if c == 1:
            nodes[a].one.append(b)
            nodes[b].one.append(a)
        if c == 2:
            nodes[a].two.append(b)
            nodes[b].two.append(a)
        if c == 3:
            nodes[a].three.append(b)
            nodes[b].three.append(a)
    q = [(1,1)]
    nodes[1].a = 1
    nodes[1].b = 1
    
    while len(q) != 0:
        x = q.pop()
        index,op = x[0],x[1]
        if op == 1: # possible split lines
            for e in nodes[index].one:
                if nodes[e].a == 0 or nodes[e].b == 0:
                    nodes[e].a = 1
                    nodes[e].b = 1
                    q.append((e,1))
            for e in nodes[index].two:
                if nodes[e].a == 0:
                    nodes[e].a = 1
                    if nodes[e].b == 1: q.append((e,1))
                    else: q.append((e,2))
            for e in nodes[index].three:
                if nodes[e].b == 0:
                    nodes[e].b = 1
                    if nodes[e].a == 1: q.append((e,1))
                    else: q.append((e,3))
        elif op == 2 and nodes[index].b == 0:
            for e in nodes[index].two:
                if nodes[e].a == 0:
                    nodes[e].a = 1
                    if nodes[e].b == 1: q.append((e,1))
                    else: q.append((e,2))
        elif op == 3 and nodes[index].a == 0:
            for e in nodes[index].three:
                if nodes[e].b == 0:
                    nodes[e].b = 1
                    if nodes[e].a == 1: q.append((e,1))
                    else: q.append((e,3))
        ans = list()
    for snth in range(1,n+1):
        if nodes[snth].a == 1 and nodes[snth].b == 1:
            ans.append(snth)
    print(len(ans))
    print(*ans)
