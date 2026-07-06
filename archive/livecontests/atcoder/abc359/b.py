import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = readar()
a = [-1]*n
b = [-1]*n
for i in range(2*n):
    x = ar[i]-1
    if a[x] == -1: a[x] = i
    else: b[x] = i
ans = 0
for c in range(n):
    if b[c]-a[c] == 2: ans += 1
print(ans)
