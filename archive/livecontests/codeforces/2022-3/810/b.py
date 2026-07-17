import sys

#input/output functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,m = readints()
    ar = readar()
    pairs = list()
    h = [0]*n
    for j in range(m):
        a,b = readints()
        a -= 1
        b -= 1
        h[a] += 1
        h[b] += 1
        pairs.append([a,b])
    if m % 2 == 0: print(0)
    else:
        ans = 0
        best = 9999999999
        for k in range(n):
            if h[k] % 2 == 1: best = min(best,ar[k])
        for l in range(m):
            if (h[pairs[l][0]]+h[pairs[l][1]]) % 2 == 0:
                best = min(best,ar[pairs[l][0]]+ar[pairs[l][1]])
        print(best)    
