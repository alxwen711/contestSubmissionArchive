import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ar = readar()
    br = readar()
    cr = list()
    dr = list()
    for j in range(n):
        if ar[j] == 1: cr.append(br[j])
        else: dr.append(br[j])
    cr.sort()
    dr.sort()
    c,d = len(cr),len(dr)
    x = sum(br)*2
    if c > d:
        print(x-sum(cr[:c-d]))
    elif d > c:
        print(x-sum(dr[:d-c]))
    else: print(x-min(cr[0],dr[0]))
