import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
current degree of the nodes coloured black has something
n = 4 <- not all 4 edge starts can be completed
2222 passes
1223 fails

the answer is always either max or max-1
assume that all empty graphs with a divisor of 3 can pass
3,4,6,7,9,10,12,13...
other ones are remainder 1

n=5 works, ALL empty cases should pass?

there must be some way to convert the remaining into a cycle

greedily remove edges?
"""
class Node:
    def __init__(self):
        self.edges = list()
        self.pt = 0
        self.deg = 0

def solve(n,nodes): #remove edges by lowest next indexer
    eu = {}
    i = 0
    while i != n:
        while nodes[i].pt != nodes[i].deg:
            if eu.get((i,nodes[i].edges[nodes[i].pt])) != None:
                nodes[i].pt += 1
            else: break
        if nodes[i].pt != nodes[i].deg: # start new cycle attempt
            pts = {}
            pts[i] = 1
            #pts[nodes[i].deg[nodes[i].pt]] = 1
            eu[(i,nodes[i].edges[nodes[i].pt])] = 1
            eu[(nodes[i].edges[nodes[i].pt],i)] = 1
            start = i
            current = nodes[i].edges[nodes[i].pt]
            while pts.get(current) == None:
                pts[current] = 1
                # find new edge
                while nodes[current].pt != nodes[current].deg:
                    if eu.get((current,nodes[current].edges[nodes[current].pt])) != None:
                        nodes[current].pt += 1
                    else: break
                if nodes[current].pt == nodes[current].deg:
                    #print(eu)
                    return False
                eu[(current,nodes[current].edges[nodes[current].pt])] = 1
                eu[(nodes[current].edges[nodes[current].pt],current)] = 1
                current = nodes[current].edges[nodes[current].pt]
            if current != start:
                #print(eu)
                return False
        else: i += 1
    #print(eu)
    return True
n,m = readints()
nodes = list()
for _ in range(n):
    nodes.append(Node())

for _ in range(m):
    a,b = readints()
    a -= 1
    b -= 1
    nodes[a].edges.append(b)
    nodes[b].edges.append(a)
    nodes[a].deg += 1
    nodes[b].deg += 1
for snth in range(n):
    nodes[snth].edges.sort()
if not solve(n,nodes): print((n*n-n)//2-1)
else: print((n*n-n)//2)
