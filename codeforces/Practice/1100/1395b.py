import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n,m,a,b = readints()
ar = [a]
br = [b]
for i in range(1,n+1):
    if i != a: ar.append(i)
for j in range(1,m+1):
    if j != b: br.append(j)
for k in range(n):
    for l in range(m):
        print(ar[k],br[l])
    br.reverse()
