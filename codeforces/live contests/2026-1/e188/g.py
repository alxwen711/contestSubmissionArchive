import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
heavily suspecting this is binary exponention via matrix scuff

O(n^2) subarrays possible, matrix mult is O(n^3), binary expo is O(log n)

O(n^6 log n) (yeah I don't think that works)

maybe some modded operation can make this O(n^4 log n)?

use a pseudo dp state
"""



n,m,mod = readints()

# construct_base(m,mod)

c = 0
d = list()
for i in range(m):
    for j in range(i,m):
        d.append((i,j))
        c += 1

matrix = list()
mult = list()
for ii in range(c):
    tmp = [0]*c
    tmp[ii] = 1
    matrix.append(tmp)
    tmp = [0]*c
    mult.append(tmp)

# build set 1 of mult
for a in range(c):
    for b in range(a,c):
        ra = d[a]
        rb = d[b]
        if not (ra[1] < rb[0] or rb[1] < ra[0]):
            mult[a][b] = 1
            mult[b][a] = 1

