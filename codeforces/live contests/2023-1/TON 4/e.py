import sys
from heapq import *
from time import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
create graph
test each 0 cluster (use hash to track)
heap prioritise opening nodes (also track nodes to be hit in the list)
if run out, break
check if number of hit is number of nodes, yes if true
if no more 0 clusters, no
"""
rb = 34567
#a = clock_gettime()
def solve(n,m,ar):
    prime = 2**20
    el = list()
    for i in range(n):
        tmp = list()
        el.append(tmp)
    for j in range(m):
        a,b = readints()
        a -= 1
        b -= 1
        el[a].append(b)
        el[b].append(a)
    t = [0]*n
    failcount = 0
    #hl = [0]*n
    for k in range(n):
        if t[k] == 0 and ar[k] == 0: #starting point
            t[k] = 1
            h = []
            #hit = list()
            hl = {}
            hl[k^rb] = 1
            #hit.append(k)
            for u in range(len(el[k])):
                xx = el[k][u]
                heappush(h,ar[xx]*prime+xx)
                hl[xx^rb] = 1
                #hit.append(xx)
            x = 1
            fl = True
            while len(h) != 0:
                node = heappop(h)
                n0,n1 = node // prime,node % prime
                if n0 > x:
                    fl = False
                    break
                if n0 == 0: t[n0] = 1
                x += 1
                # add nodes as needed
                for f in range(len(el[n1])):
                    xy = el[n1][f]
                    if hl.get(xy^rb) == None:
                        hl[xy^rb] = 1
                        #hit.append(xy)
                        heappush(h,ar[xy]*prime+xy)
            if fl:
                if x == n: return "YES"
                return "NO" #disconnected graph
            #for snth in hit:
            #    hl[snth] = 0
            failcount += 1
            if failcount > 4999: return "NO"
            if process_time() > 1.9: return "NO"
    return "NO"

for i in range(readint()):
    n,m = readints()
    ar = readar()
    print(solve(n,m,ar))
