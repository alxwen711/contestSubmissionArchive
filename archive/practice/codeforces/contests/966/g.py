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
doing nothing is an option, then binary searching the answer
seems reasonable here

if you have options to ride the bus or walk, always ride
there are cases where it is more optimal to wait for a call
to end, then ride the bus

for now assume that you can ride a bus starting at t2

you can take bus up to t1 too apparently
"""


class Node:
    def __init__(self):
        self.best = 999999999999999999
        self.costs = list()
        
def f(n,nodes,t,ps,pe,x):
    nodes[0].best = x
    for snth in range(1,n):
        nodes[snth].best = 999999999999999999
    h = [x*1000000]
    while len(h) != 0:
        entry = heappop(h)
        cost,index = entry//1000000,entry%1000000
        if index == n-1: return cost <= t
        if nodes[index].best == cost: # optimal case, continue
            for e in nodes[index].costs:
                
                # walk cost
                wc = cost+e[2]

                # compute bus cost
                bc = max(cost,pe)+e[1]
                if cost < ps and cost+e[1] <= ps:
                    bc = cost+e[1]

                # update if needed
                mc = min(wc,bc)
                if mc < nodes[e[0]].best and mc <= t:
                    nodes[e[0]].best = mc
                    heappush(h,mc*1000000+e[0])
    return False
anslist = list()
for _ in range(readint()):
    n,m = readints()
    t,ps,pe = readints() # time to finish, phone start, phone end
    nodes = list()
    for _ in range(n):
        nodes.append(Node())
    for _ in range(m):
        u,v,x,y = readints()
        u -= 1
        v -= 1
        nodes[u].costs.append((v,x,y))
        nodes[v].costs.append((u,x,y))
        
    low = 0
    high = t
    while high-low > 1:
        mid = (low+high)//2
        if f(n,nodes,t,ps,pe,mid): low = mid
        else: high = mid
    # t is actually impossible since n >= 2 and all roads need 1 unit of time min
    if f(n,nodes,t,ps,pe,low): anslist.append(low)
    else: anslist.append(-1)
sys.stdout.write("\n".join(map(str,anslist)))

    
