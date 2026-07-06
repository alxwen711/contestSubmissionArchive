import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


for i in range(readint()):
    n,k = readints()
    ar = readar()
    h = [1]*(n+1)
    for j in ar:
        h[j] = 0
    l = -1
    for m in range(n+1):
        if h[m] == 1:
            l = m
            break
    ar.append(l)
    ans = list()
    for p in range(n):
        ans.append(ar[(k*n+p) % (n+1)])
    print(*ans)
