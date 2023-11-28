import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n,x = readints()
    ar = readar()
    ans = ar[0]
    for i in range(1,n):
        ans = max(ans,ar[i]-ar[i-1])
    ans = max(ans,(x-ar[-1])*2)
    print(ans)
