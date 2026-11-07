import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,k = readints()
ar = readar()
ans = ar.count(k)
for i in range(n-1):
    if (ar[i] < k and ar[i+1] > k) or (ar[i] > k and ar[i+1] < k): ans += 1
print(ans)
