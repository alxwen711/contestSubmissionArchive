import sys
from copy import deepcopy

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
if multiple are assigned,
then assign similar for max efficiency
note: this is NOT full greed project wise
4 2
15 10 10 10
15 30
above would fail by greedy allocation of projects

could use bit mask to hit one at a time on each round,
elim sub optimal cases, make sure for duplicate values
they are traversed IN ORDER

how does this help with
20 20
1 2 3 ... 20
1 2 3 ... 20 (but shuffled)

at most there is C(20,10) states, 184756
go from highest to lowest hash val?

00000011
00000101
00000110?
00001001?
00010010
00100001
"""


class state:
    def __init__(self):
        self.r = 0
        self.ar = list()

def assign(ar,ptr,x):
    y = 1
    for snth in range(ptr-1,-1,-1):
        if y*ar[snth] >= x: return snth
        y += 1
    return -1

n,m = readints()
ar = readar()
er = list()
for iii in range(n):
    er.append((ar[iii],iii+1))
er.sort()
fr = list()
for jjj in range(n):
    fr.append(er[jjj][1])

ar.sort()
br = readar()
d = {}
d[0] = state()
d[0].r = n
#print(d)

for i in range(m):
    e = {}
    for a in d.keys():
        v = 1
        ptr = d[a].r
        prev = -1 #last unadded
        for j in range(m):
            if v & a == 0 and prev != br[j]: #add new
                xv = v | a
                np = assign(ar,ptr,br[j])
                if np != -1: #actually possible
                    if e.get(xv) == None: #create new
                        e[xv] = state()
                        e[xv].r = np
                        e[xv].ar = deepcopy(d[a].ar)
                        e[xv].ar.append(j)
                    elif e[xv].r < np: #replace new
                        e[xv].r = np
                        e[xv].ar = deepcopy(d[a].ar)
                        e[xv].ar.append(j)
                prev = br[j] 
            v *= 2
    d = e
    #print(d)

if d.get(2**m-1) == None: print("NO")
else:
    print("YES")
    #print(d[2**m-1].ar) #need to run this exact case after
    ptr = n
    dr = list()
    for b in d[2**m-1].ar:
        cr = list()
        ptr -= 1
        cr.append(ar[ptr])
        while cr[-1]*len(cr) < br[b]:
            ptr -= 1
            cr.append(ar[ptr])
        dr.append(cr)
    #print(dr)
    while ptr != 0:
        ptr -= 1
        dr[-1].append(ar[ptr])
    #translate values
    index = 0
    for g in range(len(dr)-1,-1,-1):
        for hh in range(len(dr[g])):
            dr[g][hh] = fr[index]
            index += 1
        dr[g].append(len(dr[g]))
        dr[g].reverse()
    #print(dr)
    for why in d[2**m-1].ar:
        print(*dr[why])

