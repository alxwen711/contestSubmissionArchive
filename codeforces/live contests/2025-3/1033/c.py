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
    if (n*n+n)//2 < m or m < n: print(-1)
    else:
        ar = list()
        h = [1]*(n+1)
        h[0] = 0
        for i in range(n):
            remaining = m-(n-i-1)
            if remaining > (n-i):
                h[n-i] = 0
                ar.append(n-i)
                m -= (n-i)
            else:
                h[remaining] = 0
                ar.append(remaining)
                break
        for j in range(n+1):
            if h[j] == 1: ar.append(j)
        print(ar[0])
        for k in range(n-1):
            print(ar[k],ar[k+1])
        
