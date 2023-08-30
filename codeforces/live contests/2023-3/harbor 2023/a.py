import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x,y,n = readints()
    g = (n*n-n)//2
    if (y-x) < g: print(-1)
    else:
        ans = [0]*n
        ans[0] = x
        ans[-1] = y
        v = y
        for j in range(n-2):
            v -= (j+1)
            ans[-j-2] = v
        print(*ans)
