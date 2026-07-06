import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

"""
find an existing rearrangement (always exists?)
ANY set of n-1 edges will work?
take most frequent value, connect this to as many
lower values as possible, repeat
easiest way is to setup order of adding lists
"""

for _ in range(readint()):
    n = readint()
    ar = readar()
    d = {}
    for i in ar:
        if d.get(i) == None: d[i] = 0
        d[i] += 1
    br = list()
    for j in d.keys():
        br.append((-d[j],j))
    br.sort()
    cr = list() # values to add and what order
    dr = list() # indicies to add and what order
    for b in br:
        for _ in range(-b[0]):
            cr.append(b[1])
    for b in br:
        dr.append(b[1])
    h = [1]*n
    for e in dr:
        h[e-1] = 0
    for f in range(n):
        if h[f] == 1: dr.append(f+1)
    dr.append(dr.pop(0))
    ans = [0]*n
    for g in range(n):
        ans[dr[g]-1] = cr[g]
    print(*ans)
