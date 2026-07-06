import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n,x = readints()
    ans = [0]*n
    s = 1
    for j in range(n):
        if s == x: ans[j] = "*"
        elif s > x:
            ans[j] = "-"
            s -= 1
        else:
            ans[j] = "+"
            s += 1
    if s != x: print(-1)
    else: print(*ans,sep="")
