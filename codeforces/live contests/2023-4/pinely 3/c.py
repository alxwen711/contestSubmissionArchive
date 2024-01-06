import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
attempt to create longest/shortest intervals possible
is pseudo lt binary optimal here?
all endpoints are distinct, and up to 200000
use a stack for creating segments?
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    cr = readar()
    cr.sort()
    dr = list()
    for i in range(n):
        dr.append((ar[i],1))
        dr.append((br[i],2))    
    dr.sort()
    stack = list()
    er = list()
    for f in range(2*n):
        if dr[f][1] == 1: stack.append(dr[f][0])
        else:
            st = stack.pop()
            er.append(dr[f][0]-st)
    er.sort()
    ans = 0
    for g in range(n):
        ans += er[g]*cr[-g-1]
    print(ans)
