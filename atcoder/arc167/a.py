import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m = readints()
ar = readar()
ar.sort()
ans = 0
d = n-m
for i in range(d):
    x = ar[i]+ar[2*d-i-1]
    ans += (x*x)
for j in range(m-d):
    ans += (ar[-j-1]*ar[-j-1])
print(ans)
