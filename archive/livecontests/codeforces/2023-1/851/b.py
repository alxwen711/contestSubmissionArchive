import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    k = n
    ds = 0
    while k != 0:
        ds += k % 10
        k //= 10
    ds //= 2
    k = str(n)
    ans = 0
    for j in range(len(k)):
        x = min(ds,int(k[-1-j]))
        ans += (x*10**j)
        ds -= x
        if ds == 0: break
    print(n-ans,ans)
