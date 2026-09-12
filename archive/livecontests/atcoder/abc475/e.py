import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
after last query

oxo

oxx
oxx
xxo
oox
ooo

changing wrong to right when already passing does not affect result
changing right to wrong when already failing does not affect result

n <= 30000, k <= 200

possibly a tree works here?

6 million nodes seems wrong here

what if we just cutoff at a certain node size (10?)
"""


n,m,k = readints()

answers = readin()
ar = list() # contestant responses

for _ in range(n):
    s = readin()
    ar.append(s)
for _ in range(readint()):
    i,j = readints()
