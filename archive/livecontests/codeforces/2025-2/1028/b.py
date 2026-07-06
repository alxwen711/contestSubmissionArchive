import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,q = readints()
    br = readar()
    cr = list()
    for _ in range(q):
        x,y,z = readints()
        cr.append((x,y,z))
    ar = deepcopy(br)
    for i in range(q-1,-1,-1):
        ar[cr[i][2]-1] = max(ar[cr[i][0]-1],ar[cr[i][1]-1])
    print(*ar)
