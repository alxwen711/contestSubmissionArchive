import sys
from heapq import *
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if 1 and 5 are disconnected, inf
max time is time before hitting n in graph
"""

class Node:
    def __init__(self,ID):
        self.ID = ID
        self.connected = {}

    def add(self,x,y):
        self.connected[x] = y

    
def nodeList(n: int) -> list[Node]:
    ar = list()
    ar.append(None)
    for i in range(1,n+1):
        ar.append(Node(i))
    return ar

def edge(a,b,c):
    a.add(b.ID,c)
    b.add(a.ID,c)


n,m = readints()
nodes = nodeList(n)
for snth in range(m):
    a,b,c = readints()
    edge(nodes[a],nodes[b],c)

ans = list()
hit = [0]*n
hit[0] = 1
t = 0
entries = []
#setup 1 first
for i in nodes[1].connected.keys():
    heappush(entries,(t+nodes[1].connected[i],i))

while len(entries) != 0:
    c = heappop(entries)
    nn = c[1]
    tt = c[0]
    if hit[nn-1] == 0: #valid new node
        ans.append((deepcopy(hit),tt-t))
        t = tt
        hit[nn-1] = 1
        if nn == n: break
        for j in nodes[nn].connected.keys():
            heappush(entries,(t+nodes[nn].connected[j],j))

if hit[n-1] == 0: print("inf")
else:
    print(t,len(ans))
    #print(ans)
    for k in ans:
        #print(k[0])
        #v = "".join(k[0])
        print(*k[0],sep="",end=" ")
        print(k[1])
