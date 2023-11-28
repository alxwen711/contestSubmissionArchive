import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

m = 998244353

n,x = readints()
ar = readar()
p = [0]*(x+1)
p[0] = 1

denom = pow(n,m-2,m)
#fill probability array
for i in range(1,x+1):
    y = 0
    for j in range(n):
        if i >= ar[j]:
            y += p[i-ar[j]]*denom
    p[i] = (y % m)
ans = 0
for j in range(min(ar[0],x+1)):
    ans += (p[-j-1]*denom)
print(ans % m)
