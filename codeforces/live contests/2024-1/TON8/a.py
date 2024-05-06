import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

for _ in range(readint()):
    n,k = readints()
    if n == k:
        ans = [1]*n
        print(*ans)
    elif k == 1:
        ans = list()
        for i in range(n):
            ans.append(i+1)
        print(*ans)
    else: print(-1)
