import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
number of subarrays with an inversion value of k
use sparse table

consider widest and narrowest possible cases
"""

def query(sparse,li,ri):
    r = ri
    l = li
    ans = 0
    for i in range(len(sparse)):
        if l > r: return ans
        if l % 2 == 1:
            ans += sparse[i][l]
            l += 1
        if r % 2 == 0:
            ans += sparse[i][r]
            r -= 1
        l //= 2
        r //= 2
    return ans

def update(sparse,xi,v):
    x = xi
    for i in range(len(sparse)):
        if x == len(sparse[i]): break
        sparse[i][x] += v
        x //= 2

n,k = readints()
ar = readar()

sparse = list()
tmp = [0]*n
sparse.append(tmp)
while len(sparse[-1]) != 1:
    tmp = [0]*(len(sparse[-1])//2)
    sparse.append(tmp)

invcount = 0
lp = 0
ansa = [-1]*n # narrowest
ansb = [-1]*n # widest

for i in range(n):
    v = ar[i]
    invcount += query(sparse,v,n-1)
    update(sparse,v-1,1)
    while invcount >= k:
        if lp > i: break
        if invcount == k: ansa[i] = lp
        update(sparse,ar[lp]-1,-1)
        invcount -= query(sparse,0,ar[lp]-1)
        lp += 1

sparse = list()
tmp = [0]*n
sparse.append(tmp)
while len(sparse[-1]) != 1:
    tmp = [0]*(len(sparse[-1])//2)
    sparse.append(tmp)

invcount = 0
lp = 0

for i in range(n):
    v = ar[i]
    invcount += query(sparse,v,n-1)
    update(sparse,v-1,1)
    while invcount > k:
        if lp > i: break
        update(sparse,ar[lp]-1,-1)
        invcount -= query(sparse,0,ar[lp]-1)
        lp += 1
    if invcount == k: ansb[i] = lp

ans = 0
for ii in range(n):
    if ansa[ii] != -1 and ansb[ii] != -1:
        ans += (ansa[ii]-ansb[ii]+1)
    elif ansa[ii] != -1 or ansb[ii] != -1: ans += 1
print(ans)
