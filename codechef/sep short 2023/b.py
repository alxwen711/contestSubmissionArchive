import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for i in range(readint()):
    x,h = readints()
    if (5*x//2) >= h: print((h+(x//2-1))//(x//2))
    else:
        ans = 5
        v = h-(5*x//2)
        ans += (v+x-1)//x
        print(ans)
