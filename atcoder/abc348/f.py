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
"""


n,m = readints()
ar = list()
for _ in range(n):
    tmp = readar()
    ar.append(tmp)

cols = list()
for a in range(m):
    d = [0]*1000
    v = 1
    for b in range(n):
        c = ar[b][a]
        d[c] += v
        v <<= 1
    cols.append(d)

ans = 0
de = 1
for i in range(n):
    cv = 0
    for j in range(m):
        x = cols[j][ar[i][j]]
        if x != de: cv ^= cols[j][ar[i][j]]
    if cv & de != 0: cv ^= de
    while cv != 0:
        ans += cv % 2
        cv //= 2
    de <<= 1
#if m % 2 == 1: ans -= n
print(ans//2)
