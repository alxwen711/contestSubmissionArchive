import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

def pSet(a,b):
    t = list()
    for snth in range(len(a)):
        if a[snth] == b[snth]: t.append(a[snth])
        else: t.append(3-a[snth]-b[snth])
    return t

def en(x):
    ans = 0
    for e in range(len(x)):
        ans *= 3
        ans += x[e]
    return ans

def een(x,kk):
    return x[0]+(x[1]*(3**kk))+(x[2]*(3**(kk*2)))

def dis(a,b):
    if a[0] == b[0]: return True
    if a[0] == b[1]: return True
    if a[0] == b[2]: return True
    if a[1] == b[0]: return True
    if a[1] == b[1]: return True
    if a[1] == b[2]: return True
    if a[2] == b[0]: return True
    if a[2] == b[1]: return True
    if a[2] == b[2]: return True
    return False

n,kk = readints()
ar = list()
for i in range(n):
    tmp = readar()
    ar.append(tmp)
ar.sort()
d = {}
sets = {}
setset = list()
for o in range(n):
    d[en(ar[o])] = True
for j in range(n):
    for k in range(j+1,n):
        x = pSet(ar[j],ar[k])
        if d.get(en(x)) != None: #exists
            pans = [en(ar[j]),en(ar[k]),en(x)]
            pans.sort()
            p = een(pans,kk)
            if sets.get(p) == None:
                sets[p] = 1
                setset.append(pans)
sets = setset

#may be a faster way to check metasets here
ans = 0
qq = len(sets)
#print(qq)
h = {}
"""
for q in range(qq):
    for r in range(q+1,qq):
        if dis(sets[q],sets[r]): ans += 1
print(ans)
"""

for q in range(qq):
    a,b,c = sets[q][0],sets[q][1],sets[q][2]
    if h.get(a) == None: h[a] = 0
    h[a] += 1
    if h.get(b) == None: h[b] = 0
    h[b] += 1
    if h.get(c) == None: h[c] = 0
    h[c] += 1
hh = list(h.keys())
for sn in range(len(hh)):
    f = h[hh[sn]]
    ans += (f*(f-1))//2
print(ans)
