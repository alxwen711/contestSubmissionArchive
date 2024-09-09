import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
attempt a 2-colouring, if fails, Alice can win

Bob strategy
label b/w
assign a colour to b and w, at least 1 of the options is usable
if only b or w left, 3rd colour is added to there
again, at least one of the two assigned colours has to be given

Alice strategy
just give 2 colours the entire time?

graph is connected, no need to consider hanging nodes
"""

class Node:
    def __init__(self):
        self.colour = -1
        self.edges = list()

def bob(n,m,nodes):
    print("Bob")
    flush()
    c0,c1 = 0,0
    i0,i1 = 1,1

    # colour first node
    a,b = readints()
    print(1,a)
    flush()
    if nodes[1].colour == 0:
        i0 += 1
        while i0 <= n:
            if nodes[i0].colour == 1: i0 += 1
            else: break
        while i1 <= n:
            if nodes[i1].colour == 0: i1 += 1
            else: break
        c0 = a
    else:
        i1 += 1
        while i1 <= n:
            if nodes[i1].colour == 0: i1 += 1
            else: break
        while i0 <= n:
            if nodes[i0].colour == 1: i0 += 1
            else: break
        c1 = a
        
    for _ in range(n-1):
        cols = readar()
        if cols[0] == -1: return -1 # something screwed up
        a,b = cols[0],cols[1]
        if i0 > n: # only 1 colour nodes left
            c = a
            if c == c0: c = b
            print(i1,c)
            i1 += 1
            while i1 <= n:
                if nodes[i1].colour == 0: i1 += 1
                else: break
        elif i1 > n: # only 0 colour nodes left
            c = a
            if c == c1: c = b
            print(i0,c)
            i0 += 1
            while i0 <= n:
                if nodes[i0].colour == 1: i0 += 1
                else: break
        # standard colouring cases
        elif c0 == a:
            print(i0,a)
            i0 += 1
            while i0 <= n:
                if nodes[i0].colour == 1: i0 += 1
                else: break
        elif c0 == b:
            print(i0,b)
            i0 += 1
            while i0 <= n:
                if nodes[i0].colour == 1: i0 += 1
                else: break
        elif c1 == a:
            print(i1,a)
            i1 += 1
            while i1 <= n:
                if nodes[i1].colour == 0: i1 += 1
                else: break
        elif c1 == b:
            print(i1,b)
            i1 += 1
            while i1 <= n:
                if nodes[i1].colour == 0: i1 += 1
                else: break
        # assign new colour cases
        elif c0 == 0:
            c0 = a
            print(i0,c0)
            i0 += 1
            while i0 <= n:
                if nodes[i0].colour == 1: i0 += 1
                else: break
        else:
            c1 = a
            print(i1,c1)
            i1 += 1
            while i1 <= n:
                if nodes[i1].colour == 0: i1 += 1
                else: break
        #print("index vals:",i0,i1)
        flush()
    return 0

def solve(n,m):
    nodes = [0]
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        a,b = readints()
        nodes[a].edges.append(b)
        nodes[b].edges.append(a)
    q = [1]
    nodes[1].colour = 0
    while len(q) != 0:
        x = q.pop()
        for y in nodes[x].edges:
            if nodes[y].colour == -1:
                nodes[y].colour = nodes[x].colour ^ 1
                q.append(y)

    # 2-colouring check
    for i in range(1,n+1):
        for j in nodes[i].edges:
            if nodes[i].colour == nodes[j].colour: # run Alice strategy
                print("Alice")
                for _ in range(n):
                    print("1 2")
                    flush()
                    response = readar()
                    if response[0] == -1: return -1
                return 0

    # Bob strategy
    return bob(n,m,nodes)

for _ in range(readint()):
    n,m = readints()
    x = solve(n,m)
    if x == -1: break
