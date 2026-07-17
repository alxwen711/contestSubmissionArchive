import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n = readint()
ar = list()
br = list()
for _ in range(n):
    a,b = readints()
    ar.append(a)
    br.append(b)
ans = 0
s = sum(ar)
for i in range(n):
    ans = max(ans,s-ar[i]+br[i])
print(ans)
