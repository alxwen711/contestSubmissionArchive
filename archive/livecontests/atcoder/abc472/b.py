import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n = readint()
ar = readar()
s = sum(ar)
v = 0
ans = 45378463432432
for i in range(n-1):
    s -= ar[i]
    v += ar[i]
    ans = min(ans,abs(s-v))
print(ans)
