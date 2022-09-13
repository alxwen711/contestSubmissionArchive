import sys
from copy import deepcopy
for i in range(int(sys.stdin.readline())):
    n,kk = map(int,sys.stdin.readline().split())
    ar = list(map(int,sys.stdin.readline().split()))
    br = deepcopy(ar)
    for j in range(n):
        br[j] -= (n-j-1)
    #print(br)
    d = {}
    for k in range(n):
        x = br[k]
        if d.get(x) == None: d[x] = list()
        d[x].append(k)
    f = list(d.keys())
    f.sort()
    f.reverse()
    #print(f)
    cr = list()
    for m in range(len(f)):
        cr.extend(d[f[m]])
    h = [0]*n
    for s in range(kk):
        h[cr[s]] = 1
    ans = 0
    inc = 0
    for b in range(n):
        if h[b] == 1: inc += 1
        else: ans += (ar[b] + inc)
    print(ans)
    """
    if jumping over is beneficial, do it, else don't
    """
    
    
