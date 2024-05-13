import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
if n == 1: print(-1)
else:
    ans = -1
    for i in range(1,n):
        if ar[i] > ar[0]:
            ans = i+1
            break
    print(ans)
