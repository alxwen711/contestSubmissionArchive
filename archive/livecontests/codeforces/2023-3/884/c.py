import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def f(ar):
    if len(ar) == 0: return -643897478935743879743897348
    elif len(ar) == 1: return ar[0]
    d = [0]*len(ar)
    d[0] = ar[0]
    for k in range(1,len(ar)):
        d[k] = max(ar[k],ar[k]+d[k-1],d[k-1])
    return max(d)

for i in range(readint()):
    n = readint()
    ar = readar()
    br = list()
    cr = list()
    x = 0
    for d in range(n):
        if x == 0: br.append(ar[d])
        else: cr.append(ar[d])
        x ^= 1
    print(max(f(br),f(cr)))
