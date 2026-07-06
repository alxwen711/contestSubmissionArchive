import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
ar.sort()
f = 0
ans = 0
for i in range(n):
    x = ar[i]
    while (x-ar[f]) >= m:
        f += 1
    ans = max(ans,i-f+1)
print(ans)
