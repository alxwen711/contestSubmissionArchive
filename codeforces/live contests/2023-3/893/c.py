import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    d = {}
    for j in range(1,n//2+1):
        d[j] = 2*j
    h = [0]*(n+1)
    ar = list()
    for k in range(1,n+1):
        if h[k] == 0:
            s = k
            ar.append(s)
            h[s] = 1
            while d.get(s) != None:
                s = d[s]
                ar.append(s)
                h[s] = 1
    print(*ar)
