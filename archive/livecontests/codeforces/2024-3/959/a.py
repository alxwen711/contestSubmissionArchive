import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

for _ in range(readint()):
    n,m = readints()
    ar = list()
    for _ in range(n):
        ar.append(readar())
    if n == 1 and m == 1: print(-1)
    elif m == 1:
        tmp = ar[0][0]
        for i in range(n-1):
            ar[i][0] = ar[i+1][0]
        ar[-1][0] = tmp
        for c in ar:
            print(*c)
    else:
        for a in range(n):
            tmp = ar[a][0]
            for b in range(m-1):
                ar[a][b] = ar[a][b+1]
            ar[a][-1] = tmp
        for c in ar:
            print(*c)
        
    
