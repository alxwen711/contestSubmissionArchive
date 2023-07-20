import sys
from heapq import *
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def total(ar,x): #determine sum of first x vals
    # ar is bin sparse array
    ans = 0
    for i in range(len(ar)):
        if x % 2 == 1: ans += ar[i][x-1]
        x //= 2
    return ans

n,m,q = readints()
s = input()

# log st/ed points for each substring

st = {}
ed = {}
for i in range(m):
    a,b = readints()
    a -= 1
    b -= 1
    if st.get(a) == None: st[a] = list()
    if ed.get(b) == None: ed[b] = list()
    st[a].append(i)
    ed[b].append(i)

# determine priority for each chr
h = []
ar = list()
used = [1]*m
for j in range(n):
    # add in st pts
    if st.get(j) != None:
        for nn in st[j]: heappush(h,nn) # does single line for loop work?
    # get lowest
    if len(h) != 0: ar.append((h[0],j))
    # mark ends
    if ed.get(j) != None:
        for kk in ed[j]: used[kk] = 0
    # remove until valid
    while len(h) != 0:
        if used[h[0]] == 0: heappop(h)
        else: break
ar.sort()

# log priorities, create bintable
br = list()
priority = [-1]*n
for k in range(len(ar)):
    priority[ar[k][1]] = k
    br.append(int(s[ar[k][1]]))
#print(br)
#print(priority)
dr = list()
one = 0
for nth in range(n):
    if s[nth] == "1": one += 1
    dr.append(int(s[nth]))
cr = list()
cr.append(deepcopy(br)) #len 1 sums, len 2 sums, len 3 sums
while len(cr[-1]) != 1:
    tmp = list()
    for v in range(len(cr[-1])//2):
        tmp.append(cr[-1][v*2]+cr[-1][v*2+1])
    cr.append(tmp)
#print(cr)
# process queries
for l in range(q):
    x = readint()
    x -= 1
    p = priority[x]
    dr[x] = dr[x] ^ 1
    if p != -1: #adjust bintable
        inc = 1
        if cr[0][p] == 1: inc = -1
        one += inc
        for snth in range(len(cr)):
            if p >= len(cr[snth]): break
            cr[snth][p] += inc
            p //= 2
    else:
        if dr[x] == 0: one -= 1
        else: one += 1
    tt = min(one,len(cr[0]))
    print(tt-total(cr,tt)) # 5,6,2,3,7,8
    #print(cr)
