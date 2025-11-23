import sys
from heap import heapq
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())
"""
both opponents will take moves via +score-opppotential
once one type of value is left, both players just take from there

simulate 1 turn for both players
repeat the turns until someone reaches 0 on the number/ -1 scenario

break all ties with the lower option

now there's an indexing problem to recall what nodes are still in existance
use bintable to track what nodes are left in log n time
if two nodes are merged, go to the next higher node and update that somehow

g is asking for power towers mod m, what proportion of power towers converge
to mod m = 1

i forgot where mv (maximum scoring value for the heaps) comes into this
given how long this code is this is better for upsolve (implementation practice)
either i have the right idea and this is just figuring out how to implement
or i've missed something

current rank 1303
"""

class Node:
    def __init__(self,v,f):
        self.low = -3
        self.val = v
        self.freq = f

def bintable(n):
    ar = list()
    tmp = [1]*n
    ar.append(tmp)
    while len(ar[-1]) != 1:
        tmp = [1]*(len(ar[-1])//2)
        ar.append(tmp)
    return ar

def nodequery(y,x,ar): # determine if a node exists
    l = y
    r = x
    for i in range(len(ar)):
        if r < 0: return False
        if l % 2 == 1:
            if ar[i][l]: return True
            l += 1
        if r % 2 == 0:
            if ar[i][r]: return True
            r -= 1
        l //= 2
        r //= 2
    return False

def update(x,ar): # remove a node from existance
    i = x
    for j in range(len(ar)):
        if len(ar[j]) == i: break
        ar[j][i] -= 1
        i //= 2

def getnext(x,ar): # find next lowest node from x still in play
    low = 0
    high = x-1
    while high-low > 1:
        mid = (low+high)//2
        if nodequery(mid,x-1,ar): low = mid
        else: high = mid
    if nodequery(high,x-1,ar): return high
    if nodequery(low,x-1,ar): return low
    return -1 # no lowest node found



hv = 3878414
hv2 = 34343
for _ in range(readint()):
    n = readint()
    existingnodes = bintable(n)
    ar = readar()
    if ar == [1]*n: # in case b never gets a move
        print(n,0)
        continue
    aturn = True
    ascore = 0
    bscore = 0
    amoves = list()
    bmoves = list()
    amove = None
    bmove = None
    d = {}
    keylist = list()
    for e in ar:
        if d.get(e^hv+hv2) == None:
            d[e^hv+hv2] = 0
        d[e^hv+hv2] += 1
        keylist.append(e)
    keylist.sort()
    nodes = list()
    mv = 0
    for ii in keylist:
        nodes.append(Node(ii,d[ii^hv+hv2]))
        mv = max(d[ii^hv+hv2],mv)
    for j in range(len(nodes)-1):
        nodes[j+1].low = nondes[j].val
    # compute all base moves for a
    for s in range(n):
        bs = nodes[s].freq
        if nodes[s].val-1 == nodes[s].low:
            heappush(amoves,(max(mv,nodes[s].freq+nodes[s-1].freq)-bs,s))
    # act on a's move
    ascore += nodes[amoves[0][1]].freq
    nodes[amoves[0][1]].val -= 1
    amove = amoves[0]
    # find next lowest node
    if nodes[amoves[0][1]].val == 0: # done with this node
        update(ar,amoves[0][1]) 
        amove = None
    else:
        nln = getnext(amoves[0][1],existingnodes)
        if nln != -1: # merge nodes
            if nodes[amoves[0][1]].val == nodes[nln].val: 
                nodes[amoves[0][1]].freq += nodes[nln].freq
                nodes[amoves[0][1]].low = nodes[nln].low
                update(nln,ar)
                amove = None
        
