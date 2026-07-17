import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
only 1 edge in each graph needs to be the same, and both nodes
must have some sort of parity to reach it
graph may not be a tree meaning that parity may always be possible
cost = difference in node indices

maybe just try moving all nodes in a dp sense?

use a*?
"""


for _ in range(readint()):
    n,a,b = readints()
    nodea = list()
    for _ in range(n):
        tmp = {}
        nodea.append(tmp)
    nodeb = list()
    for _ in range(n):
        tmp = {}
        nodeb.append(tmp)
    for _ in range(readint()):
        x,y = readints()
        nodea[x-1][y-1] = 1
        nodea[y-1][x-1] = 1
    for _ in range(readint()):
        x,y = readints()
        nodeb[x-1][y-1] = 1
        nodeb[y-1][x-1] = 1
    d = {}
    d[(a-1,b-1)] = 0
    h = [(0,a-1,b-1)]
    flag = False
    searched = {}
    while len(h) != 0:
        state = heappop(h)
        cost,na,nb = state[0],state[1],state[2]
        if na == nb:
            for ii in nodea[na].keys():
                if nodeb[nb].get(ii) == 1:
                    print(cost)
                    flag = True
                    break
            if flag: break
        if searched.get((na,nb)) == None:
            searched[(na,nb)] = 1
            for aa in nodea[na].keys():
                for bb in nodeb[nb].keys():
                    if d.get((aa,bb),5000000) > (cost+abs(aa-bb)):
                        d[(aa,bb)] = cost+abs(aa-bb)
                        heappush(h,(cost+abs(aa-bb),aa,bb))
    if not flag: print(-1)
