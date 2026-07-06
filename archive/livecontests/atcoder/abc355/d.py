import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = list()
for _ in range(n):
    a,b = readints()
    ar.append((a,1))
    ar.append((b,2))
ar.sort()
c = 0
ans = 0
for i in range(2*n):
    if ar[i][1] == 1:
        ans += c
        c += 1
    else: c -= 1
print(ans)
