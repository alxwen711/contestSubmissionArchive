import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()


def solve(n,ar):
    ans = [0]*n
    first = ar[0]
    ans[0] = 1
    prev = first
    reset = False
    for i in range(1,n):
        if reset:
            if ar[i] >= prev and ar[i] <= first:
                ans[i] = 1
                prev = ar[i]
        else:
            if ar[i] >= prev:
                ans[i] = 1
                prev = ar[i]
            elif ar[i] <= first:
                reset = True
                prev = ar[i]
                ans[i] = 1
                
    print(*ans,sep="")

for i in range(readint()):
    n = readint()
    ar = readar()
    solve(n,ar)
