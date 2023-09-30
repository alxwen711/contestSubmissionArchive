import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    n = readint()
    ans = 99999999999999999
    for j in range(n):
        a,b = readints()
        d = (b-1)//2
        if d >= 0: a += d
        ans = min(a,ans)
    print(ans)
