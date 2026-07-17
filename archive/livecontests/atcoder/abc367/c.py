import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,k = readints()
ar = readar()
br = [[]]
for i in ar:
    cr = list()
    for j in br:
        for kk in range(1,i+1):
            dr = deepcopy(j)
            dr.append(kk)
            cr.append(dr)
    br = cr
ans = list()
for b in br:
    if sum(b) % k == 0: ans.append(b)
ans.sort()
for a in ans:
    print(*a)
        
