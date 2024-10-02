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
edges in the graph form a 1 to n circle, + m other edges
up to 50 extra edges
compute number of possible paths of length k
with no extra edges only 1 path (1,2,3,4,5,6...n)
every time an edge is hit, considered as a possible split
possibly around 10000000 dp cases?

when hitting the start point of an edge, options are to
either +1 or to move to where-ever it goes next, can speed
up process to move directly to the next point

unsure if number of potential points at a given moment could cause problems
you are able to merge setups together if they happen at the same step and pos

pretty sure tracking the number of positions here
potentially at each step is causing n**2 blowup
"""

n,m,steplimit = readints()
nextsection = [-1]*n
d = {}
starts = list()
for _ in range(m):
    x,y = readints()
    x -= 1
    y -= 1
    if (x + 1) % n != y: # else this edge is pointless
        starts.append(x)
        if d.get(x) == None: d[x] = list()
        d[x].append(y)
if m == 0: print(1)
else:
    starts.sort()
    for i in range(m-1):
        for j in range(starts[i],starts[i+1]):
            nextsection[j] = starts[i+1]
    if len(starts) == 1:
        nextsection = [starts[0]]*n
    else:
        for l in range(starts[0]):
            nextsection[l] = starts[0] 
        for k in range(starts[-1],n):
            nextsection[k] = starts[0]
    q = [(0,0,1)] # (steps taken,position,num of ways)
    ans = 0
    mod = 998244353
    while len(q) != 0:
        x = heappop(q)
        #print(x)
        steps,pos,v = x[0],x[1],x[2]
        while len(q) != 0:
            if q[0][0] == steps and q[0][1] == pos:
                v += q[0][2]
                heappop(q)
            else: break
        if steps >= steplimit: ans = (ans+v) % mod
        else:
            if d.get(pos) == None: # move until reaching next point
                move = min((nextsection[pos]-pos) % n,steplimit-steps)
                heappush(q,(steps+move,(pos+move) % n,v))
            else: # either move to next point or transport
                move = min((nextsection[pos]-pos) % n,steplimit-steps)
                heappush(q,(steps+move,(pos+move) % n,v))
                for i in d[pos]:
                    if d.get(i) != None:
                        heappush(q,(steps+1,i,v))
                    else:
                        np = nextsection[i]
                        move = min((np-i) % n + 1, steplimit-steps)
                        heappush(q,(steps+move,(i+move-1) % n,v))
    print(ans)
