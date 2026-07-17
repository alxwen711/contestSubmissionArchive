import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

"""
range of values is low (1 to 999)
for each value, track each occurance in grid
if a column is part of a 2+ setup, possible xor

so it turns out that xoring values up to 2**2000 might not be it
tracking each value

alt setup where each index with same cols are tracked
issue here is this could go up to O(n^3) depending on repeat value count
"""


n,m = readints()
ar = list()
for _ in range(n):
    tmp = readar()
    ar.append(tmp)

cols = list()
for a in range(m):
    d = {}
    for b in range(n):
        c = ar[b][a]
        if d.get(c) == None: d[c] = list()
        d[c].append(b)
    cols.append(d)

ans = 0
#de = 1
for i in range(n):
    cv = 0
    h = [0]*n
    for j in range(m):
        for k in cols[j][ar[i][j]]:
            h[k] ^= 1
    ans += sum(h)
    #de <<= 1
if m % 2 == 1: ans -= n
print(ans//2)
