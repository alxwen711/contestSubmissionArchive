import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
tree structure probably means r/b lines are possible
2-colouring to find all edges to colour in

example gives node colours as RBRB

must connect a R with a B

also cannot be adjacent already

this should give a list of all moves that are made in the game
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.colour = -1

n = readint()
nodes = list()
for _ in range(n+1):
    nodes.append(Node())

for _ in range(n-1):
    a,b = readints()
    nodes[a].edges[b] = 1
    nodes[b].edges[a] = 1

nodes[1].colour = 0
q = [1]
while len(q) != 0:
    x = q.pop()
    for k in nodes[x].edges.keys():
        if nodes[k].colour == -1:
            nodes[k].colour = nodes[x].colour ^ 1
            q.append(k)
movelist = list()
for a in range(1,n):
    for b in range(a+1,n+1):
        if nodes[a].edges.get(b) == None and nodes[a].colour != nodes[b].colour:
            movelist.append((a,b))
movesmade = {}
m = len(movelist)
if m % 2 == 0:
    print("Second",flush=True)
    x,y = readints()
    movesmade[(x,y)] = 1
else:
    print("First",flush=True)
index = 0
for _ in range((m+1)//2):
    while movesmade.get(movelist[index]) != None:
        index += 1
    s = str(movelist[index][0])+" "+str(movelist[index][1])
    print(s,flush=True)
    movesmade[movelist[index]] = 1
    index += 1
    x,y = readints()
    movesmade[(x,y)] = 1
    



            
    
